import os
import json
import base64
import hashlib
import asyncio
import aiohttp
import aiofiles
from aiohttp import web
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 配置
UPLOAD_DIR = Path("uploads")
CHUNK_SIZE = 8192  # 8KB chunks
USERS_FILE = "users.json"

# 确保上传目录存在
UPLOAD_DIR.mkdir(exist_ok=True)

# 用户数据
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as f:
        json.dump({
            "admin": {
                "password": hashlib.sha256("admin123".encode()).hexdigest(),
                "role": "admin"
            }
        }, f)

def load_users():
    with open(USERS_FILE, "r") as f:
        return json.load(f)

# 权限验证装饰器
def auth_required(handler):
    async def wrapper(request):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Basic "):
            return web.Response(status=401, text="未授权访问")
        
        try:
            auth_decoded = base64.b64decode(auth_header[6:]).decode()
            username, password = auth_decoded.split(":")
            users = load_users()
            
            if (username in users and 
                users[username]["password"] == hashlib.sha256(password.encode()).hexdigest()):
                request["user"] = {"username": username, "role": users[username]["role"]}
                return await handler(request)
        except Exception:
            pass
        
        return web.Response(status=401, text="认证失败")
    return wrapper

# 路由处理函数
@auth_required
async def list_files(request):
    files = []
    for file_path in UPLOAD_DIR.glob("*"):
        if file_path.is_file():
            files.append({
                "name": file_path.name,
                "size": file_path.stat().st_size,
                "modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
            })
    return web.json_response(files)

@auth_required
async def upload_file(request):
    if request["user"]["role"] != "admin":
        return web.Response(status=403, text="需要管理员权限")
    
    reader = await request.multipart()
    field = await reader.next()
    
    if field is None:
        return web.Response(status=400, text="没有文件")
    
    filename = field.filename
    if not filename:
        return web.Response(status=400, text="无效的文件名")
    
    file_path = UPLOAD_DIR / filename
    try:
        async with aiofiles.open(file_path, 'wb') as f:
            while True:
                chunk = await field.read_chunk(CHUNK_SIZE)
                if not chunk:
                    break
                await f.write(chunk)
    except Exception as e:
        return web.Response(status=500, text=f"上传失败: {str(e)}")
    
    return web.Response(text=f"文件 {filename} 上传成功")

@auth_required
async def download_file(request):
    filename = request.match_info['filename']
    file_path = UPLOAD_DIR / filename
    
    if not file_path.exists():
        return web.Response(status=404, text="文件不存在")
    
    try:
        response = web.StreamResponse()
        response.headers['Content-Disposition'] = f'attachment; filename="{filename}"'
        response.headers['Content-Type'] = 'application/octet-stream'
        
        await response.prepare(request)
        
        async with aiofiles.open(file_path, 'rb') as f:
            while True:
                chunk = await f.read(CHUNK_SIZE)
                if not chunk:
                    break
                await response.write(chunk)
        
        return response
    except Exception as e:
        return web.Response(status=500, text=f"下载失败: {str(e)}")

@auth_required
async def delete_file(request):
    if request["user"]["role"] != "admin":
        return web.Response(status=403, text="需要管理员权限")
    
    filename = request.match_info['filename']
    file_path = UPLOAD_DIR / filename
    
    if not file_path.exists():
        return web.Response(status=404, text="文件不存在")
    
    try:
        os.remove(file_path)
        return web.Response(text=f"文件 {filename} 删除成功")
    except Exception as e:
        return web.Response(status=500, text=f"删除失败: {str(e)}")

# 创建应用
app = web.Application()
app.router.add_get('/files', list_files)
app.router.add_post('/upload', upload_file)
app.router.add_get('/download/{filename}', download_file)
app.router.add_delete('/files/{filename}', delete_file)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080) 