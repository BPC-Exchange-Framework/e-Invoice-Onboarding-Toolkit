## Sample git workflow<hr/>

### A minimal git "script" to work with the code.

This is a sample workflow of a very rudimentary process to create a branch in Github, add code, and push up to the repo on Github.  

1. Create a new branch:   
      ```git checkout -b <insert branch name here`>```   
2. Implement your changes
3. Add into the repo:  
      ```git add .```   
      ```git commit -m <your comment here>```   
      ```git push```   
   :pushes your changes up to the remote branch  
4. Either create a pull request in Github, or:  
      ```git checkout main```  
      ```git merge <branch you want to merge here>```   
      ```git push```  to push main changes up to remote branch



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