#mypy
echo "Begin mypy check..."
mypy ../discovery/conf/*.py
mypy ../discovery/data/*.py
mypy ./*.py
mypy ../delivery/*.py
pylint ../discovery/conf/*.py
pylint ../discovery/data/*.py
pylint ./*.py
pylint ../delivery/*.py
echo "End mypy check..."
