# E-Invoice Onboarding Tool-kit
## Working with the code
### Test Cases

#### Using an .env file

???+ Warn "Copy the .env.example.dev to .env"
    Some of the test cases rely on local variables imported at runtime.  These values are in the ".env.example.dev" file.  This file is at the ./einvoice root of the project.  The file MUST be copied or renamed to ".env" in order for all of the tests to complete successfully. (The tests may also be refactored manually to refer to local dev enivornment variables.) 


#### Test modules

Every module includes a test module in the ./einvoice/test directory.  

???+ note "Test cases are written as functions, not classes."
    The test cases are written as functions and __CAN__ be directly called from the command line.  


???+ Important "Use Pytest to run the test cases."
    The use case for the test cases include using Pytest.  
     __The Pytest package must be installed in your Python distribution.__

From the a terminal console, change directory into the ./einvoice/test  directory.  

To see the list of available test files, use either the file browser or the command line.
For Windows: 
```
dir .\einvoice\test\
```
For Mac/*nix/WSL2:
```
ls -al ./einvoice/test/ 
```


???+ Important "The ./test directory __must__ be at the same level as the code."
     Out of the box, Pytest requires that without additional configuration it must be executed from  a directory at the same level of the code that's being tested.  That is, test scripts are in ./einvoice/test and code files are in ./einvoice/discovery and ./einvoice/delivery.   

Pytest will automatically look for files formatted as test files, with "test" in the lead of the filename.  To execute an inidividual test the syntax is:
```
pytest test_app_logging.py
```

No test is dependent on any other, and each may be run on its own, or run them all at once, in any order.  


The test will run and either the "assert" statement(s) inside will pass or it will fail.  

__Failures MUST be resolved prior to attempting to check code into GitHub as our baseline CI/CD process checks for these failures before committing and will not continue if any are found.__

The included assert statements currently test a variety of cases up to validation of URN creation, query of the NAPTR DNS record, REST API call to the SMP, and validation of the ebMS header against the AS4 conformance profile.  

The test folder also contains a number of shell scripts to validate the code using  a number of linters including flake8, pylint, mypy, pycodestyte, and pydocstyle.   Prior to check in, all code must have all warnings from all linters resolved or noted.  

<figure markdown>
  ![Successful completion of all tests cases.](./successful_tests.png)
  <figcaption>Successful completion of all test cases.</figcaption>
</figure>


<br/>
<br/>
<br/>