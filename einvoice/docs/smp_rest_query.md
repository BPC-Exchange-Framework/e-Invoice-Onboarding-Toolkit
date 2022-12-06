
# SMP REST API Query

Query to an SMP service to obtain terminal or final "Endpoint" destination of the e-invoice is implemented using two REST API web service calls.   


## References  
* See the [BPC SMP Profile Version 1.0](https://github.com/BPC-Exchange-Framework/BPC-Market-Pilot/blob/f3844411c40dd4b84276fd3ef6020d247afd83c4/BPC%20SMP%20Profile%20Version%201.0.pdf) (the "Profile") document for general guidance to the format of this service call.  
* See the OASIS website for the authoritative [OASIS SMP 2.0 Standard](https://docs.oasis-open.org/bdxr/bdx-smp/v2.0/bdx-smp-v2.0.docx) (the "Standard").   
* Section 3 of the BPC SMP Profile referencing the REST interface specifies in Section 3.1 that client authentication must not be required when accessing SMP \[server\] resources.    
* The REST API for the web service calls are referenced in section 3.2 of the BPC SMP Profile, mandating implementation as provided in section 5.2 of the OASIS SMP 2.0 Standard.    
<br/>
???+ note "The BPC SMP Profile implements the OASIS SMP 2.0 Standard"
    Section 3.2 of the BPC SMP Profile mandates implementation of the OASIS SMP 2.0 standard.  <br/><br/>To the extent that Section 6 of the BPC Profile has a requirement that the SMP client __MUST__ validate the signature of the SMP [server response] as directed in section 5.6.2.2  of the OASIS standard, the OASIS standard is permissive and says the SMP client __MAY__ verify the signature.



??? Warning "Functional versus non-functional requirements"
    Software engineering best practices including separation of concerns and SOLID Principles, specifically the single responsibility principle, limit the functional scope to the minimum necessary to achieve the desired outcome.
    
    Minimum Viable Product as outlined in the Project Goals, Project Roadmap, and Project Outcomes is achieved by abstraction of non-functional requirements.  
    
    The logic to calculate the hash necessary for the SML DNS look-up query _does not change_ regardless of the value of the specification, the schema, or the party ID.  Values provided for this data should be checked against rules from the BPC Policy and the OASIS Standard to ensure data integrity.  Separating validation of the data and computation of the URN hash provides for flexibility in changes to both rules governing the format of the data and implementation of the URN hash logic. 

## The REST Web Service calls to the SMP service

???+ Important "The rules for constructing the ServiceGroup  REST API web service call."
    In Section 5.4 "Resources" The OASIS SMP Standard provides the format used to create the ServiceGroup REST API web service call.  This specifies the __oasis-bdxr-smp-2(bdxr-smp-2)__ SMP REST binding, the "identifier scheme" and the "participant id."  The "identifier scheme" is literally the URN specifying the format the participant ID is going to take.  
    
   




 
## 1. Service Group Discovery
The first REST API query to the Service Group is created using the SMP REST binding, "identifier scheme" and "participant ID."  
### Creating the SMP REST API call #1 to obtain ServiceGroup data
<span style="font-size: 120%;">The first web service call to obtain the ServiceGroup data is constructed from:</span>

#### 1a. Use the SMP web service being queried with its fully qualified domain.   
   * Not specified, but implied to make a web service call, is the scheme or protocol of "https://"   
   * Further unspecified, but implied as it is required, is the fully qualified application server domain and reference to any sub-domains. In the case of the example, this is "smp-api.sc-b2b.us."  The subdomain is "smp-api." The second-level domain is "sc-b2b." The top level domain is "us."
   * The only REST method required to be supported by the OASIS SMP Standard is "GET."  Everything after the domain specification is the "resource" uri of the GET method request.  

Using these guidelines, in the development environment of the Onboarding Toolkit the first part of the URL is: ```https://smp-api.sc-b2b.us/.``` _This value will  be different in the Market Pilot._  In the Market Pilot, use the value _bpcb2b.net_.  The URL will begin with ```https://bpcb22.net/```  

#### 1b.  The SMP REST Binding
Section 5.5 of the OASIS SMP 2.0 Standard provides the SMP REST Binding should be ```oasis-bdxr-smp-2```.     However, In the prior Section 5.4 "Resources" the example URI indicates an SMP Binding of ```bdxr-smp-2```.    

The development and test environment of the Onboarding Toolkit use ```bdxr-smp-2``` for the value of the SMP Binding.  

The Onboarding Toolkit dev URL becomes: ```https://smp-api.sc-b2b.us/bdxr-smp-2/```    

The Market Pilot URL becomes: ```https://bpcb22.net/bdxr-smp-2/```


#### 1c.  The Identifier Scheme
The next element in the call to obtain the ServiceGroup data is the "identifier scheme" which identifies the format of the PartyID.  This value should already be known, as it is the Specification and the Schema used when creating the hash value for the SML NAPTR DNS look-up.  Together, the Specification and the Scheme create the "identifier scheme," which defines the _format_ of the party ID.   

Detailed requirements of the identifier scheme are found in the [OASIS ebCore Party Id Type Technical Specification Version 1.0](http://docs.oasis-open.org/ebcore/PartyIdType/v1.0/CS01/PartyIdType-1.0.html)  for the __ebCorePartyID__.

From the documentation, an example of a normative value for the identifier scheme is: __urn:oasis:names:tc:ebcore:partyid-type:iso6523__.  

The Onboarding Toolkit dev URL then becomes: ```https://smp-api.sc-b2b.us/bdxr-smp-2/urn:oasis:names:tc:ebcore:partyid-type:iso6523```   
  
The Market Pilot URL becomes: ```https://bpcb22.net\/bdxr-smp-2/urn:oasis:names:tc:ebcore:partyid-type:iso6523```

#### 1d. Append the PartyID
After starting with the protocol, the fully qualified domain name of the SMP Application Server, the SMP Rest Binding, and the Identifier Scheme, the last component of the ServeGroup look-up REST API web service call is the party ID.  This should be the same value as that used in creating the hash for the SML DNS look-up.  

As an example, if the party id is "bpcBusid01"...   
The Onboarding Toolkit dev URN is (the same as in the SML DNS look-up): ```urn:oasis:names:tc:ebcore:partyid-type:iso6523/bpcBusid01```   
  
The Market Pilot URN is (also the same as in the SML DNS look-up): ```urn:oasis:names:tc:ebcore:partyid-type:iso6523/bpcBusid01```
    

    


#### 1e. Create the string for the SMP REST API Query
The ServiceGroup web service call then takes the format of:```https://smp-api.sc-b2b.us/bdxr-smp-2/urn:oasis:names:tc:ebcore:partyid-type:iso6523/bpcBusid01```

  
Using the terminology employed by the OASIS SMP 2.0 specification the URL is constructed as:  ```https://bpcb22.net/bdxr-smp-2/urn:oasis:names:tc:ebcore:partyid-type:iso6523/bpcBusid01```


#### 1f. Substitute hex into the URL for successful web service call

The URL to be used for the SML REST API query is defective in that it has illegal characters that can't be parsed into a recognizable web address.  The extra colons ":" will cause problems.  To remedy this do a string search/replace substitution on the offending punctuation and convert it to hex representation which can be handled by the browser.  The hex representation of a colon is "\3A."  Substitute "\3A" in the URL every place where it is used as part  of the resource and the literal protocol.  

The ServiceGroup web service call then takes the format of:
```https://smp-api.sc-b2b.us/bdxr-smp-2/urn\3Aoasis\3Anames\3Atc\3Aebcore\3Apartyid-type\3Aiso6523\3A\3AbpcBusid01```

  
Using the terminology employed by the OASIS SMP 2.0 specification the URL is constructed as:  ```https://bpcb22.net\/bdxr-smp-2/urn\3Aoasis\3Anames\3Atc\3Aebcore\3Apartyid-type\3Aiso6523\3A\3AbpcBusid01```

??? Note "Test the SMP REST API web service call"
    When the URL is constructed properly it is a simple matter to copy and paste it into a web browser.  The response should  be the SMP ServiceGroup look-up data in XML format.

#### 1g. Make the web service call

The response of the Service Group Discovery returns information necessary to construct the Service Metadata Query.  The BPC SMP Profile requires that the Service Group Discovery REST API call must not be skipped and that the presence of Service Metadata should not be assumed.


## Example
    protocol = "https"
    uri = "smp-api.sc-b2b.us"
    standard = "bdxr-smp-2"
    identifier_scheme = "urn:oasis:names:tc:ebcore:partyid-type:iso6523:0088"
    participant_id = "123456789"
    urn = identifier_scheme + "::" + participant_id 
    query_url_1 = protocol + "://" + uri + ":" + identifier_scheme + "::" + participant_id
    query_url_2 = protocol + "://" + uri + ":" + urn
    print(f"Value of query_url_1: {query_url_1}")
    print(f"Value of query_url_2: {query_url_2}")
    print(f"constructed urls are the same: {query_url_1 == query_url_2}")  

## Output 
    Value of query_url_1: https://smp-api.sc-b2b.us:urn:oasis:names:tc:ebcore:partyid-type:iso6523:0088::123456789
    Value of query_url_2: https://smp-api.sc-b2b.us:urn:oasis:names:tc:ebcore:partyid-type:iso6523:0088::123456789
    constructed urls are the same: True

## 2. Service Metadata Query

### Call #2 to obtain ServiceMetadata

???+ important "Inferring values for the ServiceMetadata REST web service call"
    In the BPC Proof of Concept and creation of the Onboarding Toolkit, the service and document schemas defined by the SMP were static.  

    The QName Subtype Identifier was used.   Validation of the queries resulted in assumption of the  value of some ServiceMetadata parameters.  <br/><br/>
