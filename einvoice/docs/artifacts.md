## The Repo(sitory)<hr/>


### Repository Layout

This project includes the following files, _i.e., "artifacts"_ in __.py__, .__md__, .__txt__ and other formats, updated as of:  
__02/07/2022 (February 7th, 2022)__

```
/e-Invoice-Onboarding-Toolkit  
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
│   │       ├── __init__.py
│   │       └── test_import_xsd.py
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
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   ├── ebms-header-3_0-20220119.xsd
│   │   │   ├── ez_linter.sh
│   │   │   ├── flake8_linter.sh
│   │   │   ├── hardcore_linter.sh
│   │   │   ├── magic_linter.py
│   │   │   ├── mypy_linter.sh
│   │   │   ├── pycodestyle_linter.sh
│   │   │   ├── pydocstyle_linter.sh
│   │   │   ├── pylint_linter.sh
│   │   │   ├── test_accessor.py
│   │   │   ├── test_app_logging.py
│   │   │   ├── test_create_sample_data.py
│   │   │   ├── test_create_tracking_id.py
│   │   │   ├── test_dns_query.py
│   │   │   ├── test_line_item.py
│   │   │   ├── test_party_address.py
│   │   │   ├── test_semantic_model.py
│   │   │   ├── test_smp_query.py
│   │   │   ├── test_urn.py
│   │   │   ├── test_urn_hasher.py
│   │   │   └── unaptr_response.json
│   │   ├── urn.py
│   │   └── urn_hasher.py
│   ├── docs
│   │   ├── __init__.py
│   │   ├── _license.md
│   │   ├── accessor.md
│   │   ├── app_logging.md
│   │   ├── artifacts.md
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
│   │   ├── getting_started.md
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
│   │   ├── test_cases.md
│   │   ├── todo.md
│   │   ├── tools_and_resources.md
│   │   ├── urn.md
│   │   ├── urn_handler.md
│   │   ├── urn_hasher.md
│   │   ├── using_the_modules.md
│   │   └── working_with_the_code.md
│   └── mkdocs.yml
├── requirements.txt
└── todo.md

13 directories, 109 files
```

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
