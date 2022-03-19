# Project Outcomes:<hr>

## Functionality
1. Discovery  
    a. Hashing functionality to derive the URN for look-up in a DNS NAPTR record.   
    b.  DNS NATPR lookup and extract the relevant SMP URI.  
    c.  Two REST requests to an SMP server to retrieve a Corner 3 URI.  
    d.  Execute the REST requests to the SMP server.  
     e.  Extract the Corner 3 endpoint URI from the response from the SMP server.    
1. Delivery  
  a.  Validate an e-invoice ebXML message header for compliance with an AS4 conformance profile.  
<br/>

<hr style="height: 2px;border:none;color:#333;background-color:#333;">


## Implementation

1.	Functional  Python code:
     
     - [x] Construct the URN from the specification, schema ID, and party ID,
         - [x]  urn_hasher.py
     - [x] Hash the URN per the requirements to create a NAPTR record for a DNS look-up to obtain SMP service URI.
         - [x]  urn_hasher.py
         - [x] accessor.py
     - [x] Execute DNS look-up to obtain the SMP service URI.
         - [x] accessor.py
         -  [x] dns_query.py
     - [x] Query the SMP URI using the ebXML specifcation.
         - [x] accessor.py
         - [x] smp_query.py
    - [x] Dataclass object comprised of specification, schema ID, party ID, and a sample JSON E-Invoice payload.
         - [x] einvoice_message_package.py
         -  [x] line_item_py
         - [x] party_address.py
         - [x] semnantic_model.py
         -  [x] URN.py
     - [x] Test cases implemented using Test Driven Development
         - [x] test_accessor.py
        - [x] test_app_logging.py
        - [x] test_create_sample_data.py
        - [x] test_create_tracking_id.py
        - [x] test_dns_query.py
        - [x] test_import_xsd.py
        - [x] test_line_item.py
        - [x] test_party_address.py
        - [x] test_semantic_model.py
        - [x] test_smp_query.py
        - [x] test_urn.py
        - [x] test_urn_hasher.py
    - [x] Logging implemented through custom logging using standard Python modules.
        - [x]  app_loggiing.py


2. Documentation and code artifacts for Infrastructure components:
    - [x] Demonstrating implementation of DNS infrastructure using Amazon Route53 and code to provision, update, and delete NATPR records, acting as the SML.
    - [x] Demonstrating implementation of SMP infrastructure to reply to the REST API for service functionally and AS4 final endpoint.    

3.	Documentation
    - [x] Previously created documentation and diagrams which were outcomes of analysis and process review.  
    - [x] Jupyter Lab Notebooks running on Google Colab for real-time examples of a dev sandbox.  
        - [x] Hash URN and SML query Lab Notebook   (Hash URN and SML query are in the same Notebook)
        - [x] SMP query Lab Notebook
        - [x] Review of AS4 XSD specification Lab Notebook
       - [x] Validation of ebMS sample message header against AS4 XSD Lab Notebook
    - [x] <s>Implementation Guide </s> Documentation site written to facilitate utilization of the code and work product to be delivered <s>via readthedocs.org site</s> though the GitHub repository.
    - [x] <s>readthedocs.org site registration/creation</s> Create document set using __mkdocs-material__  hosted on GitHub repository.
    - [x] Create <s>list of assumptions</s> __FAQ__ and __Outcomes__ pages for starting point/baseline documentation.
    - [x] Consolidation of documentation in the GitHub repository.  
<br/>
 
<hr style="height: 2px;border:none;color:#333;background-color:#333;">

## To do

1.	A deployment package which includes Python code to:
    - [ ] \(In-progress\)_ Creation of "final" Python package which delivers code artifacts as a library.

3.	Documentation
    - [ ] \(In-progress\) Generated from python docstring using <s>Sphinx</s> __mkdocs-material__ framework
    - [ ] \(In-progress\) Documentation of supporting infrastructure including DNS and SMP provisioning.  
<br/>

<hr style="height: 2px;border:none;color:#333;background-color:#333;">
<br/>
## Notes  

- [x] Test-driven development methodology is being implemented to include test cases for code as it is being developed and delivered.  
- [x] CI/CD process implemented via GitHub workflow has been validated to ensure PEP8 code standards and checks using flake8, pylint, and pytest are valid.  All changes and updates to code must pass CI/CD before it's merged into the repo.   


<br/>
<br/>
<br/>