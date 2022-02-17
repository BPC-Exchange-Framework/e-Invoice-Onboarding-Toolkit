# Project Home

## Welcome
__Welcome to the e-Invoice Onboarding Toolkit__  

This is a repository for open source software tools created to facilitate market adoption of e-invoices implemented conformant with the Four-Corner interoperability model framework.   

???+ Important "Outcomes"
    1. Hashing functionality to derive the urn for look-up in a DNS NAPTR record.  
    2. DNS NATPR lookup and extract the relevant SMP URI.  
    3. Two REST requests to an SMP server to retrieve a Corner 3 URI.  
    4. Execute the REST requests to the SMP server.  
    5. Extract the Corner 3 endpoint URI from the response from the SMP server.    
    6. Validate an e-Invoice ebMS message header for compliance with an AS4 conformance profile.  

For information about e-invoices and implementing the Four-Corner Model please visit the [Business Payments Coalition website](https://businesspaymentscoalition.org/electronic-invoices).  

 Additional documentation, reference materials, and standards can be found on the [Oasis-Open.org website](https://www.oasis-open.org). Start with the [ebXML specification](http://docs.oasis-open.org/ebxml-msg/ebms/v3.0/core/os/ebms_core-3.0-spec-os.html)

## This Project

* [Project Home](./index.md)
* [FAQ](./faq.md)
* [Outcomes](./outcomes.md)
* [Assumptions](./assumptions.md)
* [Tools and Resources](./tools_and_resources.md)
* [Configure a Python Environment](./python_dev_env.md)
* [Package Requirements](./requirements.md)
* [Getting the Code](./working_with_the_code.md)
* Using the Code
    * [Using the Modules](./using_the_modules)
    * [Test Cases](./test_cases.md)
    * [Start-to-Finish example](./start_to_finish.md)
    * [JupyterLab/Notebooks](./google_colab_pages.md)
* [Infrastructure Components](infrastructure_components.md)
* [Project Roadmap](./project_roadmap.md )
* [Project Artifacts](./artifacts.md)
* [Workflow](./git_workflow.md)
* [Oasis Resources](./oasis_documentation.md)
* [License](./_license.md)

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
