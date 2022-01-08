# Bash

Bash is a Unix shell and command language written by Brian Fox for the GNU Project as a free software replacement for the Bourne shell. First released in 1989, it has been used as the default login shell for most Linux distributions. A version is also available for Windows 10 via the Windows Subsystem for Linux. It is also the default user shell in Solaris 11. Bash was also the default shell in all versions of Apple macOS prior to the 2019 release of macOS Catalina, which changed the default shell to zsh, although Bash remains available as an alternative shell.

Bash is a command processor that typically runs in a text window where the user types commands that cause actions. Bash can also read and execute commands from a file, called a shell script. Like most Unix shells, it supports filename globbing (wildcard matching), piping, here documents, command substitution, variables, and control structures for condition-testing and iteration. The keywords, syntax, dynamically scoped variables and other basic features of the language are all copied from sh. Other features, e.g., history, are copied from csh and ksh. Bash is a POSIX-compliant shell, but with a number of extensions.

The shell's name is an acronym for Bourne Again Shell, a pun on the name of the Bourne shell that it replaces and the notion of being "born again".

A security hole in Bash dating from version 1.03 (August 1989), dubbed Shellshock, was discovered in early September 2014 and quickly led to a range of attacks across the Internet. Patches to fix the bugs were made available soon after the bugs were identified. 

source : https://en.wikipedia.org/wiki/Bash_(Unix_shell)



##### Using Loops and Conditional Execution

    #!/bin/sh
    read number
    counter=1
    while [ $counter -le 10 ]
    do
        multiply=$((number*counter))
        echo "$number x $counter = $multiply"
        counter=$(($counter+1))
    done

### [Shell Programming]()

Course Topics

    1. Linux and Shell Basics
    1.1. Introduction to Linux and Shell
    1.2. Installing and Configuring
    1.3. Writing Basic Commands and Scripts
    1.4. Reading and Writing a File
    1.5. Handling Files and Directories
        1.5.1. Navigating Directories
        1.5.2. Copy Files and Directories
        1.5.3. Rename/Move Files and Directories
        1.5.4. Delete Files and Directories
    1.6. Input and Output Formatting
        1.6.1. Formatting Output
        1.6.2. Pipe Operators
        1.6.3. Input Redirection
    
    2. Processes, Utilities, and Shell Programming Constructs
    2.1. File Attributes and Permissions
        2.1.1. File Types and Named Pipes
        2.1.2. Permissions
        2.1.3. Handling Ownership
    2.2. Handling Processes
        2.2.1. Handling Processes
        2.2.2. Scheduling Jobs
    2.3. Shell Variables
    2.4. Expression Substitution
    2.5. Quoting
    2.6. Conditional Execution
    
    3. Moving Ahead with Shell Programming
    3.1. Loops
    3.1.1. Introduction and While Loop
    3.1.2. For loop and More
    3.2. Functions
    3.2.1. Introduction to Functions
    3.2.2. Scope of a Variable and Return in Functions
    3.3. Shell Utilities
    3.3.1. Sort, cut and grep commands
    3.3.2. The sed command
    3.3.3. Displaying File Contents
    3.3.4. Finding Files and Directories
    
    4. Shell Scripts and Other Utilities
    4.1. Working with awk
    4.2. Process Monitoring
    4.3. Networking Utilities
    
