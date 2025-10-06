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
find('*.jpg', r'C:\Users\原神\Downloads') #test on windows11
find('*.txt', '/') #test on colab linux
find('*.jpg', '/content') #test on colab linux
