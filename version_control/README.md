# Intro to Version Control and Git

## Version Control System

### What is a Version Control System (VCS)
* A system which track/manage/save/record changes to a file or a set of files over time, so that we can recall a specific version later 

### Benefits
* Revert changes for a file or all the files back to specific version
* Compare changes over time
* See who made changes and when 
* Able to accept changes 


### Types of version control
*
#### What is manual version control
* Such as when you make a copy of a file(s) or folder with a name like v1.1 v1.2

#### How did early version control systems work
* Tracked changes to indvidual files
* base file was saved, then each version saved a delta
* To get the latest version, had to us ebase file + all deltas

#### Centralised VCS vs Distributed VCS like Git
> see diagram
> * centralised: 
> * distributed: 
## Local Version Control with Git
*
### What is stored in each version of a file that changes



### Does Git need to be used as a distributed VCS
* no but its most beneficial as a distributed VCS

### What does Git store in a 'commit'
* * Stores the snapshot of the whole file that has been changed
* if a file isn't part of a commit there will still be a reference link to the latest commit for that specific file 
### The three states in Git
* 
### Where does Git store its information
* .git folder 
### Common workflow of Git commands
* turn a normal folder into a git repo: `git init`
* save changes to a group of files
  1. stage the files: git add . 
  2. commit the changes: `git commit -m "appropriate git message`