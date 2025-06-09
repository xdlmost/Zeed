"""
Zeed 包描述文件
定义包的构建和配置信息
"""

from zeed.templates.package_template import Package

# 创建包配置
pkg = Package("zeed")
pkg.description = "Python包管理工具"
pkg.author = "开发者"
pkg.author_email = "developer@example.com"
pkg.keywords = ["package", "management", "build"]

# 设置环境变量
pkg.env.version = "0.1.0"
pkg.env.set_var("PYTHON_PATH", "python3")
pkg.env.set_var("PIP_INDEX_URL", "https://pypi.tuna.tsinghua.edu.cn/simple")

# 添加源文件
pkg.builder.add_source([
    "src/zeed/*.py",
    "src/zeed/templates/*.py"
])

# 添加测试文件
pkg.builder.add_source([
    "tests/*.py"
])

# 添加构建依赖
pkg.build_requires.update({
    "wheel": ">=0.37.0",
    "setuptools": ">=58.0.0",
})

# 添加测试依赖
pkg.test_requires.update({
    "pytest": ">=7.0.0",
    "pytest-cov": ">=3.0.0",
})

# 添加运行依赖
pkg.install_requires.update({
    "click": ">=8.0.0",
    "pyyaml": ">=6.0.0",
    "requests": ">=2.26.0",
})

# 配置构建目标
pkg.targets["build"] = [
    "src/zeed",
    "src/zeed/templates"
]

pkg.targets["test"] = [
    "tests/test_*.py"
]

pkg.targets["install"] = [
    "src/zeed",
    "README.md",
    "LICENSE"
]

pkg.targets["clean"] = [
    "build/*",
    "dist/*",
    "*.egg-info",
    "**/__pycache__",
    "**/*.pyc"
]

if __name__ == "__main__":
    # 执行构建流程
    pkg.configure()
    
    # 根据命令行参数执行不同的操作
    import sys
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "build":
            pkg.build()
        elif command == "test":
            pkg.test()
        elif command == "install":
            pkg.install()
        elif command == "clean":
            pkg.clean()
        else:
            print(f"未知命令: {command}")
            print("可用命令: build, test, install, clean")
            sys.exit(1)
    else:
        # 默认执行完整构建流程
        pkg.build()
        pkg.test()
        pkg.install() 