# Debugger Exercise 1

1. Copy the file pdb_ex1.py (in this directory) to your host. In this program add the following somewhere in the middle of your program:

```
import pdb
pdb.set_trace()
```

2. Execute your program and verify that you drop into the debugger.
    1. List 10 or more lines around your current point.
    2. Execute next three times.
    3. Print out a variable in your program
    4. Execute !my_var = 72 and verify this variable is now set in your program using 'p my_var'.
    5. Set a breakpoint ahead of your current point. Use 'continue' to execute and verify you are now stopped at the breakpoint.
    6. Use 'step' to descend down into a function call. Once in the function use 'up' to go up the stack once and 'down' to descend back down the stack once.
    7. Use 'args' to see the arguments that were passed into the function.
    8. Use 'q' to exit the debugger.
