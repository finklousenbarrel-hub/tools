"""项目脚手架：一键生成标准 Python 项目结构
用法: python tools/new_project.py 项目名
"""
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent.parent          # ai-engineering 目录
DIRS = ["src", "tests", "docs", "data"]
GITIGNORE = ".venv/\n__pycache__/\n.pytest_cache/\n.env\n.vscode/\n"
README = "# {name}\n\n（一句话介绍）\n"
AGENTS = "# 项目说明书\n\n## 项目是什么\n\n## 结构地图\n\n## 怎么运行和验证\n\n## 铁律（不许碰）\n"

def run(cmd, cwd):
    # 已填好：在指定目录执行命令，失败就报错退出
    subprocess.run(cmd, cwd=cwd, check=True)

def main():
    if len(sys.argv) != 2:
        print("用法: python tools/new_project.py 项目名")
        return
    root = BASE / sys.argv[1]
    if root.exists():
        print(f"错误：{root} 已存在")
        return

    for d in DIRS:
        (root / d).mkdir(parents=True)
        (root / d / ".gitkeep").touch()

    # TODO 1: 循环 DIRS，创建每个目录（含父目录），并在每个里面放一个 .gitkeep 空文件
    # 提示: (root / d).mkdir(parents=True) 和 (root / d / ".gitkeep").touch()

    (root / ".gitignore").write_text(GITIGNORE, encoding="utf-8")
    (root / "README.md").write_text(README.replace("{name}", sys.argv[1]), encoding="utf-8")
    (root / "AGENTS.md").write_text(AGENTS, encoding="utf-8")

    # TODO 2: 写三个文件：.gitignore / README.md / AGENTS.md
    # 提示: (root / ".gitignore").write_text(GITIGNORE, encoding="utf-8")
    # 注意 README 模板里的 {name} 要替换成项目名

    run([sys.executable, "-m", "venv", ".venv"], cwd=root)
    run(["git", "init"], cwd=root)
    run(["git", "add", "."], cwd=root)
    run(["git", "commit", "-m", "chore: 项目初始化（脚手架生成）"], cwd=root)

    # TODO 3: 创建虚拟环境 + git 初始化 + 首次提交
    # 提示: run([sys.executable, "-m", "venv", ".venv"], cwd=root)
    #       run(["git", "init"], cwd=root)  → add . → commit -m "chore: 项目初始化（脚手架生成）"

    print(f"✅ 项目 {sys.argv[1]} 创建完成：{root}")

if __name__ == "__main__":
    main()