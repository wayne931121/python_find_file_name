import sys
import platform
import os
import argparse

try:
    from .find import find
except:
    from find import find

matchMode = "in"
typeMode = "both"

# p = platform.system()
# if p=="Linux":
  # default_path = "/"
# else:
  # default_path = "C:\\"

default_path = os.getcwd()

parser = argparse.ArgumentParser(description="Find File or Folder Name.")
parser.add_argument("-p", "--base_path", dest="base_path", default=default_path, type=str, help="base path")
parser.add_argument("-d", "--pattern", dest="pattern", default=".jpg", type=str, help="dest pattern")
parser.add_argument("-file", "--file", dest="file", action='store_true', help="only search file")
parser.add_argument("-folder", "--folder", dest="folder", action='store_true', help="only search folder")
parser.add_argument("-m", "--mode", dest="mode", default="in", type=str, help="mode: -m in, -m fm, -m re")
parser.prog = "Python File Finder"
args = parser.parse_args()

matchMode = args.mode
pattern = args.pattern
base_path = args.base_path

if args.file:
    typeMode = "file"
elif args.folder:
    typeMode = "folder"

if __name__=="__main__":
    try:
      find(pattern, base_path, typeMode=typeMode, matchMode=matchMode)
    except KeyboardInterrupt:
      pass