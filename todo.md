# e-Invoice Open Source Toolkit Project 
## List of Deliverables

1.	A deployment package which includes:

Python code to:
- [x] Create dataclass object comprised of specification, schema ID, party ID, and a sample JSON e-Invoice payload. 
- [x] Construct the URN from the specification, schema ID, and party ID,
- [x] Hash the URN per the requirements to create a NAPTR record for a DNS look-up to obtain SMP service URI.
- [x] Do the DNS look-up to obtain the SMP service URI.
- [ ] [In-progress] Query the SMP URI using the ebXML spec.
- [x] Test cases implemented using Test Driven Development
- [x] Create a sample e-Invoice dataclass.
- [x] Logging implemented through custom logging using standard Python modules.
- [ ] [In-progress] Containerized web API/UI to implement the code/functionality above.
    - [ ] Provided as a Docker image.
- [ ] [In-progress] Creation of "final" Python package which delivers code artifacts as a library.

2. Documentation and code artifacts for Infrastructure components:
- [x] Demonstrating implementation of DNS infrastructure using Amazon Route53 and code to provision, update, and delete NATPR records, acting as the SML.
- [ ] [In-progress] Demonstrating implementation of SMP infrastructure to reply to the REST API for service functionally and AS4 final endpoint.    

3.	Documentation 
- [ ] [In-progress] Generated from FastAPI or Flask
- [ ] [In-progress] Generated from python docstring using Sphinx
- [ ] Previously created documentation and diagrams which were outcomes of analysis and process review.  
- [ ] Jupyter Lab Notebooks running on Google Colab for real-time examples of a dev sandbox.  
    - [x] Hash URN Notebook
    - [x] SML query Notebook
    - [ ] SMP query Notebook
- [ ] Implementation Guide written by SEs and prepared with BSAs to facilitate utilization of the code and work product to be delivered via readthedocs.org site.
    - [x] ~~readthedocs.org site registration/creation~~
    - [ ] [In-progress] Create list of assumptions for starting point/baseline.
    - [ ] Aggregation of above referenced artifacts.
    - [ ] Documentation of supporting infrastructure inc;luding DNS and SMP provisioning specifically called out as a parallel value-add result of the project.

Notes:
* Test drive development methodology is being implemented to include test cases for code as it is being developed and delivered.  
* CI/CD process implemented via Github workflow has been validated to ensure PEP8 code standards and checks using Flake8, pylint, and pytest are valid.
* Cerfitificate work has been determined to be out of scope at this time and will be removed from the e-Invoice Onboarding Toolkit repository.  [@mnkellyk](@mnkellyk) will host this content under their personal repo available pursuant to a GPL3 license for use by anyone who may have an interest or benefit from it.    

