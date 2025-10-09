import sys

name = sys.argv[1]
version =  sys.argv[2]

setup = """
from setuptools import setup,find_packages

# print(find_packages())

with open("README.md","r",encoding="utf-8") as f:
    md = f.read()


setup(
    name="%s",
    version="%s",
    author="wayne931121",
    author_email="",
    description="debug",
    long_description=md,
    long_description_content_type="text/markdown",
    license="",
    url="https://github.com/wayne931121",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
)

"""%(name,version)

build = """

pushd %%~dp0
python setup.py sdist
pip install dist/%s-%s.tar.gz --no-build-isolation
pause

"""%(name,version)

with open("setup.py","w",encoding="utf-8") as f:
    md = f.write(setup)

with open("build.bat","w",encoding="utf-8") as f:
    md = f.write(build)