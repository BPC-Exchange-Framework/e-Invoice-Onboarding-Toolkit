# To do:<hr>


## List of Deliverables

1.	A deployment package which includes Python code to:
     - [x] Create dataclass object comprised of specification, schema ID, party ID, and a sample JSON e-Invoice payload.
     - [x] Construct the URN from the specification, schema ID, and party ID,
     - [x] Hash the URN per the requirements to create a NAPTR record for a DNS look-up to obtain SMP service URI.
     - [x] Do the DNS look-up to obtain the SMP service URI.
     - [x] Query the SMP URI using the ebXML spec.
     - [x] Test cases implemented using Test Driven Development
    - [x] Create a sample e-Invoice dataclass.
    - [x] Logging implemented through custom logging using standard Python modules.
    - [ ] \(In-progress\) Containerized web API/UI to implement the code/functionality above.
    - [ ] Provided as a Docker image.
    - [ ] \(In-progress\)_ Creation of "final" Python package which delivers code artifacts as a library.

2. Documentation and code artifacts for Infrastructure components:
    - [x] Demonstrating implementation of DNS infrastructure using Amazon Route53 and code to provision, update, and delete NATPR records, acting as the SML.
    - [x] Demonstrating implementation of SMP infrastructure to reply to the REST API for service functionally and AS4 final endpoint.    

3.	Documentation
    - [ ] \(In-progress\) Generated from FastAPI or Flask
    - [ ] \(In-progress\) Generated from python docstring using Sphinx
    - [x] Previously created documentation and diagrams which were outcomes of analysis and process review.  
    - [x] Jupyter Lab Notebooks running on Google Colab for real-time examples of a dev sandbox.  
    - [x] Hash URN Notebook   (Hash URN and SML query are in the same Notebook)
    - [x] SML query Notebook  (Hash URN and SML query are in the same Notebook)
    - [x] SMP query Notebook
    - [ ] Implementation Guide written by SEs and prepared with BSAs to facilitate utilization of the code and work product to be delivered via readthedocs.org site.
    - [x] ~~readthedocs.org site registration/creation~~
    - [ ] \(In-progress\) Create list of assumptions for starting point/baseline.
    - [ ] Aggregation of above referenced artifacts.
    - [ ] Documentation of supporting infrastructure including DNS and SMP provisioning specifically called out as a parallel value-add result of the project.
<br/>
<br/>
<br/>
<hr style="height: 2px;border:none;color:#333;background-color:#333;">

- __Notes__:  
    - [x] Test drive development methodology is being implemented to include test cases for code as it is being developed and delivered.  
    - [x] CI/CD process implemented via Github workflow has been validated to ensure PEP8 code standards and checks using Flake8, pylint, and pytest are valid.  All changes and updates to code must pass CI/CD before it's merged into the repo.  
    - [x] Certificate work has been determined to be out of scope at this time and has been removed from the e-Invoice Onboarding Toolkit repository.  [@mnkellyk](@mnkellyk) will host this content under their personal repo available pursuant to a GPL3 license for use by anyone who may have an interest or benefit from it.    




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
