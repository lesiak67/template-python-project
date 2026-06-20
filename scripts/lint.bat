@echo off
call .venv\Scripts\activate.bat
python -m pylint main.py tests/test_calculate.py tests/test_errors.py --exit-zero