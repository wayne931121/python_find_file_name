

pushd %~dp0
python setup.py sdist
pip install dist/wfind-0.0.2.tar.gz --no-build-isolation
pause

