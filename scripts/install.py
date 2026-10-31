"""从下载或克隆的仓库安装 skill；不会覆盖已有目录。"""
import argparse
import os
from pathlib import Path
import shutil
import sys
import tempfile

p=argparse.ArgumentParser(description='安装 performance-engineering；已有安装需自行备份移走')
p.add_argument('--dest',type=Path,default=Path(os.environ.get('CODEX_HOME',str(Path.home()/'.codex')))/'skills')
a=p.parse_args(); source=Path(__file__).resolve().parents[1]/'skills/performance-engineering'
try:
    a.dest.mkdir(parents=True,exist_ok=True)
    target=a.dest/'performance-engineering'
    if target.exists() or target.is_symlink():
        raise FileExistsError(f'已有安装，未修改：{target}')
    with tempfile.TemporaryDirectory(prefix='.skill-install-',dir=a.dest) as tmp:
        staged=Path(tmp)/'performance-engineering'
        shutil.copytree(source,staged,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        # 在复制期间出现的目标也必须被拒绝。
        target.mkdir()
        try:
            for child in staged.iterdir():
                shutil.move(str(child),target/child.name)
        except Exception:
            shutil.rmtree(target)
            raise
    print(f'已安装：{target}；请重新打开 Codex 会话并调用 $performance-engineering')
except OSError as e:
    print(f'安装失败：{e}',file=sys.stderr); sys.exit(1)
