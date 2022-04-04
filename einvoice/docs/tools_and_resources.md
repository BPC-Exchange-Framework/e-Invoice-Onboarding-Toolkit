# Tools and Resources

__GOAL:__ Create, test, deploy, and maintain code to the highest professional standards.

__HOW:__ Tools and best practices which facilitate development of high quality code with testable and reproducible outcomes.

### Quick Guide

| Tool | Minimal requirements |
| --- | --- |
| Programming Language | Python 3.6 or above. |
| Computer | Supports running Python 3.6 or above. |
| OS  | Mac, Windows, or Windows w/WSL2. |
| Documents and resources. | GitHub and [BPC-Technical-Workgroup-Folder - Google Drive](https://na01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F15aJogTieUuqukjDHm5AVQVVm-PVukPs9&data=04%7C01%7C%7C0ce76ff21ff048af0c2b08d8ef9790ff%7C84df9e7fe9f640afb435aaaaaaaaaaaa%7C1%7C0%7C637522781535891404%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=l1%2BAoHrIHr8przKXkn6pSCQTGnGXKMcOjQnzY0jpqws%3D&reserved=0) |

### Programming Languages

The primary programming language for the project is Python.  Knowledge of other enabling technologies, specifically shell scripting (e.g., ZSH, BASH, or PowerShell) and CommonMark or GitHub Flavored Markdown may be helpful.

All effort will be made to remain within the [Python Standard Library](https://docs.python.org/3.10/library/index.html). Other publicly hosted packages with an open source license may be implemented.

#### Version of Python

*Select a minimum version of Python 3.6. This will include newer features such as f-string.* **Python 3.10 is recommended.**

### Operating System

OS | Considerations  
----------- | -----------  
 Mac OS | Included system version of Python 2.x must be respected.  Make sure to use Python virtual environments. 
 Windows | Latest version of Python are now available on the Windows Store.  Anaconda3 is an especially good option in this OS.  
 Windows w/WSL2 |  WSL2 allows implementation of native Ubuntu on Windows for a linux based Python install while using Windows tools. Integration of virtual environments and Python executable with an IDE like VS Code can be finicky.  
 Linux | Native support for distributed technologies, i.e., Kubernetes and Docker.    
 Chrome OS | Limited on-device resources but a growing number of online and cloud development options, e.g., AWS, Azure, OpenShift, JupyterLab and Notebooks.  
 Raspberry PI | With native Python support, Linux packages, and cloud options there is no reason dev is not an option.  


#### Additional Configuration and Environment Considerations

Future looking consideration for implementation of additional Python enabling technology in support of scalability, portability, and resiliency includes:

##### Frameworks:

* Django
* Flask
* FastAPI
* OpenAPI  

##### Containerization and Cloud Services:

* Docker




Cloud services such as:

* Amazon Web Services (AWS) including lambdas and Route53 DNS
* Microsoft Azure
* RedHat OpenShift


Additional infrastructure components may be implemented by the Project for testing or prototyping utilization of cloud services.

Local testing of Docker containerization may be done on a desktop.  Choice of a cloud infrastructure provider to host and mange Docker containers is at the discretion of the application implementer.

#### Python Programming Methodologies, Standards, and Tools:

Python Coding Standards:

* [PEP20](https://pep20.org) - The Zen of Python
* [PEP8](https://pep8.org) -  The Style Guide for Python Code
* [Guiding Design Principles](https://nsls-ii.github.io/scientific-python-cookiecutter/guiding-design-principles.html) from the [Scientific Python Cookiecutter](https://nsls-ii.github.io/scientific-python-cookiecutter/index.html).
* [Python Doc](https://www.python.org/doc/) the official Python web site page of references to more documentation.
* _See the list of books below for additional guidance on standards and best practices in Python development_.

Tools in bold are used to validate code against PEP8 and PEP20 standards and must complete successfully in order to do a pull into GitHub,  __bold__) .

* __flake8__
* autopep8
* __pylint__
* __pytest__
* unittest
* bandit
* __mypy__
* __pycodestyle__
* __pydocstyle__



#### Development methodologies  
* Documentation and use of __docstrings__
    * [PEP257](https://peps.python.org/pep-0257/)
    * [Google/numpy style docstings as documented in the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).  This document is also provides additional best practices for professional Python devleopers.  
* Domain Driven Design.  See the list of books below for original and supplemental sources material by Eric Evans and Vaughn Vernon.
* Test Driven Development.  See the list of books below for original source material by Harry J.W. Percival. 
* Agile principles applied appropriate to the the size and state of the project.

#### Books

There are many great reference materials in print and on the Internet about Python development.

Below are references that may be helpful. 

* <ins>The Hitchhiker's Guide to Python</ins> by Kenneth Reitz and Tanya Schlusser.  Online for free at [docs.python-guide.org](https://docs.python-guide.org/).  
* <ins>Serious Python</ins> by Julien Danjou
* <ins>Domain-Driven Design Distilled</ins> by Vaughn Vernon
* <ins>Domain Driven Design: Tackling Complexity in the Heart of Software</ins> by Eric Evans
* <ins>Test Driven Development with Python: Obey the Testing Goat, etc.</ins> by Harry J.W. Percival. Also [available online for free](https://www.obeythetestinggoat.com/).
* <ins>Architecture Patterns with Python</ins> by Harry J.W. Percival and Bob Gregory
* <ins>Pro Git</ins> by Scott Chacon and Ben Straub. [Available as a free download](https://git-scm.com/book/en/v2) under an open source license.



<br/>
<br/>
<br/>