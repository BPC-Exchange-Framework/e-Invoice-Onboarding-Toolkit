# pylint
echo "Begin all checks..."
echo "Begin pylint check..."
pylint ./*.py
pylint ../discovery/*.py
pylint ../delivery/*.py
echo "End pylint check..."
echo "Begin flake8 check..."
# flake8
flake8 ./*.py
flake8 ../*.py
flake8 ../discovery/*.py
flake8 ../delivery/*.py
echo "End flake8 check..."
echo "If there are no issues to this point then it should pass github CI/CD"
echo "End of checks to satisfy github CI/CD"