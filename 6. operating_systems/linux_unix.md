# Unix / Linux

### [Bash : Unix shell and command language](https://github.com/CatalaniCD/computer_science/tree/main/6.%20operating_systems/bash)

### [C++](https://github.com/CatalaniCD/computer_science/tree/main/6.%20operating_systems/cpp)

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
 
## File System
* Organized hirarchically as a tree
* Ability to create and delete files / directories
* Grow dynamically
* Devices / Directories / Files are all treated as files
* Protection of data

![file system](https://github.com/CatalaniCD/computer_science/blob/main/6.%20operating_systems/file_system.png)


## File Internal Representation : Inodes
* Data structure in file system that describes a file-system object such as a file or a directory
* Each inode stores the attributes and disk block locations of the object's data : ls -i
* File-system object attributes may include metadata (times of last change, access, modification), as well as owner and permission data
* Each file is associated with an inode, which is identified by an integer, often referred to as an i-number or inode number
* POSIX standard description for an inode : stat <filename>
  
![inode](https://github.com/CatalaniCD/computer_science/blob/main/6.%20operating_systems/ext2_inode.png)
  
 ## Inode Composition 
* file -> Inode 
* Block Size : 512 bytes
* Block number address : 32 bits
* Direct addressing : 12 * 512 bytes (6 Kb) -> 12 indexes entries to Direct Data Blocks
* Single addressing : 128 * 512 bytes (64 Kb) -> index n 13, to 128 pointers
* Double addressing : 128 * 128 * 512 bytes (8 Mb) ->  index n 14, to 128 pointers, to 128 pointers each one
* Triple addressing : 128 * 128 * 128 * 512 bytes (1 Gb) -> index n 15, to 128 pointers, to 128 pointers each one, to 128 pointers each one    
  
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
