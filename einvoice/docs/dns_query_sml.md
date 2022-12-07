# DNS Query Functionality

The code below provides an example of how to query a DNS record, specifically using the NAPTR __regexp__ field specified in the NAPTR protocol.   NAPTR fields are treated as a __set__ , using Python to iterate it, and using the regexp field to directly access the data.

!!! Important "The BPC SML Domain"
    The BPC SML Domain is:
    __bpcb2b.net__

## Example - Querying a DNS NAPTR Record

### 1.  Import the necessary module
The example implements the ```dns.resolver``` Python module.   

    import dns.resolver 

### 2. Provide the hashed URN for look-up  
For the example, the URN is already created, hashed, and the domain of "sc-b2b.us" is appended.  (This was functional at the time of initial development.)   

    hashed_value = "6c24uvqpxrfyweqimfxmsuym3bbjvoikuwmmidquz2a2zzyikdya.sc-b2b.us"

### 3. Do the DNS look-up  
The look-up is returned from the ```resolve()``` method of    ```dns.resolver.```  In this implementation, the method takes two parameters, the query string, and the look-up type.  See [Resolver Functions and the Default Resolver](https://dnspython.readthedocs.io/en/latest/resolver-functions.html) for the complete method signature.  
<br/>
!!! note "dns.resolver.resolve() return type is dns.resolver.Answer"
    The dns.resolver.resolve() method return type is __dns.resolver.Answer__.  See [The dns.resolver.Resolver and dns.resolver.Answer Classes](https://dnspython.readthedocs.io/en/latest/resolver-class.html) for details on the Answer response class. 
    <br/>

### 4. The NAPTR DNS query response
<br/>
#### 4a.  The response as Rdata
Rdata is typed data in one of the known DNS data types, i.e., an IPv4 address for a host, MX record, or NAPTR record.  RRset is an Rdata object which supports the Python __set__ API.  For details on RRset see [Rdataset, RRset, and Node Classes](https://dnspython.readthedocs.io/en/latest/rdata-set-classes.html).  
<br/>
#### 4b. The fields in the NAPTR response
The returned Rdata data set is in the format as [specified by the NATPR protocol](https://www.ietf.org/rfc/rfc2915.txt) and contains the following fields which may be iterated as a set: 

    Order Preference Flags Service Regexp Replacement

The set values are iterated using:  

    for a in lookup.rrset:

<br/>
#### 4c. The "regexp" field of the NATPR response
The value of the "regexp" field contains the terminal address of the SMP in the format of a regular expression, which is how it would otherwise be used if doing a Session Initiation Protocol (SIP) lookup.   
The value is directly accessed using:   

     for a in lookup.rrset:
        smp_uri = a.regexp
<br/>
#### 4d. The response as a string
Use the String decode() method to change the returned response from Binary to String format.    

    smp_uri = smp_uri.decode()    
The final response is the terminal SMP URL in the NAPTR regular expression substitution format.  
<br/>
## Code

    import dns.resolver

    hashed_value = "6c24uvqpxrfyweqimfxmsuym3bbjvoikuwmmidquz2a2zzyikdya.sc-b2b.us"
    lookup = dns.resolver.resolve(hashed_value,'NAPTR')
    print(type(lookup))
    for a in lookup.rrset:
        smp_uri = a.regexp
    smp_uri = smp_uri.decode()
    print(smp_uri)

## Output 

    <class 'dns.resolver.Answer'>
    !^.*$!https://my-smp-url.com/0123456789!