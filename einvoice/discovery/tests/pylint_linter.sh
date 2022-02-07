# pylint
echo "Begin all checks..."
echo "Begin pylint check..."
pylint ../conf/*.py
pylint ../data/*.py
pylint ./*.py
pylint ../*.py
echo "End pylint check..."
