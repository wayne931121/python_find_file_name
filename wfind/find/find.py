"""
Attribution 4.0 International

Copyright (c) 2025 wayne931121

Usage:

find(pattern, path, prt=1, typeMode="both", matchMode="in")
finder(name, pattern, matchMode)
typeMode:
  both
  file
  folder
matchMode:
  in (in)
  re (regex)
  fm (fnmatch)

"""

import os, fnmatch, re

def finder(name, pattern, matchMode):
    if matchMode=="in":
        return pattern in name
    if matchMode=="re":
        return re.search(pattern,name)
    else:
        return fnmatch.fnmatch(name,pattern)

def find(pattern, path, prt=1, typeMode="both", matchMode="in"):
    result = []
    for root, dirs, files in os.walk(path):
        if typeMode=="both" or typeMode=="file":
            for name in files:
                if finder(name, pattern, matchMode):
                    result.append(os.path.join(root, name))
                    if prt: print(result[-1])
        if typeMode=="both" or typeMode=="folder":
            for name in dirs:
                if finder(name, pattern, matchMode):
                    result.append(os.path.join(root, name))
                    if prt: print(result[-1])
    return result

# if __name__=="__main__":
    # try:
      # find(pattern, base_path)
    # except KeyboardInterrupt:
      # pass