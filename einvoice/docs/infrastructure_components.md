# Additional Infrastructure Build-out

The code is intended to interact with other participants in the Four-Corner Model,  including Access Providers, DNS servers and SMP service providers.

## SML

__Q:__    

How do you test the toolkit?  How do you create a NAPTR  DNS record entry on a domain? 

__A:__

In order to do the SML look-up, the appropriate NAPTR records must be in place.  The assumption is that a NAPTR DNS record exists as a key:value pair.  A look-up of the "key" in the DNS of the NAPTR record will return the "value."  The "key" is the hashed value of the urn.  The value being sought and returned is the URI of the SMP for the next step in the Model.

Access Point 1 in Corner 2 may be acting in the role of the SML and handling tasks associated with it.  Theses task could include:
* Creating the URN
* Creaing the hash value of the URN
* Queryhing the DNS NATPR record record
* Returning the SMP URI

The Python modules provide examples of some ways  the tasks of SML could be accomplished, either as, or by, an Access Point or an organization on its own behalf.    

For testing purposes the BPC has is running a DNS server on Amazon Web Services Route53 on the test domain of sc-b2b.us.   This allows for the registration of urn hashes in the DNS domain of sc-b2b.us.  These entiries are live in the DNS accessible worldwide.  
 
A REST API is available at [https://sml-api.sc-b2b.us/docs](https://sml-api.sc-b2b.us/docs) to register SML entries, which are the DNS NATPR records on the sc-b2b.us domain.  This process creates the urn hash based in inputs provided by the user.  Organizations wishing to register a test urn on the BPC test domain can reach  out to the BPC  or @mnkellyk for assistance in using the web interface.  

Once these SML/DNS NATPR entries are created, they can queried using the toolkit to make public queries to DNS NAPTR look-up within a matter of seconds.

The code implemented to create the NAPTR DNS record on AWS Route53 is available in the GitHub repository:  [BPC-OpenSourceTools/sml-service-r53](https://github.com/BPC-OpenSourceTools/sml-service-r53).  
  
## SMP
  
The BPC also has an application to test the SMP REST API service calls on the same domain as the SML at  [https://smp-api.sc-b2b.us/docs](https://smp-api.sc-b2b.us/docs) .  Again, this is a REST API to make web service calls to test the toolkit.  

The SMP iitself s a web service queried by a SOAP API call to return the Corner 3 URI or terminal endpoint.  The specification for the actual API can be found in the document: [Service Metadata Publishing (SMP) Version 2.0](http://docs.oasis-open.org/bdxr/bdx-smp/v2.0/bdx-smp-v2.0.html) dated 14 February 2021 as an Oasis standard.   

__Section 5.4 Resources__  


| Resource  | URI | Method  | XML resource root element | HTTP Status | Description of returned content |    
| ------ | ------ | ------ | ------ | ------ | ------ |  
| test | test | test | test | test | test |  
| ServiceGroup | ./bdxr-smp-2/[{identifier scheme}::]{participant id} See section 3.6 for {participant id} format | GET | <ServiceGroup\> |  200; 500; 404 | Holds the Participant Identifier of the recipient, and a list of references to individual ServiceMetadata resources that are associated with that participant identifier.  |   
| ServiceMetadata | ./bdxr-smp-2/[{identifier scheme}::]{participant id}/services/{service ID} See section 3.7 for {service ID} format | GET |  <ServiceMetadata\>  | 200; 500; 404 | Holds all of the metadata about a Service, or a redirection URL to another Service Metadata Publisher holding this information. |

The SMP service proivded by the BPC registers a urn for query.  Note that the API specification is essentially the urn with modifications to include some additional service capability codes but mostly to accomodate characters that would otherwise be illegal in a URL.  

After registering a urn(s) on the SML service, go to the SMP service at [https://sml-api.sc-b2b.us/docs](https://sml-api.sc-b2b.us/docs) to register the urn there in order to get a reponse for testing SMP query functionality.

The code implemented to create the NAPTR DNS record on AWS Route53 is available in the GitHub repository:  [BPC-OpenSourceTools/smp-service](https://github.com/BPC-OpenSourceTools/smp-service).

??? warn "Client/server certificate trust implicit in the test doman."
    The SMP service specification has rules regarding Access Point and Reqestor security certificates (client) and SMP provider (server side)  security certificates to estabilish non-reputability, etc.   The BPC e-Invoice workgroup has not fully addressed the question of how the security certificate relationships are going to be managed.  As such, the test application does not validate the client/requestor or its Access Point.  It does return the security certificate of the server in its response, registered under letencrypt.org.  In the future, if rules were to be finalized, the security certicate relationship would need to be incorporated into the SMP REST API  protocol.   





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
