

pushd %~dp0
python setup.py sdist
python setup.py bdist_wheel
pip install dist/wfind-0.0.4.tar.gz --no-build-isolation
pause

