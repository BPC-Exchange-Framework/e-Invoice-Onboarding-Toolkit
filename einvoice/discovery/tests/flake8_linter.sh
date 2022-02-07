echo "Begin flake8 check..."
# flake8
flake8 ../conf/*.py
flake8 ../data/*.py
flake8 -qq ./*.py
flake8 ../*.py
pylint ../*.py
echo "End flake8 check..."
