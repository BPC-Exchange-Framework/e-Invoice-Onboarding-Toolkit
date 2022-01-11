## Project Artifacts<hr/>
  
### 4-Corners Model and OASIS Specifications
For full documentation visit [mkdocs.org](https://www.mkdocs.org).  
  
 <br/> 


### Project layout

This project inclues the following artifacts:  
```
/e-Invoice-Onboarding-Toolkit  
├── einvoice  
│   ├── docs  
│   │   ├── custom_theme  
│   │   │   ├── css  
│   │   │   │   └── extra.css  
│   │   │   └── main.html  
│   │   ├── drawio  
│   │   │   ├── Bounded Context - Entity Relationships 1.3.drawio  
│   │   │   ├── Bounded Context - Functional Capabilities 1.2.drawio  
│   │   │   └── Bounded Context - Participant 1.1.drawio  
│   │   ├── jupyterlab  
│   │   │   ├── dns_query.ipynb  
│   │   │   ├── naptr_lookup.ipynb  
│   │   │   ├── python_dev.ipynb  
│   │   │   ├── tracking_id_sandbox.ipynb  
│   │   │   ├── untitled.txt  
│   │   │   └── urn_hash_work.ipynb  
│   │   ├── pdf  
│   │   │   ├── Bounded Context - Entity Relationships 1.4.pdf  
│   │   │   ├── Bounded Context - Functional Capabilities 1.2.pdf  
│   │   │   ├── Bounded Context - Functional Capabilities 1.3.pdf  
│   │   │   ├── Bounded Context - Participant 1.1.pdf  
│   │   │   └── Bounded Context - Participants 1.2.pdf  
│   │   ├── Creating-a-Common-Dev-Environment.md  
│   │   ├── Google-Colab-Pages.md  
│   │   ├── Home.md  
│   │   ├── Integrating.md  
│   │   ├── LICENSE.md  
│   │   ├── Project-Roadmap.md  
│   │   ├── The-Main-Components.md  
│   │   ├── Working-with-the-Code.md  
│   │   ├── _Footer.md  
│   │   ├── _README.md  
│   │   ├── \_\_init\_\_.py  
│   │   ├── einvoice_design.xlsx  
│   │   ├── git-workflow.md  
│   │   ├── index.md  
│   │   ├── python_dev_env.md  
│   │   ├── requirements.md  
│   │   ├── todo.md  
│   │   └── tree.txt  
│   ├── einvoice  
│   │   ├── conf  
│   │   │   ├── \_\_init\_\_.py  
│   │   │   ├── config_tool.py  
│   │   │   └── smp_config.py  
│   │   ├── data  
│   │   │   ├── \_\_init\_\_.py  
│   │   │   ├── create_sample_data.py  
│   │   │   ├── item_list.csv  
│   │   │   └── per_item_list.csv  
│   │   ├── tests  
│   │   │   ├── \_\_init\_\_.py  
│   │   │   ├── hardcore_linter.sh  
│   │   │   ├── magic_linter.py  
│   │   │   ├── not_so_hard_linter.sh  
│   │   │   ├── test_accessor.py  
│   │   │   ├── test_app_logging.py  
│   │   │   ├── test_create_sample_data.py  
│   │   │   ├── test_create_tracking_id.py  
│   │   │   ├── test_dns_query.py  
│   │   │   ├── test_line_item.py  
│   │   │   ├── test_party_address.py  
│   │   │   ├── test_semantic_model.py  
│   │   │   ├── test_smp_query.py  
│   │   │   ├── test_urn.py  
│   │   │   ├── test_urn_hasher.py  
│   │   │   └── unaptr_response.json  
│   │   ├── \_\_init\_\_.py  
│   │   ├── accessor.py  
│   │   ├── app_logging.py  
│   │   ├── create_tracking_id.py  
│   │   ├── dns_query.py  
│   │   ├── einvoice_message_package.py  
│   │   ├── line_item.py  
│   │   ├── party_address.py  
│   │   ├── semantic_model.py  
│   │   ├── smp_query.py  
│   │   ├── urn.py  
│   │   ├── urn_handler.py  
│   │   └── urn_hasher.py  
│   └── mkdocs.yml  
├── LICENSE  
├── README.md  
├── requirements.txt  
└── todo.md  
  
11 directories, 75 files  
```

<div style="font-size: 12px;
            padding: 15px;
            border: 2px solid lightgray;
            margin-top: 100px;
            margin-left: 0px;
            margin-bottom: 40px;
            margin-right: auto;
            width: 90%;
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