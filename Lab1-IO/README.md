# IO

In this lab we are going to explore basic IO both standard streams as well as files.

## 1 Console

### 1.1 Output

Using pi in the math library, print the message "Pi has the value 3.14" to console (make sure that you only print 2 decimals).

### 1.2 Input

Ask the user how many decimals of pi that should be printed, and print it accordingly.

Example run

```
Enter wanted number of decimals: 4
Pi has the value 3.1416
```

## 2 File

### 2.1 Single`tail`

Create a simplified version of the  `tail` command. In other words, create a script that takes a file path as argument and prints the last 10 lines of the file on standard output

_NOTE:_ Do **not** try to make this in a smart way dealing with large files etc unless you fell rather comfortable with Python.

### 2.2 Multi`tail`

Expand the `tail` script to allow for n number of file paths as argument. If more than one is given, the lines from the file should be preceded with a header giving the file path.

### 2.3 Variable lines

Add an option where the user can select the number of lines from each file that should be printed.

### 2.4 Large files (Extra)

If you've gotten this far, then you can try to write a function that can manage very large files.