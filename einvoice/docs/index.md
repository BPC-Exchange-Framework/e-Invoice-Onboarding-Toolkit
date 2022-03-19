# Project Home

## Welcome
__Welcome to the E-Invoice Onboarding Toolkit__  

This is a repository for open source software tools created to facilitate market adoption of e-invoices implemented conformant with the Four-Corner Model of an Exchange Framework.   

## Project Goals
???+ Alert "GOALS: The features of the project as oultined in the [project roadmap](./project_roadmap.md). "
    Roadmap Feature | Feature Phase | Purpose of Feature  
    ------ | ------ | ------
    Feature #1 - SML NAPTR DNS Lookup | Discovery |  1.  Create an ID code based on the Buyer's party ID  <br/> 2. Look the ID code up in a globabl internet datatbase to get the address of a website which has more informaiton about the Buyer.
    Feature #2 - SMP REST API Query | Discovery |  3. Contact the website  from the previous step to make sure the Buyer can in fact handle receiving an e-invoice and where to send it. |
    Feature #3 - AS4 Message Exchange  | Delivery |  4. Validate that an e-mail message sent to the Buyer is in the correct format.  

## Project Outcomes

???+ Important "OUTCOMES: How the features are implemented."  
    Outcome | Feature | Phase  
    ------ | ------ | ------
    1. Hashing functionality to derive the URN for look-up in a DNS NAPTR record.  | Feature #1 | Discovery
    2. Execute DNS NATPR lookup and extract the relevant SMP URI.  | Feature #1 | Discovery
    3. Two REST requests to an SMP server using a SOAP API to retrieve a Corner 3 URI. | Feature #1 | Discovery
    4. Execute the wbe service requests to the SMP server. | Feature #2 | Discovery
    5. Extract the Corner 3 endpoint URI from the response from the SMP server.      | Feature #2 | Discovery
    6. Validate an E-Invoice ebMS message header for compliance with an AS4 conformance profile. | Feature #3| Delivery

For information about E-Invoices and implementing the Four-Corner Model please visit the [Business Payments Coalition website](https://businesspaymentscoalition.org/electronic-invoices).  

 Additional documentation, reference materials, and standards can be found on the [Oasis-Open.org website](https://www.oasis-open.org). Start with the [ebXML specification](http://docs.oasis-open.org/ebxml-msg/ebms/v3.0/core/os/ebms_core-3.0-spec-os.html)

## Site Map

* [Project Home](./index.md)
* [FAQ](./faq.md)
* [Outcomes](./outcomes.md)
* [Assumptions](./assumptions.md)
* [Tools and Resources](./tools_and_resources.md)
* [Configure a Python Environment](./python_dev_env.md)
* [Package Requirements](./requirements.md)
* [Getting the Code](./working_with_the_code.md)
* Using the Code
    * [Using the Modules](./using_the_modules)
    * [Test Cases](./test_cases.md)
    * [Discovery Validation](./discovery_validation.md)
    * [JupyterLab/Notebooks](./google_colab_pages.md)
* [Infrastructure Components](infrastructure_components.md)
* [Project Roadmap](./project_roadmap.md )
* [Project Artifacts](./artifacts.md)
* [Workflow](./git_workflow.md)
* [Oasis Resources](./oasis_documentation.md)
* [License](./_license.md)

