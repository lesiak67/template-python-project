#! /bin/bash
source .venv/bin/activate
python -m pylint main.py  tests/test_calculate.py tests/test_errors.py