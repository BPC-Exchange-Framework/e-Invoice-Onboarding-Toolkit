## Python installation and configuration.


Note:  This documentation assumes running on MacOS.  All tools should be available in Windows and various flavors of Linux.  Your mileage may vary. 

Install Homebrew using command:  
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Then install Python.
```
brew install python
```

```
Install other tools you may need or want using Homebrew.  These will make life easier.
brew install --cask visual-studio-code
brew install node
brew install r
brew install rstudio
brew install typescript
brew install docker
brew install --cask powershell
```


Upgrade pip right OOB as it always seems to be a bit out of date... 
```
pip3 install --upgrade pip
```

Get a list of what's been installed in a "clean" install of Python.
```
pip3 list

Package          Version
---------------- ----------
appdirs          1.4.4
certifi          2020.12.5
distlib          0.3.1
filelock         3.0.12
pip              21.1.2
pipenv           2020.11.15
setuptools       56.0.0
six              1.16.0
virtualenv       20.4.6
virtualenv-clone 0.5.4
```


## Create a virtual environment to use for Dev
Step|Command|What it's doing/output
---|---|---
1.|cd|Change to user home dir
2.|pwd|Print the working directory
 | |/Users/kelly|output of pwd command
3.|mkdir ./Dev ./Dev/virtualenvs|Create working directories 
4.|cd ./Dev/virtualenvs|Change into the working directory
5.|pwd| Print the working directory
 | |/Users/kelly/Dev/virtualenvs|
6.|virtualenv --python python3.9 e-Invoice|Create the e-Invoice virtual environment
7.|cd ../e-Invoice|Change into the e-Invoice directory  
8.|ls -l|list contents of current directory structure
 | |drwxr-xr-x  7 kelly  staff  224 Jun 15 08:52 e-Invoice
9.|cd ../bin|Change into the bin directory
10.|source ./activate | source the activate file and make the current virtual environment active.
11.|python -m pip install --upgrade pip | update version of pip 
12.|pip list | list the installed default modules and packages for this virtual env.

Additional packages or modules to be installed in e-Invoice include:
Docker, flask, requests






## Create a virtual environment to use working with Jupiter notebooks.
```
cd /Users/kelly/Dev/virtualenvs
virtualenv --python python3.9 jupiter
python -m pip install --upgrade pip
pip install jupyter
pip install jupyterlab
```  
  
Start jupyterlab by running it from within your Python virtualenv /bin directory.  
At runtime, point it to the location of your GITHub root, e.g.,   
```
./jupyter-lab --notebook-dir /Users/kelly/GitHub
```
                                                                                                            


<!-- ## Create a virtual environment to use working with NinjaIDE (require PyQt5)
```
cd /Users/kelly/Dev/virtualenvs
virtualenv --python python3.9 ninja-ide
python -m pip install --upgrade pip
pip install PyQt5
```

Clone the NinjaIDE repository from GitHub at https://github.com/ninja-ide/ninja-ide.git,
In the clone cd to ninja-ide
The first time you will need to run this line, but should not required every time unless there is an update to one it's dependencies: 
```
pip install requirements.txt
```
To run the IDE, from the ninja-ide root run:
```
python ninja-ide.py
```
-->
