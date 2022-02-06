# pylint
echo "Begin all checks..."
echo "Begin pylint check..."
pylint ../conf/*.py
pylint ../data/*.py
pylint ./*.py
pylint ../*.py
echo "End pylint check..."
echo "Begin flake8 check..."
# flake8
flake8 ../conf/*.py
flake8 ../data/*.py
flake8 -qq ./*.py
flake8 ../*.py
pylint ../*.py
echo "End flake8 check..."
echo "If there are no issues to this point then it should pass github CI/CD"
echo "Begin mypy check..."
#mypy
mypy ../conf/*.py
mypy ../data/*.py
mypy ./*.py
mypy ../*.py
pylint ../*.py
echo "End mypy check..."
echo "Begin pycodestyle check..."
#pycodestyle
pycodestyle ../conf/*.py
pycodestyle ../data/*.py
pycodestyle ./*.py
pycodestyle ../*.py
echo "End pycodestyle check..."
echo "Begin pydocstyle check..."
#pydocstyle
pydocstyle ../conf/*.py
pydocstyle ../data/*.py
pydocstyle ./*.py
pydocstyle ../*.py
echo "End pydocstyle check..."
echo "End of all checks"