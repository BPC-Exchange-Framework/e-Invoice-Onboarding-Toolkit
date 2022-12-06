# pylint
echo "Begin all checks..."
echo "Begin pylint check..."
pylint ../discovery/conf/*.py
pylint ../discovery/data/*.py
pylint ./*.py
pylint ../discovery/*.py
pylint ../delivery/*.py
echo "End pylint check..."
