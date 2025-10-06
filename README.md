# python_find_file_name
find file or dir location.

# Code
```py
import os, fnmatch

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
        for name in dirs:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

find('*yourfilenameordictname*', 'base_path')
find('*.txt', '/')
find('*.jpg', '/content')
find('*sample*', '/')
```

# source and reference
https://stackoverflow.com/a/1724723/19470749 <br>
https://www.runoob.com/python/os-walk.html
