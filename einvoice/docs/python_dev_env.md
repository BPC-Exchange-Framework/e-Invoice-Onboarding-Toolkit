# Configure a Python Dev Environment

Respecting individual preferences and work style these are some suggested guidelines  for creation of a Python development environment.  These are consistent with Python standards and best practices and appropriate as a starting point for professional software development in Python.  

<!-- _Important items for consideration include:_
- Installation of Python
- Use of virtual environments for project and application segmentation.
- Including resources for:
    - Style checking against PEP8
    - Test drive-development including unit tests from the beginning.
    - Include documentation using __docstrings__ while coding.
- Including Docker and flask
- Incorporating Test Drive Development as a matter of practice.
- Logging
- Editors and other IDEs
- Links to additional resources. -->


## Installing Python

The correct method of installing Python varies depending on the OS.  Here are some considerations based on popular OS.

OS | Considerations
----------- | -----------
MacOS | Mac OS comes configured with Python 2.x. This version of Python is required by the OS and removal will impair system function.  [Homebrew](https://brew.sh) is a package installer for Mac. Using Homebrew  to install Python versions prior to 3.7 may generate errors on  instal due to deprecated libraries.  That isues has been resolved for versions 3.7 and higher.[Apple XCode Developer Tools](https://developer.apple.com/xcode/) installs Git and a version of Python.  Available through the App Store it is a large download and system intensive program which may not run smoothly on older or less robust systmes.  A more granular installation would be the [XCode Command Line Tools](https://mac.install.guide/commandlinetools/4.html) which installs Git combined with a Python install pulled directly from Python.org.      
WindowsOS | Python is now available on the [Windows Store](https://www.microsoft.com/en-us/store/apps/windows), though updates may lag behind current Python releases at python.org before arriving on the Windows Store.  The option to set environment variables via a UI on a per user basis facilitates multiple installed versions simultaneously.  [VS Code](https://code.visualstudio.com/) from Miscrosoft integrates direcltly with a system installled version of Python.
Windows WLS2 | A fully native Python install on Ubuntu is available for [Windows Subsystem for Linux 2](https://docs.microsoft.com/en-us/windows/wsl/install).  The version of Python may need to be updated from a secondary repository as the official Ubuntu version trails official Python releases.  Integration between VS Code running on Windows and integration with WSL2 Python may require custom configuration.
Linux | A variety of package managers based on the installed distro enable installation and updates through a GUI or command line.

??? info "Python3"
    Python is officially referred to and invoked by specfiying either Python 2.x as  "Python2" or Python 3.x.x as "Python3."  The difference is generally trivial except on Macs where Python2 is included as part of the OS install.  

    On Mac and Linux based systems, adding an alias to .bashrc or .zshrc is an easy way to prevent inadvertent references to an incorrect version of Python, e.g.,
    ```
    alias python='python3'
    alias pip='pip3'
    ```
    Note that the above included an alias for pip to pip3 as well.  



## Create a virtual environment to use for Dev

A Python virtual environment is a development sandbox which allows for segmentation of development environments. This allows for management of different combinations and versions of Python releases, deployed packages, development and testing environments, and shifting between entirely different development projects. See the [Python documentation for venv](https://docs.python.org/3/library/venv.html) for a more detailed explanation and rationalization of Python virtual environments.

The use of Python virtual environments can't be overstated as a best practice to organize Python versions and package management. [PEP-405](https://www.python.org/dev/peps/pep-0405/)

Creating virtual environments to use in Python programming can be done entirely with packages that are include in the Python install or by additional third party applications.    

The choice of tools to create and manage Python virtual environments is dependent on situation, preference, and use case.  

| Tool/App | Use Case |
------------ | ------------
| [venv](https://docs.python.org/3/library/venv.html) | Implementation of the virtualenv as a Python module included in the Python install since v.3.3.  This tool does not require installation outside of the Python distribution itself.  |
| [virtualenv](https://virtualenv.pypa.io/en/latest/index.html) | Includes features not included in venv (see the [comparison](https://virtualenv.pypa.io/en/latest/index.html)). |  
| [Anaconda](https://www.anaconda.com/)  | A heavyweight package and virtual environment manager.  It acts as an "all in one" for Python application versions, package management, virtual environments, additional programming languages such as R and Julia and tools such as visualizers and IDEs. The full fledged install can overtax some systems and performance can suffer from an overly ambitious installation configuration. A personal license for individuals is free for non-commercial use.  Use by for-profit or governmental organizations with more than 200 people requires licensing. |
| [miniconda](https://docs.conda.io/en/latest/miniconda.html) | A slimmed down version of Anaconda focused on virtual environment and package management, includes only conda and Python, not open source, but free. |
| [conda](https://docs.conda.io/en/latest/) | The open source package manager utilized by Anaconda and miniconda. |
| [pip](https://pip.pypa.io/en/stable/) | Included in Python 3.4 and later, this tool does not manage the virtual environment but does handle package management for both venv and virtualenv. Not all python tools have been integrated into the Anaconda repositories or packages for install.  Some, such as mkdocs, must still be installed via pip even when using Anaconda3 or miniconda.  

??? tip "'virtualenv venv' vs. 'venv virtualenv'"
    Avoid the confusion of the typical example given in the documentation of __virtualenv__ which uses the command executed as "virtualenv venv." This calls __virtualenv__ to create a virtual environment named __venv__.  

    Compare with "venv virtualenv" which calls __venv__ to create a virtual environment called __virtualenv__.  For most practical purposes when using Python 3.6 or greater it doesn't matter whether __venv__ or __virtualenv__ is used to create the virtual instance.

    It's recommended to  name a virutal environment with a single word unique identifier as the word will be prefixed to the terminal command line when the virtual environment  is activated. 

 



???+ note "Other Python Tools"
    Other tools such as [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), [pipenv](https://pipenv.pypa.io/en/latest/), [pew](https://github.com/berdario/pew), [tox](https://tox.wiki/en/latest/) and [nox](https://nox.thea.codes/en/stable/), [poetry](https://python-poetry.org/), and [black](https://black.readthedocs.io/en/stable/) may be useful but are not currently utilized in this project.  [Pyenv](https://github.com/pyenv) was deprecated in Python 3.5 and not utilized.





<br/>
<br/>
<br/>