# Sample git workflow<hr/>

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


