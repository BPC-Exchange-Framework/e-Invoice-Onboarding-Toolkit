# Questions...
<hr>
__Q:__
: Who is the audience for this project?   

__A:__  
: This software is intended for those interested in participating as service endpoints in a Four-Corner Model framework. The code to implement in the repository is written in the Python programing language. Other toolsets to facilitate the initiative such as Markdown or Docker may also be incorporated where appropriate.     

<hr>

__Q:__
: What do I need in order to use this code?  

__A:__
: __Python__  
  1. Some knowledge of Python  
  2. Python 3.6 or greater, _Python 3.10 or greater is recommended._.  

<hr>
__Q:__
: Does this code provide a full end-to-end solution to process an e-invoice?  

__A:__  
: This code answers some very domain specific questions regarding e-invoice functionality in a Four-Corners Model framework.  
_Specifically it's helpful with:_  
1. The hashing functionality to derive the urn for look-up in a DNS NAPTR record.  
2. How to do the DNS NATPR lookup and extract the relevant SMP URI.  
3. How to construct the two REST requests to an SMP server to retrieve a Corner 3 URI.  
4. How to execute the REST requests to the SMP server.  
5. How to extract the Corner 3 endpoint URI from the response from the SMP server.    
6. Validating an e-Invoice ebXML message header for compliance with an AS4 conformance profile.  

<hr>


__Q:__

:   How do I use the code?  

__A:__
: There are a number of ways the code can be examined or worked with:  
1. [Start to finish example of the  URI discovery process](./start_to_finish.md).  
2. [Test Cases](./test_cases.md) which demonstrate functionality of the modules.  
3. Jupyter Notebook sandbox environments at [Google Colab Pages](./google_colab_pages.md) which isolate and demonstrate the code in a sandbox.  
4. Package/Library API see the [Index](./index.md) for links to the code API on the modules themselves.  
5. Integration of an example discovery process implemented in a [Flask application on a Docker container](./flask_integration_on_docker.md) (forthcoming).  




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
