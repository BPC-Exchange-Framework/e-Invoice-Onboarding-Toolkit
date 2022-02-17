# Project Outcomes:<hr>

## Functionality

1. Hashing functionality to derive the urn for look-up in a DNS NAPTR record.  
2. DNS NATPR lookup and extract the relevant SMP URI.  
3. Two REST requests to an SMP server to retrieve a Corner 3 URI.  
4. Execute the REST requests to the SMP server.  
5. Extract the Corner 3 endpoint URI from the response from the SMP server.    
6. Validate an e-Invoice ebXML message header for compliance with an AS4 conformance profile.  
<br/>

<hr style="height: 2px;border:none;color:#333;background-color:#333;">


## Implementation

1.	Functional  Python code:
     
     - [x] Construct the URN from the specification, schema ID, and party ID,
         - [x]  urn_hasher.py
     - [x] Hash the URN per the requirements to create a NAPTR record for a DNS look-up to obtain SMP service URI.
         - [x]  urn_hasher.py
         - [x] accessor.py
     - [x] Do the DNS look-up to obtain the SMP service URI.
         - [x] accessor.py
         -  [x] dns_query.py
     - [x] Query the SMP URI using the ebXML spec.
         - [x] accessor.py
         - [x] smp_query.py
    - [x] Dataclass object comprised of specification, schema ID, party ID, and a sample JSON e-Invoice payload.
         - [x] einvoice_message_package.py
         -  [x] line_item_py
         - [x] party_address.py
         - [x] semnantic_model.py
         -  [x] urn.py
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
        - [x] Review of AS4 XSD spec Lab Notebook
       - [x] Validation of ebMS sample message header against AS4 XSD Lab Notebook
    - [x] <s>Implementation Guide </s> Documentation site written by SEs and prepared with BSAs to facilitate utilization of the code and work product to be delivered <s>via readthedocs.org site</s> though the github repository.
    - [x] <s>readthedocs.org site registration/creation</s> Create document set using __mkdocs-material__  hosted on github repository.
    - [x] Create <s>list of assumptions</s> __FAQ__ and __Outcomes__ pages for starting point/baseline documentation.
    - [x] Aggregation of above referenced artifacts hosted on github.  
<br/>
 
<hr style="height: 2px;border:none;color:#333;background-color:#333;">

## To do

1.	A deployment package which includes Python code to:
    - [ ] \(In-progress\)_ Creation of "final" Python package which delivers code artifacts as a library.

3.	Documentation
    - [ ] \(In-progress\) Generated from python docstring using <s>Sphinx</s> __mkdocs-material__ framework
    - [ ] \(In-progress\) Documentation of supporting infrastructure including DNS and SMP provisioning specifically called out as a parallel value-add result of the project.  
<br/>

<hr style="height: 2px;border:none;color:#333;background-color:#333;">
<br/>
## Notes  

- [x] Test-driven development methodology is being implemented to include test cases for code as it is being developed and delivered.  
- [x] CI/CD process implemented via Github workflow has been validated to ensure PEP8 code standards and checks using Flake8, pylint, and pytest are valid.  All changes and updates to code must pass CI/CD before it's merged into the repo.   


<br/><br/>
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
