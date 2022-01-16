# Unix / Linux

### [Bash : Unix shell and command language](https://github.com/CatalaniCD/computer_science/tree/main/6.%20operating_systems/bash)

## Unix
* Birth : 1970, AT&T Labs, led by Kenneth Thompson and Dennis Ritchie
* Written in high level language, typically C
* Easy to read and understand
* Power to provide services in a Simple Way
* Build complex programs from simple ones
* Hierarchical file system with efficient implementation
* Support different file systems
* Every device is treated as a file

## GNU / Linux
* GNU is a recursive acronim for  "GNU's Not Unix"
* Open Source System ( GPL Licence )
* Developed from a scratch, using the same principles of unix
* GNU Open Source developement started in 1984, Free Software Foundation (FSF) by Richard Mathew Stallman
* Developed central components, forming largest single contribution to the whole system
* Linus Torvalds wrote Linux in 1991 and contributed to the Free Software Foundation (FSF) Community, as part of an academic project
* Many distributions / flavors
  ```
  - Ubuntu
  - Debian
  - Fedora
  ```
 
## [File System]
* Organized hirarchically as a tree
* Ability to create and delete files / directories
* Grow dynamically
* Devices / Directories / Files are all treated as files
* Protection of data

![linux arch](https://github.com/CatalaniCD/computer_science/blob/main/6.%20operating_systems/file_system.png)


## [File Internal Representation : Inodes]()


## Architecture of a Linux System
* System divided in layers

![linux arch](https://github.com/CatalaniCD/computer_science/blob/main/6.%20operating_systems/linux_arch.png)

* Linux kernel communicates with the hardware ( OS -> Hardware )
* Shell (and other) interact with the kernel, don't have direct access to hardware
* Outermost layer can build on top of the low level programs

## Shell
* Command Line Interpreter
* Uses terminal / console
* Interacts with kernel
* Execute commands and scripts

## Applications
* Day to day usage
* Cron jobs (automating tasks) - i.e. backup everynight
* Package installation
* Cloud automation and cloning systems
* Creating system images in the cloud
* Database migrations
* System Monitoring
* Automating the build process
* Running files in batch mode
* Link various programs using pipes and filters
* Scheduling and executing system tasks

## Users
* Users
* Programmers
* System Administrators
