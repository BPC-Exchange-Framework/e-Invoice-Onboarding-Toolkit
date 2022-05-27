# pylint
echo "Begin all checks..."
echo "Begin pylint check..."
cd ../discovery/conf/
DIR=$(pwd) &> /dev/null
cd - &> /dev/null
echo "Pylint code in $DIR"
pylint ../discovery/conf/*.py


cd ../discovery/data/
DIR=$(pwd) &> /dev/null
cd - &> /dev/null
echo "Pylint code in $DIR"
pylint ../discovery/data/*.py


cd ./
DIR=$(pwd) &> /dev/null
cd - &> /dev/null
echo "Pylint code in $DIR"
pylint ./*.py


cd ../discovery/
DIR=$(pwd) &> /dev/null
cd - &> /dev/null
echo "Pylint code in $DIR"
pylint ../discovery/*.py


cd ../delivery/
DIR=$(pwd) &> /dev/null
cd - &> /dev/null
echo "Pylint code in $DIR"
pylint ../delivery/*.py


echo "End pylint check..."
echo "Begin flake8 check..."
# flake8


cd ../discovery/conf/
DIR=$(pwd) &> /dev/null
cd - &> /dev/null
echo "Flake8 check code in $DIR"
flake8 ../discovery/conf/*.py


cd ../discovery/data/
DIR=$(pwd) &> /dev/null
cd - &> /dev/null
echo "Flake8 check code in $DIR"
flake8 ../discovery/data/*.py


cd ./
DIR=$(pwd) &> /dev/null
cd - &> /dev/null
echo "Flake8 check code in $DIR"
flake8 ./*.py


cd ../discovery/
DIR=$(pwd) &> /dev/null
cd - &> /dev/null
echo "Flake8 check code in $DIR"
flake8 ../discovery/*.py


cd ../delivery/
DIR=$(pwd) &> /dev/null
cd - &> /dev/null
echo "Flake8 check code in $DIR"
pylint ../delivery/*.py
cd 

echo "End flake8 check..."
echo "If there are no issues to this point then it should pass github CI/CD"
echo "End of checks to satisfy github CI/CD"