
from setuptools import setup,find_packages

# print(find_packages())

with open("README.md","r",encoding="utf-8") as f:
    md = f.read()


setup(
    name="wfind",
    version="0.0.4",
    author="wayne931121",
    author_email="",
    description="Find file or folder by Python, Faster than Windows File Explorer.",
    long_description=md,
    long_description_content_type="text/markdown",
    license="Attribution 4.0 International, Copyright (c) 2025 wayne931121.",
    url="https://github.com/wayne931121/python_find_file_name",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
)

