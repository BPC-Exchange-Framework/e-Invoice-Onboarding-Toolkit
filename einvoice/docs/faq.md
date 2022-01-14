### Sometimes asked questions...
<hr>
#### Q: Who is the audience for this project?    

A: Developers immplementing e-invoice functionality of a 4-Corners model.   
<hr>
#### Q: What do I need in order to use this code?  

A: Python
1. Some knowledge of Python  
2. Python 3.6 or greater  
<hr>
#### Q: Does this code provide a full end-to-end solution to process an e-invoice?  

A:  This code answers some very domain specific questions regarding e-invoice funtionality in the 4-Coners framework.  Specifically it's helpful with:  
1. The hashing functionality to derive a urn for look-up in a DNS NAPTR record.  
2. How to do the DNS NATPR lookup and extract the relevant SMP URI.  
3. How to construct the two REST requests to an SMP server to retreive a Corner 3 URI.  
4. How to execute the REST requests to the SMP server.  
5. How to extract the Corner 3 endpoint URI from the response from the SMP server.    
6. Validating an ebxr AS4 message header for compliance with latet OASIS specifications (forthcoming)  
<hr>
#### Q: How do I use the code?  

A: There are a number of ways the code can be examined or worked with:  
1. [Start to finish exmaple of the  URI discovery process](./start_to_finish.md).  
2. [Test Cases](./test_cases.md) which demonstrate functionality of the modules.  
3. Jupyter Noteboos sandbox environments at [Google Colab Pages](./google_colab_pages.md) which isolate and demonstrate the code in a sandbox.  
4. Package/Library API see the [Index](./index.md) for links to the code API on the modules themselves.  
5. Integration of an example discovery process implemented in a [Flask application on a Docker container](./flask_integration_on_docker.md) (forthcoming).  