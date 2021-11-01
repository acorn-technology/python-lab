# Data types

In this labs we are going to write some basic algorithms, and while doing that we will learn how to work with the built in data types in Python.

Keep in mind that Python has more built in data types than just strings, numbers and lists.

* Boolean
  * bool
* Numeric
  * int
  * float
  * complex
* Sequence
  * str
  * list
  * tuple
  * range
* Mapping
  * dict
* Set
  * set
  * frozenset
* Binary
  * byte
  * bytearray
  * memmoryview

## 1 Text statistics

_Note:_ All of the tasks in this section are meant to have the file `acorn-system-development.txt` as input.

## 1.1 Basic stats

Read the input file and write the number if characters and number of words.

Example output:
```
Number of characters: 1868
Number of words: 290
```

## 1.2 Word count

Count the number of occurences for each word in the file sorted by the number of occurences.

Example output:
```
and: 17
of: 15
to: 11
the: 9
we: 8
...
```

## 1.3 Search

Take a string as input and print all the words that are containing that string.

_Note:_ Try solving it with [list comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) (e.g `[x.lower() for x in data]`)

Example output for "res":
```
architectures
irrespective
present
representing
```

## 1.4 Regular Expressions

Expand the word search to support regular expressions as input

# 2 Triangles

_Note:_ This task has been stolen from [Advent of code](https://adventofcode.com), but don't go looking for solutions just yet ;)

## 2.1 Part one

The file `triangle-input.txt` contain specifications of triangles. Each line contains the lenght of each of the three sides. Although something has gone worng, some are not valid triangles.

Check how many of the triangles follow the basic rule that the sum of any two sides, must be larger than the remaining side?

## 2.2 Part two

It seems that we have been reading the input in the wrong way. It is not a triangle per row but they are instead in a single column spreading over three rows

```
t1 t2 t3
t1 t2 t3
t1 t2 t3
t4 t5 t6
t4 t5 t6
...
```

Check how many of the triangles are valid when read in this manner.
