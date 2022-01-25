### Install and Config of a Python Dev Env

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
- Logging
- Editors and other IDEs
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


Upgrade pip to latest version right OOB.  (Note this is done using the Python3/pip3 call to avoid conflict with OS installed version of Python.)
```
pip3 install --upgrade pip
```
The pip update can also be doing using a call to Python itself, but the `python3` install!
```
python3 -m pip install --upgrade pip
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

Creating virtual environments to use in Python programming can be done entirely with a packages that comes in the Pthyon install.  

There are other tool-sets such as [Anaconda](https://www.anaconda.com/products/individual) which provide a full set of development tools and frameworks to pick from, and include the ability to create and manage Python virtual environments with its Conda virtual environment manager.    

There are other additional packages for Python such as ```pyenv```, and ```pipenv``` which can be installed separately.  The example of shown offers one way to create the virtual environments which comes OOB in the Python install and offers a lot of manual control over the packages installed in the virtual environments themselves.


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
12.|pip list | List the installed packages for this virtual env.  This will be a very small list to start as this is a clean virtual env, including ```pip```, ```setuptools```, and ```wheel```.

Additional packages or modules to be installed in e-Invoice include:
Docker, flask, requests

<br /><br />
## Add support for Style and Code checking and Unit Testing.
The Python package ```pep8``` can be installed to do style checking consistent to [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).

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

<br /><br />
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
<br /><br />

## Include Documentation
To incorporate documentation into the application at every step, bring in the Sphinx package. 

```
pip install sphinx
```

Then run sphix-quickstart in your project's top-level directory.

Sphinx uses reStructured Text as a form of Markdown.  For a brief overview see [A ReStructuredText Primer](https://docutils.sourceforge.io/docs/user/rst/quickstart.html) or [Quick reStructuredText](https://docutils.sourceforge.io/docs/user/rst/quicktest.html).

Additonal support documenting the project may include utilzing a resource like [Read the Docs](http://readthedocs.org).

- See also: [PEP-257 Docstring Conventions](https://www.python.org/dev/peps/pep-0257/) 

<br /><br />

## Test Driven Development

Incorporate [Test-Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) methodologies.   
Create the test scenarios before the actual coding.  

Primary source material for review can be found at [obeythetestinggoat.com](https://www.obeythetestinggoat.com)


<br /><br />

## Text Editors and IDEs
There are numerous tools for text editing and softwre development.  Personal preference, specialization versus generalization, and cost may all play a part in choice of tools used for development.  Here is a short list of well known and supported tools available for free or under an Open Source license.  (No compensation isß received for any reference to materials on this page.)
- [Visual Studio Code](https://code.visualstudio.com/) by Microsoft.  "Built on Open Source" the Code version is free and has many plug-ins.  It's a mature IDE with the polish of a Microsoft product.  Not the behemouth of the full Visual Studio IDE.  Available for Windows/Mac/Linux.  There is a version of Visual Studio Code compiled with all the non-Open Source components removed called [VSCodium](https://vscodium.com/).  Or compile it from source available at GitHub resulting in a product called [Code - OSS](https://github.com/Microsoft/vscode/wiki/How-to-Contribute#build-and-run).
- [Atom Text Editor](https://atom.io/).  A highly customizable text editor which is programming language agnostic and completely open source and available (packaged and source) on GitHub.  Available for Windows/Mac/Linux. 
- [PyCharm Community Edition](https://www.jetbrains.com/pycharm/) by JetBrains. A Python specific IDE.  The Community Edition is Free and Open Source, albeit with some limited functionality. Available for Windows/Mac/Linux.

 - (Optional) Install Jupyter lab and notebooks.Jupyter notebooks (deprecated in favor of JupyterLab, though the notebook format remains the same) are especially popular for use in Data Science and ML.  Runs locally on a Python framework. They are used to create documentation in Markdown and write and execute code that might not require an entire program.  Supports other languages such as R and Julia.  Can also be installed through Anaconda.  

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

<br /><br />                                          

## Additional Resources

There is a wealth of high quality documentation and writing about Python in digital and paper print and on the web in addition to that directly refered to above.  As a starting point, see the following materials.  (Again, no compensation is received for any reference to materials on this page.)
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org) by Kenneth Reitz and Tanya Schlusser.
- [Serious Python](https://nostarch.com/seriouspython) by Julien Danjoy
- [Guiding Design Principles](https://nsls-ii.github.io/scientific-python-cookiecutter/guiding-design-principles.html) from the [Scientific Python Cookiecutter](https://nsls-ii.github.io/scientific-python-cookiecutter/index.html).
- [Python Doc](https://www.python.org/doc/) - the official Python web site page of references to more documentation.




<div style="font-size: 12px;
            padding: 15px;
            border: 2px solid lightgray;
            margin-top: 100px;
            margin-left: 0px;
            margin-bottom: 40px;
            margin-right: auto;
            width: 70%;
            border-radius: 10px;">
  <h4 style="font-size: 14px;
            padding: 0px;
            margin: 0px;">No Representations or Warranties</h5>
  This software is free and Open Source offered under an MIT license. The developers of the software make no
  representations or warranties as to the software or its fitness for a particular purpose. This code is meant for
  educational and research purposes only. The code is offered "as-is" and is not intended to be used in a production
  environment. It is intended for developers of software related to the 4-corners Model to use as a stepping-off point
  for further development efforts.
</div>