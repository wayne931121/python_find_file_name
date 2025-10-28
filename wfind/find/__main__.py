import sys
import platform
import os, fnmatch, re
import argparse


matchMode = "in"
typeMode = "both"
reg = None

p = platform.system()
if p=="Linux":
  default_path = "/"
else:
  default_path = "C:\\"

parser = argparse.ArgumentParser(description="Find File or Folder Name.")
parser.add_argument("-p", "--base_path", dest="base_path", default=default_path, type=str, help="base path")
parser.add_argument("-d", "--pattern", dest="pattern", default=".jpg", type=str, help="dest pattern")
parser.add_argument("-file", "--file", dest="file", action='store_true', help="only search file")
parser.add_argument("-folder", "--folder", dest="folder", action='store_true', help="only search folder")
parser.add_argument("-m", "--mode", dest="mode", default="in", type=str, help="mode: -m in, -m fm, -re")
parser.add_argument("-re", "--re", dest="re", default=".jpg$", type=str, help="regex")
args = parser.parse_args()

matchMode = args.mode
pattern = args.pattern
base_path = args.base_path
reg = args.re

if args.file:
    typeMode = "file"
elif args.folder:
    typeMode = "folder"
    
def finder(name,pattern):
    if matchMode=="in":
        return pattern in name
    if matchMode=="re":
        return re.search(reg,name)
    else:
        return fnmatch.fnmatch(name,pattern)

def find(pattern, path, prt=1):
    result = []
    for root, dirs, files in os.walk(path):
        if typeMode=="both" or typeMode=="file":
            for name in files:
                if finder(name, pattern):
                    result.append(os.path.join(root, name))
                    if prt: print(result[-1])
        if typeMode=="both" or typeMode=="folder":
            for name in dirs:
                if finder(name, pattern):
                    result.append(os.path.join(root, name))
                    if prt: print(result[-1])
    return result

# find('*yourfilenameordictname*', 'base_pathase_path')
try:
  find(pattern, base_path)
except KeyboardInterrupt:
  pass