# pylint
echo "Begin all checks..."
echo "Begin pylint check..."
HOME=/Users/kelly/Dev/github/e-Invoice-Onboarding-Toolkit/einvoice/
cd $HOME/discovery/conf/
pylint ./*.py
cd $HOME/discovery/data/
pylint ./*.py
cd $HOME/test/
pylint ./*.py
cd $HOME/discovery/
pylint ./*.py
cd $HOME/delivery
pylint ./*.py
echo "End pylint check..."
echo "Begin flake8 check..."
# flake8
cd $HOME/discovery/conf/
flake8 ./*.py
cd $HOME/discovery/data/
flake8 ./*.py
cd $HOMe/test/
flake8 ./*.py
cd $HOME/discovery/
flake8 ./*.py
cd $HOME/delivery
flake8 ./*.py
echo "End flake8 check..."
echo "If there are no issues to this point then it should pass github CI/CD"
echo "End of checks to satisfy github CI/CD"
