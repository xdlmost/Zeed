# 设置控制台输出编码为 UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

# 加载 UV 环境变量
. "C:\software\pyuv\uv_setenv.ps1"

# 检查虚拟环境是否存在
if (-not (Test-Path .\.venv)) {
    Write-Host "正在创建虚拟环境..."
    uv venv .venv
}

# 激活虚拟环境
. .\.venv\Scripts\Activate.ps1

Write-Host "`n开发环境已准备就绪！"
Write-Host "可用命令："
Write-Host "- zeed check     检查 Zeedfile"
Write-Host "- zeed init      创建新的 Zeedfile"
Write-Host "- uv pip         包管理命令"
Write-Host "- deactivate     退出虚拟环境"
