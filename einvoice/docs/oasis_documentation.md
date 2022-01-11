The documents referenced are:  

|Referenced Documents| 
|----|
|[OASIS ebXML Messaging Services Version 3.0: Part1, Core Features](http://docs.oasis-open.org/ebxml-msg/ebms/v3.0/core/os/ebms_core-3.0-spec-os.html) OASIS Standard, October 1, 2007, has the namespace URI of:  |
|[ebXML Messaging Services Version 3.0 Core Features)](https://docs.oasis-open.org/ebxml-msg/ebms/v3.0/ns/core/200704/) and references the XSD file:  |
|[ebms-header-3_0-200704](https://docs.oasis-open.org/ebxml-msg/ebms/v3.0/core/os/ebms-header-3_0-200704.xsd) including snippets of sample XML and full SOAP for message headers.  Note that the Namespace URI identified in Part1 is incorrect and returns an error message.  |
|[OASIS ebXML Messaging Services Version 3.0: Part 2, Advanced Features](https://docs.oasis-open.org/ebxml-msg/ebms/v3.0/part2/201004/ebms-v3-part2-cd-01.html) dated June 30, 2010 with Normative Reference of: 
|[ebXML Messaging Services Version 3.0: Part 2, Advanced Features](https://docs.oasis-open.org/ebxml-msg/ebms/v3.0/part2/201004/rddl-ebms3-part2.html) which is referenced by the following three namespace URIs.  |
|Namespace URI: [ebXML Messaging V3 Part 2: Multihop Routing](http://docs.oasis-open.org/ebxml-msg/ns/ebms/v3.0/multihop/200902)  |
|Namespace URI: [ebXML Messaging V3 Part 2: Message Fragments](http://docs.oasis-open.org/ebxml-msg/ns/v3.0/mf/2010/04/)  |
|Namespace URI: [Resource Directory Description Language\(RDDL\) 2.0](http://www.openhealth.org/RDDL/20040118/rddl-20040118.html) and references the XSD files below.|
|XSD File: [XSD for Routing Input reference parameter](http://docs.oasis-open.org/ebxml-msg/ebms/v3.0/part2/201004/ebms-multihop-1_0-200902_refactored.xsd)  |
|XSD File: [MessageFragment XSD](http://docs.oasis-open.org/ebxml-msg/ebms/v3.0/part2/201004/mf.xsd)  |
|XSD File: [Refactored Core Messaging XSD](http://docs.oasis-open.org/ebxml-msg/ebms/v3.0/part2/201004/ebms-header-3_0-200704_refactored.xsd)  |
|[OASIS ebXML Messaging Services 3.0 Conformance Profiles](https://docs.oasis-open.org/ebxml-msg/ebms/v3.0/profiles/20707/ebms3-confprofiles-cs-01.html), Committee Specification 1, dated April 24, 2010 references the same namespace URI of http://docs.oasis-open.org/ebxml-msg/ns/ebms/v3.0/profiles/200707.  |
|[AS4 Profile of ebMS 3.0 Version 1.0](http://docs.oasis-open.org/ebxml-msg/ebms/v3.0/profiles/AS4-profile/v1.0/os/AS4-profile-v1.0-os.html) dated January 23, 2013.  |
<!-->
<hr style="margin-top: 30px;
        margin-left: auto;
        margin-bottom: 20px;
        margin-right: auto;">
Interoperable components under the AS4 Usage Agreements as specified in Section 5.2 of the AS4 Profile of ebMS are non-normative.  (Excepting that the new AS4 Interoperabilty Profile for Four Corners Newtworks does attempt to make interoperation normative via P-Mode configuration.)  Samples of SOAP including XML/XMLNS and XSLT are included in Appendix A of the AS4 Profile.  
  
The best infrastructure disappears and the process being implemented are seemless and agnostic to the infrastrucutre. The process don't care how the work gets done as long as it gets done. 
  
P-Mode configuration is done at the corner/access point.  

P-Mode information contained in messages do not change p-mode values on the Access Point.  

P-Mode values are required and evaluated by the spec, but they only determine if the configuration is good when measured against the spec itself.  We're checking to see if the message meets the spec, the purpose of which is to meet the spec.  

What are we trying to solve for here?  It can't messaging handling, as that's the job of the Access Point and once the message has specified it's type or required capability it's only job is to be transported to an endpoint for consumption.    

But that has no impact on the actual configuration or capability offered by the Accees Point.  If the Access Point is not modified or changed by the P-Mode configuration, why is P-Mode configuration in the message? A message of a given type, such as an einvoice, should always be handled the same way by and Access Point. Even if every P-Mode item were required to indicate to the Access Point how to handle the message, Upon providing an identifier of the message type the Access Point will be configured to execute on the message without any other input from message.  It's not changing P-mode values on the fly, which is implied their requirement in the message, when their only purpose is to as Access Point configuration.

  ofthe not convey any information about how the infrastructure should  There is no reason the message itself needs to indicate access point configuration, as there's no way the P-Modes are being impacted or configured by the messages.  If P-Modes were dynamic based on content in the messages, then requiring P-Mode configuration in the message would make sense. However since the access point P-mode configurations are not dynamically changing the P-Mode information is extraneous.  The message is not dynamically changing based on P-Modes, nor does it introspect itself to determine if it's own configuration is correct.  Rather, it's access point that must include these additonal   A well defined XSD (really this should be obtianed by an API call) 
	
<hr style="margin-top: 30px;
        margin-left: auto;
        margin-bottom: 20px;
        margin-right: auto;">
There should be a namespace URI for the committee specfifcation called https://docs.oasos-open.org/bdxr/ns/bdx-as4/v1.0/profiles/202112. This is inferred from the ebXML Messaging V3 (ebMS3) namespace at http://docs.oasis-open.org/ebxml-msg/ns/ebms/v3.0/profiles/200707.

-->


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