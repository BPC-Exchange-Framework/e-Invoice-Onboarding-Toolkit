#mypy
echo "Begin mypy check..."
mypy ../conf/*.py
mypy ../data/*.py
mypy ./*.py
mypy ../*.py
pylint ../*.py
echo "End mypy check..."
