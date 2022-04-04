# Additional Infrastructure Build-out

The code is intended to interact with other participants in the Four-Corner Model,  including Access Providers, DNS servers and SMP service providers.

## SML

__Q:__    

How do you test the toolkit?  How do you create a NAPTR  DNS record entry on a domain? 

__A:__

In order to do the SML look-up, the appropriate NAPTR records must be in place.  The assumption is that a NAPTR DNS record exists as a key:value pair.  A look-up of the "key" in the DNS of the NAPTR record will return the "value."  The "key" is the hashed value of the urn.  The value being sought and returned is the URI of the SMP for the next step in the Model.

Access Point 1 in Corner 2 may be acting in the role of the SML and handling tasks associated with it.  Theses task could include:   
  
  * Constructing the URN  
  * Creaitng the hash value of the URN  
  * Queryhing the DNS NATPR record URN
  * Returning the SMP URI  

The Python modules provide examples of some ways  the tasks of SML could be accomplished, either as, or by, an Access Point or an organization on its own behalf.    

For testing purposes there is an application to update a DNS entry with a NAPTR record key:value pair of URN:SMP URI repsonse.  The applicatiion updates a the DNS via Amazon Web Services Route53 using the test domain of sc-b2b.us.   This allows for the registration of URN hashes in the DNS domain of sc-b2b.us.  These entries are live in the DNS and accessible worldwide.  
 
The REST API is available at [https://sml-api.sc-b2b.us/docs](https://sml-api.sc-b2b.us/docs) to register SML entries, which are the DNS NATPR records on the sc-b2b.us domain.  This process creates the URN hash based in inputs provided by the user.  Organizations wishing to register a test URN to use for validation can open an issue in the project for assistance in using the web interface.  

Once these SML/DNS NATPR entries are created, they can queried using the toolkit to make public queries to DNS NAPTR look-up as soon as propated through the DNS.

The code implemented to create the NAPTR DNS record on AWS Route53 is available in the GitHub repository:  [BPC-OpenSourceTools/sml-service-r53](https://github.com/BPC-OpenSourceTools/sml-service-r53).  
  
## SMP
  
There is an application to test the SMP REST API service calls on the same domain as the SML at  [https://smp-api.sc-b2b.us/docs](https://smp-api.sc-b2b.us/docs) .  This is a REST API to make web service calls to test the toolkit.  

The SMP s a web service queried by a SOAP API call to return the Corner 3 URI or terminal endpoint.  The specification for the actual API can be found in the document: [Service Metadata Publishing (SMP) Version 2.0](http://docs.oasis-open.org/bdxr/bdx-smp/v2.0/bdx-smp-v2.0.html) dated 14 February 2021 as an Oasis standard.   

__Section 5.4 Resources__  


| Resource  | URI | Method  | XML resource root element | HTTP Status | Description of returned content |    
| ------ | ------ | ------ | ------ | ------ | ------ | 
| ServiceGroup | ./bdxr-smp-2/[{identifier scheme}::]{participant id} See section 3.6 for {participant id} format | GET | <ServiceGroup\> |  200; 500; 404 | Holds the Participant Identifier of the recipient, and a list of references to individual ServiceMetadata resources that are associated with that participant identifier.  |   
| ServiceMetadata | ./bdxr-smp-2/[{identifier scheme}::]{participant id}/services/{service ID} See section 3.7 for {service ID} format | GET |  <ServiceMetadata\>  | 200; 500; 404 | Holds all of the metadata about a Service, or a redirection URL to another Service Metadata Publisher holding this information. |

The SMP service registers a URN for query.  Note that the API specification is essentially the URN with modifications to include some additional service capability codes but mostly to accomodate characters that would otherwise be illegal in a URL.  

After registering a URN(s) on the SML service, go to the SMP service at [https://sml-api.sc-b2b.us/docs](https://sml-api.sc-b2b.us/docs) to register the urn there in order to get a reponse for testing SMP query functionality.

The code implemented to create the NAPTR DNS record on AWS Route53 is available in the GitHub repository:  [BPC-OpenSourceTools/smp-service](https://github.com/BPC-OpenSourceTools/smp-service).




<br/>
<br/>
<br/>
