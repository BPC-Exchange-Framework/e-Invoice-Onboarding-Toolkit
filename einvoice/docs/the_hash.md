The Four-Corner Model is premised on a NAPTR DNS look-up to obtain the location of the SMP URI.  The SMP URI is then used to query the SMP REST API and obtain the Corner 3 URI.  

The assumption is that a NAPTR DNS record exists as a key:value pair.  A look-up of the "key" in the DNS of the NAPTR record will return the "value."

The "key" is the hashed value of the URN.
The URN is the composite of the specification, the schema_id, and the party_id. 
The hash is:
1) concattonate the elements of the URN into a single string value. Note a single colon between the specification and the schema_id and double colon between the schema_id and the party_id.
specification + ":"  + schema_id + "::" + party_id


The Four-Cormer Model
```mermaid
        stateDiagram-v2
            [*] --> Seller
            Seller --> Access_Point_1
            state Access_Point_1 {
                [*] --> SML
                state SML {
                    [*] --> Create_Hash
                        state Create_Hash {
                           [*] --> Receive_inputs
                            Receive_inputs --> Concatonate
                            Concatonate --> to_lower_case
                            to_lower_case --> encode_utf8
                            encode_utf8 --> sha256_hash
                            sha256_hash --> byte_digest_of_hash
                            byte_digest_of_hash --> base32_hash
                            base32_hash --> strip_extra_chars
                            strip_extra_chars --> decode_to_string
                            decode_to_string --> ensure_lower_case
                            ensure_lower_case --> [*]
                        }
                    Create_Hash --> add_domain 
                    add_domain --> dns_query
                        state dns_query {
                            [*]  --> hashed_urn
                            hashed_urn --> do_dns_look-up
                            do_dns_look-up -->  [*]
                    }
                    dns_query --> [*]
                }
                SML --> SMP 
                state SMP {
                    [*] --> Create_requests
                    Create_requests --> Request_1
                    Request_1 --> Request_2
                    Request_2 --> [*]
                }
                SMP --> [*]
            }
            Access_Point_1 --> Access_Point_2
            Access_Point_2 --> Buyer
            Buyer --> [*]
            

```



