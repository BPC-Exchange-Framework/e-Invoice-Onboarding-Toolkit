#pycodestyle
echo "Begin pycodestyle check..."
pycodestyle ../conf/*.py
pycodestyle ../data/*.py
pycodestyle ./*.py
pycodestyle ../*.py
echo "End pycodestyle check..."
