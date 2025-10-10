# python_find_file_name
find file or dir location.

# Install
https://github.com/wayne931121/python_find_file_name/blob/main/wfind/README.md

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
