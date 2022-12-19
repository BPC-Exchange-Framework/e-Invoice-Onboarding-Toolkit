# E-Invoice Onboarding Tool-kit
This is a repository for open source tools created to facilitate adoption and implementation of a 4-Corners interoperability framework.     


To begin, please navigate to the [Github pages documentation](https://bpc-exchange-framework.github.io/e-Invoice-Onboarding-Toolkit) for the project.  

## Release Notes 1.0 

1. Remove extraneous artifacts through-out.

1. .gitignore file updated to suppress additional unnecessary artifacts.

1. Implement package-level config.py.  Makes app_logger.py available at the package level without importing from ./discovery into ./delivery.

1. Refactor accessor.py to framework_model.py

1. New module capture_dns_response.py created to enable additional validation of DNS fields from the DNS NAPTR query.  Logging of response from DNS NAPTR query to a file.  The response from the call to the DNS NAPTR query now returns a dictionary of all the fields returned from the DNS for post-processing.  

1. Test case captures validation of DNS NAPTR query.

1. Additional documentation including walk-through of the URN hash construction, how to execute and process the DNS NAPTR query, and breaking out how to construct the SMP Service Group and Service REST API queries and handle their respective response.

1. Refactor app_logging.py module to enable a YAML based dictionary configuration, includes an example of a log rotator, and better emitting to root logger, stdout, and stderr for containerization.  

1. Additional examples and updates in a number of additional JupyterLab notebooks.    
* dns_query.ipynb  
* urn_hash_work.ipynb





