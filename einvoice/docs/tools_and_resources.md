# Tools and Resources

__GOAL:__ Create, test, deploy, and maintain code to the highest professional standards.

__HOW:__ Tools and best practices which facilitate development of high quality code with testable and reproducible outcomes.

### Quick Guide

| Tool | Minimal requirementsß |
| --- | --- |
| Programming Language | Python 3.6 or above. |
| Computer | Supports running Python 3.6 or above. |
| OS  | Mac, Windows, or Windows w/WSL2. |
| Documents and resources. | GitHub and [BPC-Technical-Workgroup-Folder - Google Drive](https://na01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F15aJogTieUuqukjDHm5AVQVVm-PVukPs9&data=04%7C01%7C%7C0ce76ff21ff048af0c2b08d8ef9790ff%7C84df9e7fe9f640afb435aaaaaaaaaaaa%7C1%7C0%7C637522781535891404%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=l1%2BAoHrIHr8przKXkn6pSCQTGnGXKMcOjQnzY0jpqws%3D&reserved=0) |

### Programming Languages

The primary programming language for the project is Python.  Knowledge of other enabling technologies, specifically shell scripting (e.g., ZSH, BASH, or PowerShell) and CommonMark or GitHub Flavored Markdown may be helpful.

All effort will be made to remain within the [Python Standard Library](https://docs.python.org/3.10/library/index.html). Other publicly hosted packages with an open source license may be implemented.

#### Version of Python

*Select a minimum version of Python 3.6. This will include newer features such as f-string.* ***Python 3.10 is recommended.***

### Computer Spec

!!! Warning "You will need a computer which is able to download and run Python 3.6."

### Operating System

OS | Considerations  
----------- | -----------  
 Mac OS | Included system version of Python 2.x must be respected.  Make sure to use Python virtual environments. Homebrew package manager is a plus.  
 Windows | Latest version of Python are now available on the Windows Store.  Anaconda3 is an especially good option in this OS.  
 Windows w/WSL2 | Great implementation of Ubuntu on Windows is truly impressive.  Integration of virtual environments and Python executable with an IDE like VS Code can be finicky.  
 Linux | Native support for distributed technologies, i.e., Kubernetes and Docker.    
 Chrome OS | Limited on-device resources but a growing number of online and cloud development options, e.g., AWS, Azure, OpenShift, JupyterLab and Notebooks.  
 Raspberry PI | With native Python support, Linux packages, and cloud options there is no reason dev is not an option.  

These options show that there is nothing proprietary, exclusive, or given preference other than resource availability and personal preference.

#### Additional Configuration and Environment Considerations

Future looking consideration for implementation of additional Python enabling technology in support of scalability, portability, and resiliency includes:

##### Frameworks:

* Django
* Flask
* FastAPI
* OpenAPI  

##### Containerization and Cloud Services:

* Docker

Local testing of Docker containerization may be done on a desktop, however a cloud implementation is the typical endpoint for a container deployment.


Cloud services such as:

* Amazon Web Services (AWS) including lambdas and Route53 DNS
* Microsoft Azure
* RedHat OpenShift


Additional infrastructure components may be implemented by the Project for testing or prototyping utilization of cloud services.

The implementation of a cloud service and choice of provider is entirely the responsibility of the implementer of the code. Code artifacts included here which implement cloud services are examples for research and educational purposes only.  No preference or endorsement is given to any provider.  

#### Python Programming Methodologies, Standards, and Tools:

Some standards:

* [PEP20](https://pep20.org)
* [PEP8](https://pep8.org)
* [Guiding Design Principles](https://nsls-ii.github.io/scientific-python-cookiecutter/guiding-design-principles.html) from the [Scientific Python Cookiecutter](https://nsls-ii.github.io/scientific-python-cookiecutter/index.html).
* [Python Doc](https://www.python.org/doc/) the official Python web site page of references to more documentation.
* _See the list of books below for additional guidance on standards and best practices in Python development_.

Tools to implement the standards(preferred ones in __bold__) .

* __flake8__
* autopep8
* __pylint__
* __pytest__
* unittest
* black (Careful! - Handles most formatting well but line character length may not be handed as desired.)
* bandit
* __mypy__
* __pycodestyle__
* __pydocstyle__



Development methodologies
* Documentation and use of ___docstrings___
* Domain Driven Design
* Test Driven Development
* Agile principles applied appropriate to the the size and state of the project.

#### Books

There are many great reference materials in print and on the Internet about Python development.

The list below contains some of the titles the developers consider the most helpful and authoritative, regardless of level of expertise with Python. (Titles and author only, no affiliate links.)

* <ins>The Hitchhiker's Guide to Python</ins> by Kenneth Reitz and Tanya Schlusser.  On-line for free at [docs.python-guide.org](https://docs.python-guide.org/).  
* <ins>Serious Python</ins> by Julien Danjou
* <ins>Domain-Driven Design Distilled</ins> by Vaughn Vernon
* <ins>Domain Driven Design: Tackling Complexity in the Heart of Software</ins> by Eric Evans
* <ins>Test Driven Development with Python: Obey the Testing Goat, etc.</ins> by Harry J.W. Percival. Also [available online for free](https://www.obeythetestinggoat.com/), which works for a quick reference in a pinch.
* <ins>Architecture Patterns with Python</ins> by Harry J.W. Percival and Bob Gregory
* <ins>Pro Git</ins> by Scott Chacon and Ben Straub. [Available as a free download](https://git-scm.com/book/en/v2) under an open source license.



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
