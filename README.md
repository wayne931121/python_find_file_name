# python_find_file_name
find file or dir location.

# Install
```cmd
pip install wfind
```
### Warning
before you install this package, you should check no moudle named find:
```py
#prevent python package name conflicts
import find
#Output: ModuleNotFoundError: No module named 'find'
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
find without base_path will use current directory
```
python -m find --pattern ".png"
```
import
```py
"""
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

import find
result = find.find(".so","/", prt=0)
```

# Code (without installed)
```py
import os, fnmatch

def find(pattern, path, prt=1):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
                if prt: print(result[-1])
        for name in dirs:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
                if prt: print(result[-1])
    return result

find('*yourfilenameordictname*', 'base_path')
find('*.jpg', r'C:\Users\原神\Downloads') #test on windows11, my computer.
find('*.txt', '/') #test on colab linux
find('*.jpg', '/content') #test on colab linux
find('*sample*', '/') #test on colab linux

print()
```

# source and reference
https://stackoverflow.com/a/1724723/19470749 <br>
https://www.runoob.com/python/os-walk.html

# Why I need this script?
I don't know where the huggingface download the model, and after search I know it download to cache folder, but I don't know where it is, so I directly use this script to search D drive and C drive, and then success find.
```py
find("*text_encoder*", "D://")
find("*text_encoder*", "C://")
```

Notice, you can also set huggingface cache dir
```
pipe = CogVideoXImageToVideoPipeline.from_pretrained(model_id,text_encoder=text_encoder,transformer=transformer,vae=vae,torch_dtype=torch.float16,cache_dir="D://3")
```
