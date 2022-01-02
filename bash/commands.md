# General Commands

- sh  : command interpreter (shell)
- ls  : list directory contents
- date : today's date and time
- whoami : show user id
- echo : display a line of text
- cat : reading and writing from/to a file
- man : help / reference manuals
- vi : text editor
- nano : text editor
- grep : search for PATTERN in each file


### cat
```
cat <filename> ... <filename_n> : print contents on standard output
cat file1 > file2 : create file2 from file1 ( > input redirection )
cat >> file1 : appending content from standard input
cat file1 >> file2 : appending content to file2 from file1
```

### compiler

```
  gcc : C Compiler
  g++ : C++ Compiler
  g++ --version : output version
  g++ <filename> -o <execname>  : 
      compile C++ <filename> [-o] place output in file <execname> ; if no -o, the output is placed by default in <a.out>

  example : 
  
  $g++ helloworld.cpp -o exec.cpp 
  $./exec.cpp : run the compiled version of helloworld.cpp
```
