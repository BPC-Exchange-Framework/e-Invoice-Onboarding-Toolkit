### Discovery #1 - SML NAPTR DNS Lookup

1.	Feature – Access Point A sends UNAPTR DNS query with a Party ID/Party ID Schema hash and obtains a valid response with connection information to the SMP.  
  
|Action|Actor|Scoped?|
|----------|----------|----------|
|Generate the request to Access Point A, which includes Party ID, Party ID Schema, Invoice Data|Seller|No|
|Transform and format contents of Seller’s request to create UNAPTR DNS query.|Access Point A	Yes|
|Query DNS.|Access Point A|Yes|
|Return response to query.|SML – Reply from UNAPTR DNS query.|No|
|Receive query response from DNS, which is the URI to the SMP|Access Point A|Yes|  
  
### Discovery #2 - SMP REST API Query  
  
2.	Feature –Access Point A sends a REST API query to the SMP URI to obtain a valid response with connection info of target Access Point and customers invoice capabilities.  
  
|Action|Actor|Scoped?|
|----------|----------|----------|
|Send response with SMP URI to Access Point.|SML|No (not in this feature)|
|Create REST query to service provider to obtain buyer’s service capabilities.|Access Point A|Yes|
|Send REST query to service provider to obtain participant’s service capabilities.|Access Point A|Yes|
|Receive query and send response with Sellers Capabilities and route to endpoint.|SMP|No|
|Receive response to query of participant’s capabilities.|Access Point A|Yes|  
  
### Delivery - AS4 Message Exchange  
  
3.	Feature – An invoice with a semantically correct format is delivered using AS4 protocol.  
  
|Action|Actor|Scoped?|
|----------|----------|----------|
|Compose semantically correct e-Invoice based on response from service provider about participant’s capabilities.|Access Point A|Yes|
|Format e-Invoice in compliant AS4 format.|Access Point A|Yes|
|Send e-Invoice to final destination obtained from SMP service provider.|Access Point A|Yes|
|Receives the request.|Access Point B|No|



<div style="font-size: 12px;
            padding: 15px;
            border: 2px solid lightgray;
            margin-top: 100px;
            margin-left: 0px;
            margin-bottom: 40px;
            margin-right: auto;
            width: 70%;
            border-radius: 10px;">
  <h4 style="font-size: 14px;
            padding: 0px;
            margin: 0px;">No Representations or Warranties</h5>
  This software is free and Open Source offered under an MIT license. The developers of the software make no
  representations or warranties as to the software or its fitness for a particular purpose. This code is meant for
  educational and research purposes only. The code is offered "as-is" and is not intended to be used in a production
  environment. It is intended for developers of software related to the 4-corners Model to use as a stepping-off point
  for further development efforts.
</div>