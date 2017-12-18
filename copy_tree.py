import shutil
import sys
import os

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        print(item)
        if item == 'blog' or item == '.git':
            continue

        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

SOURCE_DIR = os.getcwd()
TARGET_DIR = os.path.abspath(sys.argv[1])

if os.path.exists(TARGET_DIR):
    shutil.rmtree(TARGET_DIR)

os.makedirs(TARGET_DIR)
copytree(SOURCE_DIR, TARGET_DIR)
