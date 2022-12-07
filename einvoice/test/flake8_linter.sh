echo "Begin flake8 check..."
# flake8
flake8 -qq ./*.py
flake8 ../*.py
pylint ../*.py
echo "End flake8 check..."
