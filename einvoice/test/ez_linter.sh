# pylint
echo "Begin all checks..."
echo "Begin pylint check..."
cd ../discovery/conf/
DIR=$(pwd)
echo "Pylint code in ${DIR}"
pylint *.py
cd ../../test


cd ../discovery/data/
DIR=$(pwd)
echo "Pylint code in ${DIR}"
pylint *.py
cd ../../test


DIR=$(pwd)
echo "Pylint code in ${DIR}"
pylint *.py


cd ../discovery/
DIR=$(pwd)
echo "Pylint code in ${DIR}"
pylint *.py


cd ../delivery/
DIR=$(pwd)
echo "Pylint code in ${DIR}"
pylint *.py


echo "End pylint check..."
echo "Begin flake8 check..."
# flake8


cd ../discovery/conf/
DIR=$(pwd)
echo "Flake8 check code in $DIR"
flake8 *.py
cd ../../test


cd ../discovery/data/
DIR=$(pwd)
echo "Flake8 check code in $DIR"
flake8 *.py
cd ../../test


DIR=$(pwd)
echo "Flake8 check code in $DIR"
flake8 *.py


cd ../delivery/
DIR=$(pwd)
echo "Flake8 check code in $DIR"
flake8 *.py
cd ../test

echo "End flake8 check..."
echo "If there are no issues to this point then it should pass github CI/CD"
echo "End of checks to satisfy github CI/CD"