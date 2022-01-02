DASH(1)                                                              BSD General Commands Manual                                                             DASH(1)

NAME
     dash — command interpreter (shell)

SYNOPSIS
  
     dash [-aCefnuvxIimqVEbp] [+aCefnuvxIimqVEbp] [-o option_name] [+o option_name] [command_file [argument ...]]
     dash -c [-aCefnuvxIimqVEbp] [+aCefnuvxIimqVEbp] [-o option_name] [+o option_name] command_string [command_name [argument ...]]
     dash -s [-aCefnuvxIimqVEbp] [+aCefnuvxIimqVEbp] [-o option_name] [+o option_name] [argument ...]

DESCRIPTION
     dash is the standard command interpreter for the system.  The current version of dash is in the process of being changed to conform with the POSIX 1003.2 and
     1003.2a specifications for the shell.  This version has many features which make it appear similar in some respects to the Korn shell, but it is not a Korn
     shell clone (see ksh(1)).  Only features designated by POSIX, plus a few Berkeley extensions, are being incorporated into this shell.  This man page is not
     intended to be a tutorial or a complete specification of the shell.

   Overview
     The shell is a command that reads lines from either a file or the terminal, interprets them, and generally executes other commands.  It is the program that is
     running when a user logs into the system (although a user can select a different shell with the chsh(1) command).  The shell implements a language that has
     flow control constructs, a macro facility that provides a variety of features in addition to data storage, along with built in history and line editing capa‐
     bilities.  It incorporates many features to aid interactive use and has the advantage that the interpretative language is common to both interactive and non-
     interactive use (shell scripts).  That is, commands can be typed directly to the running shell or can be put into a file and the file can be executed directly
     by the shell.

   Invocation
     If no args are present and if the standard input of the shell is connected to a terminal (or if the -i flag is set), and the -c option is not present, the
     shell is considered an interactive shell.  An interactive shell generally prompts before each command and handles programming and command errors differently
     (as described below).  When first starting, the shell inspects argument 0, and if it begins with a dash ‘-’, the shell is also considered a login shell.  This
     is normally done automatically by the system when the user first logs in.  A login shell first reads commands from the files /etc/profile and .profile if they
     exist.  If the environment variable ENV is set on entry to an interactive shell, or is set in the .profile of a login shell, the shell next reads commands from
     the file named in ENV.  Therefore, a user should place commands that are to be executed only at login time in the .profile file, and commands that are executed
     for every interactive shell inside the ENV file.  To set the ENV variable to some file, place the following line in your .profile of your home directory

           ENV=$HOME/.shinit; export ENV

     substituting for “.shinit” any filename you wish.
