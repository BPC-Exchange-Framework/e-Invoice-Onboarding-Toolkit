# Creating the SML URN Hash  
The SML look-up is a NAPTR DNS query which returns the URL of the SMP. The record queried is a URN constructed from the combined Specification, Schema, and Party ID and then hashed.  After the hash is created, the URN is combined with the look-up domain.  This combination of URN and domain is the record locator for the information in the DNS.  

The Python code, as script, function, or method, provides elaboration and implementation of the process as described in Section 3.2 of the [BPC SML Profile Version 1.0](https://github.com/BPC-Exchange-Framework/BPC-Market-Pilot/blob/f3844411c40dd4b84276fd3ef6020d247afd83c4/BPC%20SML%20Profile%20Version%201.0.pdf) document found on the [BPC-Exchange-Framework/BPC-Market-Pilot Github site](https://github.com/BPC-Exchange-Framework/BPC-Market-Pilot).  
<br/>
!!! Important "The BPC SML Domain"
    The BPC SML Domain is:
    __bpcb2b.net__

<br/>
## Information needed to create the URN
Three data points are required to create the URN:  
 <ul>
   <li>Specification  (urn:oasis:names:tc:ebcore:partyid-type)</li>
    <li>Schema (iso6523:0060)  </li>
    <li>PartyID</li>
</ul>  
<br/>
??? note "Format of Specification, Schema, and Party ID is assumed to be conformant"
    The standard articulated for an __ebCorePartyId__ referenced in the [Business Document Metadata Service Location Version 1.0](https://docs.oasis-open.org/bdxr/BDX-Location/v1.0/os/BDX-Location-v1.0-os.html) referring to the [OASIS ebCore Party Id Type Technical Specification Version 1.0](https://docs.oasis-open.org/ebcore/PartyIdType/v1.0/PartyIdType-1.0.odt) provides normative guidelines for the values used for the Specification and Schema.      

    This code does not validate or enforce compliance with those standards. There is no Inspection or validation of values used for the Specification, Schema, and Party ID used to create a URN hash for look-up.  Conformance for those values are assumed, however the code works on any string of data. 
          
    
<br/>  


## Example - Creating the URN hash
<br/>  

### 1. Import Modules  
The ```hashlib``` and ```bas64``` Python modules are used in this process.  

    import hashlib
    import base64
<br/>    


### 2. Concatenate the string    
Strings are a primitive data type in Python.  Instantiate and initialize string variables for the 
individual data values and concatenate them into a single string.   Simple validation of the correct 
format of the urn is included.  

    specification = "urn:oasis:names:tc:ebcore:partyid-type:unregistered:myscheme"  
    schema = "BPC01"  
    party_id = "bpcBusid01"   
    urn = specification + ":" + schema + "::" + party_id  
    urn_test_case = 
        "urn:oasis:names:tc:ebcore:partyid-type:unregistered:myscheme:BPC01::bpcBusid01"
    print(f"urn is concatenated properly: {urn == urn_test_case}")  
    print(urn)


!!! important "Punctuation"
    Note the use of a single and a double colon as separators between the values.  These are 
    includes as part of the string and are __required__.  


<br/>  


### 3. Convert to lower-case  
Implements the Python String ```lower()``` method.

    lower_case_urn = urn.lower()
    print(f"URN converted to lower case: {lower_case_urn}")

<br/>  



### 4. Encode as utf-8  
The sha256 and base32 operations done on the string are Buffered Protocols, 
which requires that they be in a 
[bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) 
format in Python.  This is obtained using the String ```encode()``` 
method specifying "utf-8" as the format.  
The ```bytes(x, encoding, error)``` function could also be used here. 
    
    urn_encoded =  lower_case_urn.encode('utf-8')
    print (f"URN encoded as utf-8: {urn_encoded}")

<br/>  


### 5. Create sha256 hash  
This implements the ```sha256()``` method of the hashlib module imported in Step \#1.     
    
    sha256_urn  = hashlib.sha256(urn_encoded)
    print (f"URN hashed using sha256 {sha256_urn}")  

<br/>    
  
### 6. Obtain the 'digest'   
The digest is the concatenation of all of the data fed into the hash so far, i.e., the current value.  
(Though implemented as a single operation here, the buffered protocol allows for additions and updates to the hash.)  The ```digest()``` method is included in the ```hashlib``` module.

    sha256_digest = sha256_urn.digest()
    print(f"Digest of buffered stream containing results thus far: {sha256_digest}")

<br/>  




### 7.  Encode into base32 
??? note "Why encode in base32?"
    Encryption using sha256 results in a one-way hash. The original value of the URN is not intended to be derived from that hash as that is cryptographically impossible.  (Encoding the sha256 hash into base32 is __not__ one way.)  <br/><br/>The sha256 hash is 256 bits, or 32 bytes. A two digit hexadecimal representation of the 32 byte hash is 64 characters long.  Since base32 encoding has a character set of 32 compared to hexadecimal's 16, the sha256 hashed value can be represented in 32 characters in base32 instead of the 64 required for hex.  <br/><br/>
    The irreversibility of the sha256 hash implies that the process is cryptographically significant.  It is not.  The hashed URN is ultimately used as a dictionary look-up in the DNS record _for a given domain_. Where a common specification and schema are in use by many participants, it becomes imperative that the PartyIDs are unique _for a specific domain_.  Otherwise, while a sha256 hash can't be reversed, it can be __duplicated__.  <br/><br/>
    The output of this process is a 256 bit/32 byte value represented in a base 32 character set.
    

Take the digest entry, still a bytes-like object, and encode it in base32, 
resulting in a string 32 characters in length.  This implements the ```b32encode``` 
method of the base64 module.

    b32_urn = base64.b32encode(sha256_digest)
    print(f"The base32 encoded representation of the URN: {b32_urn}")

<br/>    

### 8.  Strip off extras  
The base32 encoding may result in extra characters at the end of the string.  
The ```rstrip``` String method is used to 
remove any of this additional padding at the end of the string.

    b32_urn_clean = b32_urn.rstrip(b"=")
    print(f"The URN with any padding removed {b32_urn_clean}")


<br/>    



### 9. Convert back to a String  
The object is still in a binary or bytes-like object format.  
Convert it back into a String primitive using the String ```decode('utf-8)``` method 
where 'utf-8' was the original encoding method.  

    b32_str = b32_urn_clean.decode('utf-8')

<br/>    



### 10. Convert to lower-case  
Per the specification, ensure the output is entirely in lowercase. 
This implements the String ```lower()``` method again.  

    final = b32_str.lower()

<br/>   


### Final Output  
The final output of the hash algorithm.

    print(f"The final result: {final}")
    
    


<hr>
<br/>  
<br/>  



## Code
The entirety of the Python code for the hash algorithm - can be run as a script or a function.

        #########################################################
        #
        #  Example Constructing a URN for SML DNS NAPTR look-up
        #
        ##########################################################
        # import the modules
        import hashlib
        import base64
        # get the urn
        specification = "urn:oasis:names:tc:ebcore:partyid-type:unregistered:myscheme"
        schema = "BPC01"
        party_id = "bpcBusid01"
        urn = specification + ":" + schema + "::" + party_id
        urn_test_case = 
            "urn:oasis:names:tc:ebcore:partyid-type:unregistered:myscheme:BPC01::bpcBusid01"
        print(f"urn is concatenated properly: {urn == urn_test_case}")
        print(urn)
        # make sure it's converted to lower case
        lower_case_urn = urn.lower()
        print(f"URN converted to lower case {lower_case_urn}")
        # has to be a byte-like object to be hashed, so encode it as utf-8
        urn_encoded =  lower_case_urn.encode('utf-8')
        print (f"URN encoded as utf-8: {urn_encoded}")
        # now create the sha256 hash of it
        sha256_urn  = hashlib.sha256(urn_encoded)
        # get the current value of the buffer stream
        sha256_digest = sha256_urn.digest()
        print(f"Digest of buffered stream containing results thus far: {sha256_digest}")
        #encode into b32 
        b32_urn = base64.b32encode(sha256_digest)
        print(f"The base32 encoded representation of the URN: {b32_urn}")
        # strip off the equals sign.... 
        b32_urn_clean = b32_urn.rstrip(b"=")
        print(f"The URN with any padding removed {b32_urn_clean}")
        # convert it back to string.
        b32_str = b32_urn_clean.decode('utf-8')
        # make sure it's in lower case again.
        final = b32_str.lower()
        # This should be your final answer
        print(f"The final result: {final}")
<hr>  
<br/>  



## Output 

    urn is concatenated properly: True
    urn:oasis:names:tc:ebcore:partyid-type:unregistered:myscheme:BPC01::bpcBusid01
    URN converted to lower case: urn:oasis:names:tc:ebcore:partyid-type:unregistered:myscheme:bpc01::bpcbusid01
    URN encoded as utf-8: b'urn:oasis:names:tc:ebcore:partyid-type:unregistered:myscheme:bpc01::bpcbusid01'
    URN hashed using sha256 <sha256 _hashlib.HASH object @ 0x106202710>
    Digest of buffered stream containing results thus far: b'\xc3{4\xfc3"\xdb\xc1u\xdcd\xe8\xbf\xe2\xad\x86\xdfjxob\x1e\'\x17\x8f\xb0\x83!\xec\x15\xab~'
    The base32 encoded representation of the URN: b'YN5TJ7BTELN4C5O4MTUL7YVNQ3PWU6DPMIPCOF4PWCBSD3AVVN7A===='
    The URN with any padding removed b'YN5TJ7BTELN4C5O4MTUL7YVNQ3PWU6DPMIPCOF4PWCBSD3AVVN7A'
    The final result: yn5tj7bteln4c5o4mtul7yvnq3pwu6dpmipcof4pwcbsd3avvn7a

<br/><br/>