# Integrating Code Modules<hr/>

## The Package Structure and Using the Modules

How the package is organized.  

The top level of the packages is named "einvoice."  It is the parent to all other packages and modules.  

| Directory Structure | dot Notation |
------------ | ------------
| ./einvoice | einvoice |



There are two sub-packages called discovery and delivery. A directory named "test" contains unit tests for both delivery and discovery.  A third directory named "docs" is also at this level and contains project documentation.  

| Directory Structure | dot Notation |
------------ | ------------
| ./einvoice | einvoice |
| ./einvoice/discovery | einvoice.discovery |
| ./einvoice/delivery | einvoice.delivery |
| ./einvoice/test | einvoice.test | 
| ./einvoice/docs | NA - does not contain code artifacts |


Third level directory contains the Python modules containing actual application code.  Within the discovery directory there is a "conf" directory intended for application configuration work, a "data" directory for files and applications to generate test data and scenarios.   

| Directory Structure | dot Notation |
------------ | ------------
| ./einvoice | einvoice |
| ./einvoice/discovery | einvoice.discovery |
| ./einvoice/delivery | einvoice.delivery |
| ./einvoice/test| einvoice.test |
| ./einvoice/tests/test_app_logging.py | einvoice.discovery.tests.test_app_logging.test_log_creation |
| ./einvoice/docs | NA - does not contain code artifacts |
| ./einvoice/discovery/conf | einvoice.discovery.conf |
| ./einvoice/discovery/data | einvoice.discovery.data |
| ./einvoice/discovery/accessor.py, app_handler.py, app_logging.py, create_tracking_id.py, dns_query.py, einvoice_message_package.py, line_item.py, party_address.py, semantic_model.py, smp_query.py, urn_hasher.py, urn.py| einvoice.discovery.accessor.Accessor, einvoice.discovery.app_logging.create_logger, etc. |
|./einvoice/delivery/import_xsd | einvoice.delivery.import_xsd.ImportXSD |

Fourth level directories are the deepest in the application and contain code in the conf and data directories.  

| Directory Structure | dot Notation |
------------ | ------------
| ./einvoice | einvoice |
| ./einvoice/discovery | einvoice.discovery |
| ./einvoice/delivery | einvoice.delivery |
| ./einvoice/test| einvoice.test |  
| ./einvoice/docs | NA - does not contain code artifacts |
| ./einvoice/discovery/conf | einvoice.discovery.conf |
| ./einvoice/discovery/data | einvoice.discovery.data |
| ./einvoice/discovery/accessor.py, app_handler.py, app_logging.py, create_tracking_id.py, dns_query.py, einvoice_message_package.py, line_item.py, party_address.py, semantic_model.py, smp_query.py, urn_hasher.py, URN.py| einvoice.discovery.accessor.Accessor, einvoice.discovery.app_logging.create_logger, etc. |
|./einvoice/delivery/import_xsd.py 
 | einvoice.delivery.import_xsd.ImportXSD |
| ./einvoice/discovery/conf/config_tool.py, smp_config.py | einvoice.discovery.conf.config_tool.EInvoiceConfig, etc. |
| ./einvoice/discovery/data/create_sample_data.py | einvoice.discovery.data.create_sample_data.CreateSampleData |


## Additional Files
Additional files included in the project which are important.     

| File | Purpose |
------------ | ------------
| ./einvoice/delivery/app.log | Application log created by app_logging.py for delivery sub-package. |
| ./einvoice/delivery/web_response.log | Response logging to feed into a webservice for delivery sub-package. |
| ./einvoice/discovery/app.log | Application log created by app_logging.py for discovery sub-package. |
| ./einvoice/discovery/web_response.log | Response logging to feed into a webservice for discovery sub-package. |
| ./einvoice/docs | Markdown files compiled into the project documentation. |
| ./einvoice/docs/jupyterlab | Stored JupyterLab sandboxes which may be shared via Google Colab or downloaded and run on a Jupyter service instance. |
| ./einvoice/docs/pdf| Stored PDF files (entity diagrams) which may be included in the documentation.  |
| ./einvoice/docs/drawio | Stored PDF files (vector graphic diagrams) which may be included in the documentation.  |
|./einvoice/discovery/data/item_list.csv, per_item_list.csv| CSV files which contain same data values to populate an einvoice.
| ./einvoice/tests/ *.sh | An assortment of shell scripts to run various linters on the modules.  Includes pylint, mypy, flake8, pycodestyle, pydocstyle, and combinations.|
|.einvoice/.env .env.example.dev | Configuration files which contain example values for testing purposes. |
| ebms-header-3_20220119.xsd, sample_msg.xml | XSD containing schema definition for ebMS header and a sample message to test against.|



## Note on classes with modules.
???+ info "All module code is in classes and methods."
    All code in the discovery and delivery sub-packages is encapsulated in a class and a method within a class.  There are no excutable functions outside of a class.

    _There is no entry point to execute this code and instantiate any of the classes or methods at the command line at this time._

    Examples of implementing and executing the code can be found in the [test cases](./test_cases.md), [Discovery Validation](./discovery_validation.md), or the [JupyterLab/Notebooks](./google_colab_pages.md).

    Test cases are not encapsulated in classes or methods but are instead named functions.


The code is as Pythonic as possible in naming files for exactly what they do.  The functionality can be broken down as:

* Dataclasses - modules which define some of the key entities at use in the project.
    * urn.py - Dataclass definition of an urn object.
    * semantic_model.py - Dataclass for the semantic model (the einvoice itself).
    * party_addresss.py - Dataclass for a party entity within the Four-Corner model.
    * line_item.py - Dataclass for a line item on the semantic model (einvoice).
    * einvoice_message_package.py - Dataclass to contain all the information to be transmitted, i.e., the payload, in the einvoice message.

* Specific workflow actions - modules which execute specific tasks within the process workflow.
    * urn_hasher.py - takes the inputs of the party_id, specification, and schema_id and creates the NAPTR look-up uri.
    * dns_query.py - take the NAPTR look-up uri and execute it against DNS. The output is the SMP uri and the existing URN is passed forward as well.  
    * smp_query.py - receives the SMP uri and URN and creates two REST API calls to the endpoint based on the inputs.  Executes the webservice calls and receives a response.  Parses the response and returns it as a string containing the URI of corner 3 in the model.  
    * import_xsd.py - takes as an input an XML file and checks its validity against an XSD.  In this case it is the XML of an ebMS message header checked against an AS4 conformance profile.

 * Other "helper" modules -
    * accessor.py - module to run the Delivery Validation process, executed via test scripts.
    * create_sample_data.py - construct sample data entities to use in testing the semantic model.
    * create_tracking_id.py - create an arbitrary id with a given configuration to use to track the message through the process.  Could be used in lieu of a UUID.
    * app_handler.py - module closest to being an executable form the command line.  A prototyye module to run the delivery validation directly, if all required configuration is complete.  
    * app_logger.py - a custom logging implemenation to be used by all the other modules, including test modules, to standardize output and aggregate to single stream each for app logging, to system out, and response to a webservice.



  <br/>
<br/>
<br/>
