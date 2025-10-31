"""
################################################################

Attribution 4.0 International

Copyright (c) 2025 wayne931121

################################################################
__main__.py:

# python_find_file_name
find file or dir location.

# Install
```cmd
pip install wfind
```

# Usage
python -m find "base_path" "file_or_directory_name"
```cmd
python -m find --base_path "C:\" --pattern ".mp4"
python -m find --base_path "C:\" --pattern "mat" --mode "in" --folder
python -m find --base_path "C:\" --pattern ".png" --mode "in" --file
python -m find --base_path "C:\" --pattern ".pdf$" --mode "re"
python -m find --base_path "C:\" --pattern "*.jpg" --mode "fm" 

python -m find --help
usage: Python File Finder [-h] [-p BASE_PATH] [-d PATTERN] [-file] [-folder] [-m MODE]

Find File or Folder Name.

options:
  -h, --help            show this help message and exit
  -p, --base_path BASE_PATH
                        base path
  -d, --pattern PATTERN
                        dest pattern
  -file, --file         only search file
  -folder, --folder     only search folder
  -m, --mode MODE       mode: -m in, -m fm, -m re
```
##############################################################
find.py

```
from find import find

or

import find
```

```
find.find
find.finder
```


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

try:
    from .find import *
except:
    from find import *