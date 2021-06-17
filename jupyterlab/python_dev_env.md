## Installation and Configuration of a Python Dev Environment Capable of Producing Production Ready Artifacts

This document outlines the creation of a Python Development Environment consistent with Python standards and best practices and appropriate as a starting point for professional software development with Python.  

Important items for consideration include:
- Installation of Python
- Use of virtual environments for project and application segmentation.
- Bringing in the required tools sets for:
    - Style checking against PEP8
    - Automated code checking using ```flake8``` and ```tox```
    - Includng documentation using Sphinx and reStructuredText.
- Including Docker and flask
- Incorporating Test Drive Development as a matter of practice.
- Optionally, installing JupyterLab.
- Links to additional resources.


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


Upgrade pip to latest version right OOB. 
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
7.|ls -l|list contents of current directory structure|
 |  |drwxr-xr-x  7 kelly  staff  224 Jun 15 08:52 e-Invoice
 8.|cd ./e-Invoice|Change into the e-Invoice directory 
9.|cd ../bin|Change into the bin directory
10.|source ./activate | source the activate file and make the current virtual environment active.
11.|python -m pip install --upgrade pip | update version of pip 
12.|pip list | list the installed default modules and packages for this virtual env.

Additional packages or modules to be installed in e-Invoice include:
Docker, flask, requests

## Add support for Style and Code checking and Unit Testing.
A Python package can be installed to do style checking consistent to [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).

```
pip install pep8
```

Run your code against it in the following manner:
```
pep8 <filename>
e.g., pep8 hello.py
```

then the output from the cosole using:
``` 
echo $?
```

Another module, flake8, checks for code style and errors simultanepously.  There are a number of custom plug-ins to focus on various aspects of code validation.  

```
pip install flake8
```


The ```tox``` tool can be used to manage dependencies in virtual environments and Unit Test.

```
pip install tox
```


## Docker and flask

This project utilize [Docker](https://www.docker.com) and [flask](https://pypi.org/project/Flask/).

For support of Docker development on the Mac, use Homebrew as outlined above to install Docker locally.  If necessary to issue Docker commands or use the Docker API from with Python, include the Docker package in the virtual environment.

```
pip install docker
```

Install the flask framework using pip as well.

```
pip install flask
```

## Include documentation
To incorporate documentation into the application at every step, bring in the Sphinx package.  

Then run sphix-quickstart in your project's top-level directory.

Sphinx uses reStructured Text as a form of Markdown.  For a brief overview see [A ReStructuredText Primer](https://docutils.sourceforge.io/docs/user/rst/quickstart.html) or [Quick reStructuredText](https://docutils.sourceforge.io/docs/user/rst/quicktest.html).

Additonal support documenting the project may include utilzing a resource like [Read the Docs](http://readthedocs.org).

- See also: [PEP-257 Docstring Conventions](https://www.python.org/dev/peps/pep-0257/) 



## Test Driven Development

Incorporate the goals of Test Driven Development.  Create the test scenarios before the actual coding.  

Primary source material for review can be found at [obeythetestinggoat.com](https://www.obeythetestinggoat.com)




## (Optional) Install Jupyter lab and notebooks.

Jupyter notebooks (deprecated in favor of JupyterLab, though the notebook format remains the same) are especially popular for use in Data Science and ML.  They are convenient to document in Markdown and code that might not scale to an entire program.  

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
                                                                                                            
## Additional Resources

There is a wealth of high quality documentation and writing about Python in digital and paper print and on the web in addition to that directly refered to above.  As a starting point, see the following materials.  (No compensation is received for any reference to materials on this page.)
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org) by Kenneth Reitz and Tanya Schlusser.
- [Serious Python](https://nostarch.com/seriouspython) by Julien Danjoy
- [Guiding Design Principles](https://nsls-ii.github.io/scientific-python-cookiecutter/guiding-design-principles.html) from the [Scientific Python Cookiecutter](https://nsls-ii.github.io/scientific-python-cookiecutter/index.html).
- [Python Doc](https://www.python.org/doc/) - the official Python web site page of references to more documentation.

