### Example 1 

**Create alias countLine for wc -l and use it**

  ```bash
  alias countLine="wc-l"
  countLine myScript.sh
  7  myScript.sh
  ```

**Delete the alias**

  ```bash
  unalias countLine
  ```
### Example 2 

**Create alias process that displays process in the format ps -f**

  ```bash
  alias process="ps -f | wc -l" 
  process 
  4
  ```

**Delete the alias**

  ```bash
  unalias process
  ```
