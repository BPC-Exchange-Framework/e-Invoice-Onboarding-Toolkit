#mypy
echo "Begin mypy check..."
mypy ./*.py
mypy ../*.py
pylint ../*.py
echo "End mypy check..."
