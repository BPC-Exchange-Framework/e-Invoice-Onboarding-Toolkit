# The Repository<hr/>


### Repository Layout

This project includes the following files, _i.e., "artifacts"_ in __.py__, .__md__, .__txt__ and other formats, updated as of:  
__02/16/2022 (February 16th, 2022)__

```
/E-Invoice-Onboarding-Toolkit  
.
├── LICENSE
├── README.md
├── ebms-header-3_0-20220119.xsd
├── einvoice
│   ├── __init__.py
│   ├── delivery
│   │   ├── __init__.py
│   │   ├── ebms-header-3_0-20220119.xsd
│   │   ├── import_xsd.py
│   │   ├── sample_msg.xml
│   │   └── tests
│   ├── discovery
│   │   ├── __init__.py
│   │   ├── accessor.py
│   │   ├── app_handler.py
│   │   ├── app_logging.py
│   │   ├── conf
│   │   │   ├── __init__.py
│   │   │   ├── config_tool.py
│   │   │   └── smp_config.py
│   │   ├── create_tracking_id.py
│   │   ├── data
│   │   │   ├── __init__.py
│   │   │   ├── create_sample_data.py
│   │   │   ├── item_list.csv
│   │   │   └── per_item_list.csv
│   │   ├── dns_query.py
│   │   ├── ebms-header-3_0-20220119.xsd
│   │   ├── ebms-header.xml
│   │   ├── einvoice_message_package.py
│   │   ├── line_item.py
│   │   ├── party_address.py
│   │   ├── semantic_model.py
│   │   ├── smp_query.py
│   │   ├── urn.py
│   │   └── urn_hasher.py
│   ├── docs
│   │   ├── __init__.py
│   │   ├── _license.md
│   │   ├── accessor.md
│   │   ├── accessor_results.png
│   │   ├── app_handler.md
│   │   ├── app_log.png
│   │   ├── app_logging.md
│   │   ├── artifacts.md
│   │   ├── assumptions.md
│   │   ├── create_tracking_id.md
│   │   ├── custom_theme
│   │   │   ├── css
│   │   │   └── main.html
│   │   ├── dns_query.md
│   │   ├── drawio
│   │   │   ├── Bounded Context - Entity Relationships 1.3.drawio
│   │   │   ├── Bounded Context - Functional Capabilities 1.2.drawio
│   │   │   └── Bounded Context - Participant 1.1.drawio
│   │   ├── einvoice_design.xlsx
│   │   ├── einvoice_message_package.md
│   │   ├── enabling_infrastructure_components.md
│   │   ├── faq.md
│   │   ├── flask_integration_on_docker.md
│   │   ├── git_workflow.md
│   │   ├── google_colab_pages.md
│   │   ├── index.md
│   │   ├── jupyterlab
│   │   │   ├── Validate_bdx-as4.ipynb
│   │   │   ├── Validate_bdx-as4_v2.ipynb
│   │   │   ├── dns_query.ipynb
│   │   │   ├── ebms-header-3_0-20210119.xsd
│   │   │   ├── ebms-header-3_0-20220119.xsd
│   │   │   ├── naptr_lookup.ipynb
│   │   │   ├── python_dev.ipynb
│   │   │   ├── sample_msg.xml
│   │   │   ├── tracking_id_sandbox.ipynb
│   │   │   └── urn_hash_work.ipynb
│   │   ├── line_item.md
│   │   ├── oasis_documentation.md
│   │   ├── outcomes.md
│   │   ├── party_address.md
│   │   ├── pdf
│   │   │   ├── Bounded Context - Entity Relationships 1.4.pdf
│   │   │   ├── Bounded Context - Functional Capabilities 1.2.pdf
│   │   │   ├── Bounded Context - Functional Capabilities 1.3.pdf
│   │   │   ├── Bounded Context - Participant 1.1.pdf
│   │   │   └── Bounded Context - Participants 1.2.pdf
│   │   ├── project_roadmap.md
│   │   ├── python_dev_env.md
│   │   ├── requirements.md
│   │   ├── semantic_model.md
│   │   ├── smp_query.md
│   │   ├── start_to_finish.md
│   │   ├── successful_tests.png
│   │   ├── test_cases.md
│   │   ├── todo.md
│   │   ├── tools_and_resources.md
│   │   ├── urn.md
│   │   ├── urn_handler.md
│   │   ├── urn_hasher.md
│   │   ├── using_the_modules.md
│   │   └── working_with_the_code.md
│   ├── mkdocs.yml
│   └── test
│       ├── __init__.py
│       ├── ebms-header-3_0-20220119.xsd
│       ├── ez_linter.sh
│       ├── flake8_linter.sh
│       ├── hardcore_linter.sh
│       ├── magic_linter.py
│       ├── mypy_linter.sh
│       ├── pycodestyle_linter.sh
│       ├── pydocstyle_linter.sh
│       ├── pylint_linter.sh
│       ├── test_accessor.py
│       ├── test_app_logging.py
│       ├── test_create_sample_data.py
│       ├── test_create_tracking_id.py
│       ├── test_dns_query.py
│       ├── test_import_xsd.py
│       ├── test_line_item.py
│       ├── test_party_address.py
│       ├── test_semantic_model.py
│       ├── test_smp_query.py
│       ├── test_urn.py
│       ├── test_urn_hasher.py
│       └── unaptr_response.json
├── requirements.txt
└── todo.md

13 directories, 113 files
```
