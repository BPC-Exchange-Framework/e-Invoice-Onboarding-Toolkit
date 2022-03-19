# Jupyter Notebooks on Google Colab<hr/>


## Colab Sandboxes

[JupyterLab](https://jupyter.org/) is a sandbox development environment which allows for, among other things, rapid prototyping or testing of small units of code.  They provide a framework to execute code without building a whole application or even a complete module.

Most of the code already incorporated into the project started out in a JupyterLab runtime environment.  

JupyterLab is also useful for introspection of a piece of code.  

JupyterLab artifacts worked on for the project are stored as static documents in GitHub in the E-Invoice-Onboarding-Toolkit project under ./einvoice/docs/jupyterlab.  

[Google Colab](https://colab.research.google.com/) pages implement [JupyterLab ](https://jupyter.org/) runtime with live sandbox environments.  Pages can be linked from the E-Invoice-Onboarding-Toolkit  GitHub repository, or pulled from the repository and saved locally by anyone with a Google account.  


### URN hashing and DNS NAPTR lookup.
The Colab JupyterLab Notebook with examples of how to hash the specification, the schema_id, and the party_id to create the URN and perform the NAPTR DNS query is at this [Colab page](https://colab.research.google.com/drive/1kfMedMUapeaOS6u9hnS8IcmQaury8znP?usp=sharing).  Examples 6, 7, 8,  and 9 run the hash and submit against a DNS in real-time.  
The JupyterLab file is: __urn_hash_work.ipynb__.


## SMP query
The Colab JupyterLab Notebook page with examples of how to transform the URN and party_id and submit it to the SMP URI is at this [Colab page](https://colab.research.google.com/drive/14EVSc0GyjU0H9776UEXqoEoD3x5Kn2RV?usp=sharing).  
They JupyterLab Notebook file is: __smp_url_transformations.ipynb__.


## ebMS Message Header validation
The Colab JupyterLab Notebook  pages with examples of reading an XSD file and validating an XML file has two Google Colab pages for different aspects of the work.  
Inspection and validation of the XSD file has this [Google Colab Page](https://colab.research.google.com/drive/1zuPcP1ofEe8PReew9KbGY13EQJsNN8Es?usp=sharing).
The JupyterLab file is: __ebMS XML 3 schema.ipynb__.

Validation of an xml file against the XSD is done using this [Google Colab Page](https://colab.research.google.com/drive/1ExMZUD_5larW0wEuGJ5erHkFuoozcLCF?usp=sharing)
The JupyterFile is: __Validate_bdx-as4.ipynb__.

For ease of access these files are copies stored on the drive of one of the project Developers and is free and open to anyone to view and run.   Interested individuals should make copies of the Labs for themselves and run on Google Colab under their own account or an instance of JupytyerLab running on Anaconda, VS Code, or a Python install.

