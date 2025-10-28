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
python -m find --base_path "C:\" --mode "re" -re ".pdf$" 
python -m find --base_path "C:\" --pattern "*.jpg" --mode "fm" 

python -m find --help
usage: __main__.py [-h] [-p BASE_PATH] [-d PATTERN] [-file] [-folder] [-m MODE] [-re RE]

Find File or Folder Name.

options:
  -h, --help            show this help message and exit
  -p, --base_path BASE_PATH
                        base path
  -d, --pattern PATTERN
                        dest pattern
  -file, --file         only search file
  -folder, --folder     only search folder
  -m, --mode MODE       mode: -m in, -m fm, -re
  -re, --re RE          regex
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



