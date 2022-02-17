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
MacOS | Mac OS comes configured with Python 2.x. Don't attempt to remove it or replace it .  [Homebrew](https://brew.sh) is a package installer for Mac. However given some past and outstanding issues between Homebrew and Python, versions of Python prior to Python 3.7 may generate errors on install.  [Apple XCode Developer Tools](https://developer.apple.com/xcode/) installs Git and a version of Python.  Available through the App Store it is a large download and system intensive program.  A more granular installation would be the [XCode Command Line Tools](https://mac.install.guide/commandlinetools/4.html) which installs Git combined with a Python install pulled directly from Python.org.      
WindowsOS | Python is now available on the [Windows Store](https://www.microsoft.com/en-us/store/apps/windows), though updates may lag behind current Python releases.  Ease of setting environment variables makes it easy to maintain multiple installed versions simultaneously.  This configuration is the easiest to integrate [VS Code](https://code.visualstudio.com/) with Python.
Windows WLS2 | A fully native Python install on Ubuntu is available for [Windows Subsystem for Linux 2](https://docs.microsoft.com/en-us/windows/wsl/install).  The version of Python may need to be updated from a secondary repository as the official Ubuntu version trails official Python releases.  Integration between VS Code running on Windows and integration with WSL2 Python may not be seamless.
Linux | A variety of package managers based on the installed distro may impact the ease of installing current Python releases and updates, but overall this possibly the easiest to "OS" to install and maintain Python.  

??? info "Python3"
    Python is "officially" referred to and invoked by specfiying either Python 2.x as  "Python2" or Python 3.x.x as "Python3."  The difference is generally trivial except on Macs where Python2 is included as part of the OS install.  

    On Mac and Linux based systems, adding an alias to .bashrc or .zshrc is an easy way to prevent inadvertent references to an incorrect version of Python, e.g.,
    ```
    alias python='python3'
    alias pip='pip3'
    ```
    Note that the above included an alias for pip to pip3 as well.  



## Create a virtual environment to use for Dev

A Python virtual environment is a development "sandbox" which allows for segmentation of development environments. This allows for management of different combinations and versions of Python releases, deployed packages, development and testing environments, and shifting between entirely different development projects. See the [Python documentation for venv](https://docs.python.org/3/library/venv.html) for a more detailed explanation and rationalization of Python virtual environments.

The use of Python virtual environments can't be overstated as a best practice to organize Python versions and package management. [PEP-405](https://www.python.org/dev/peps/pep-0405/)

Creating virtual environments to use in Python programming can be done entirely with packages that are include in the Pthyon install or by additional third party applications.    

The choice of tools to create and manage Python virtual environments is dependent on situation, preference, and use case.  

| Tool/App | Use Case |
------------ | ------------
| [venv](https://docs.python.org/3/library/venv.html) | Implementation of the virtualenv as a Python module included in the Python install since v.3.3.  This is the "goto" tool of choice. |
| [virtualenv](https://virtualenv.pypa.io/en/latest/index.html) | Includes features not included in venv (see the [comparison](https://virtualenv.pypa.io/en/latest/index.html)). |  
| [Anaconda](https://www.anaconda.com/)  | A heavyweight package and virtual environment manager.  It acts as an "all in one" for Python application versions, package management, virtual environments, additional programming languages such as R and Julia and tools such as visualizers and IDEs. The full fledged install can overtax some systems and performance can suffer an overly ambitious installation configuration. A personal license for individuals is free for non-commercial use.  Use by for-profit or governmental organizations with more than 200 people requires licensing. |
| [miniconda](https://docs.conda.io/en/latest/miniconda.html) | A slimmed down version of Anaconda focussed on virtual environment and package management, includes only conda and Python, not open source, but free. |
| [conda](https://docs.conda.io/en/latest/) | The open source package manager utilized by Anaconda and miniconda. |
| [pip](https://pip.pypa.io/en/stable/) | Included in Python 3.4 and later, this tool does not manage the virtual environment but does handle package management for both venv and virtualenv. Not all python tools have been integrated into the Anaconda repositories or packages for install.  Some, such as mkdocs, must still be installed via pip even when using Anaconda3 or miniconda.  

??? tip "'virtualenv venv' vs. 'venv virtualenv'"
    Avoid the confusion of the typical example given in the documentation of __virtualenv__ which uses the command executed as "virtualenv venv." This calls __virtualenv__ to create a virtual environment named __venv__.  

    Compare with "venv virtualenv" which calls __venv__ to create a virtual environment called __virtualenv__.  For most practical purposes when using Python 3.6 or greater it doesn't matter whether __venv__ or __virtualenv__ is used to create the virtual instance.

    But don't use "virtualenv venv."  That's just obnoxious.


??? note "Other Python Tools"
    Other tools such as [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), [pipenv](https://pipenv.pypa.io/en/latest/), [pew](https://github.com/berdario/pew), [tox](https://tox.wiki/en/latest/) and [nox](https://nox.thea.codes/en/stable/) may be useful but are not currently utilized in this project.  [Pyenv](https://github.com/pyenv) was deprecated in Python 3.5 and not utilized.



<!-- ## Docker and flask

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
 -->



<div style="font-size: 12px;
            padding: 15px;
            border: 2px solid lightgray;
            margin-top: 100px;
            margin-left: 0px;
            margin-bottom: 40px;
            margin-right: auto;
            width: 100%;
            border-radius: 10px;">
  <h4 style="font-size: 14px;
            padding: 0px;
            margin: 0px;">No Representations or Warranties</h5>
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
</div>
