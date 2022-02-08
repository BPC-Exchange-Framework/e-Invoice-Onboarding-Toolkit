___Install Python. Use a minimum of Python 3.6.  Recommended Python 3.10.___

## Create a Python viritual environment.  

  The benefits of creating and running the code in a Python virtual software development environment can't be overstated.

  Use the Python virtualization tool of your choice. Developers on the project have used conda, venv, virtualenv and pipenv.

* Create your virtual environment:

  Use pip for module and package management

* Update pip in your non-virtual python installation:

  ```python -m pip install --upgrade pip```

  (If you are using a Mac or a system where the Python 3 install is not directly alias'ed or on path, substitute whatever is needed to call Python.)

* Execute "pip list" to see what's installed in the base Python installation.

  ```pip list```

  There shouldn't be more than two or three packages.

* Run the command to create your virtual environment.  In this case the virtualization is created using **venv**.


  ```python -m venv .discovery```

* Source the script file to activate the virtual environment

  ```source ./.discovery/bin/activate```

  This will place the virtual environment name at the beginning of the console prompt.

  From here you are running in the virtual environment. Any modifications made to the environment should be isolated to your virtual Python instance. You can work on code located anywhere on your filesystem after activating the virtual environment.  

  When done working in the virtual environment, enter the following command to exit it.

  ```deactivate```

## Get the code

  Viewers of this page are presumed to be able to access github.

  It is entirely possible to pull the code from github anonymously using a link from within the repo to do so.

  If you want to do more than anonymously pull code and contribute:

  1. Create a github account.

  2. install the github cli or the github desktop application

  3. Configure your personal profile and ssh keys to securely submit code to the repository.


* Pull the code from github.

  * Look for the green "Code" button which will provide links to clone the code using https, ssh, the git desktop, or a zip file.

  * This going to pull the repo at the root ./e-invoice-Onboarding-Toolkit.

  * Open the folder as a project within your IDE or editor of choice.



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
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
  </div>
