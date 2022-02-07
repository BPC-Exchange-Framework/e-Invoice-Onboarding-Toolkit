echo "Begin pydocstyle check..."
pydocstyle ../conf/*.py
pydocstyle ../data/*.py
pydocstyle ./*.py
pydocstyle ../*.py
echo "End pydocstyle check..."
