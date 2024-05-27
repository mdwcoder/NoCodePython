# MDW NoCodePython

Are you tired of watching countless tutorials and not learning Python?  
Are you tired of not having an easy way to learn?  

With **NoCodePython**, that's over. This program is easy to use and designed for beginners who want to start practicing without having to learn the basics first. With **NoCodePython**, you can create your own applications and scripts without needing to know how to code in Python, you just need to use natural language.

**NoCodePython** is not made to replace the traditional programming system but serves to transform natural language into code, allowing you to experiment and learn logic more quickly.

## What can you do with **NoCodePython**?

Currently, the development is limited to the use of base Python, without additional libraries. However, development continues and it is not known how far it will go.

## How to program with **NoCodePython**?

**NoCodePython** has its own syntax but tries to be as natural as possible.

### Current Syntax

**Note:**  
There are specific expressions for strings, such as `print <text to print>`, which will only print the text regardless of whether it has quotes; in fact, it should not have them. On the other hand, in `concatenate textA with textB into VariableStore` it is necessary that if `textA` or `textB` are not variables, they should be surrounded by quotes.

### Variable Declaration

To store a variable, you must give it content and a name.

Examples:
```
store "content" in variableName
store 10 in age
```

### Using Variables

Example:
```
store 23 in number1
add number1 with 23 into result
```

### Print to Console

There are two modes: variables and strings.

- `print variable`: will print the content of the variable.
- `print`: will print whatever you input as a string.

Examples:
```
print Hello world
store "Hello World" in string
print variable string
```

### Operations

Operations can be done as follows:

Example:
```
add 23 with 21 into result
```
(It will store the result in the `result` variable).

For other operations, it's the same with their respective names:
- add
- subtract
- multiply
- divide
- raise (to exponentiate something)
- root (to find the root of something)

### Working with Text

To concatenate text we use `concatenate`.

Example:
```
concatenate "content1" with "content2" into result
```
(It will store the result in the `result` variable).

### Conditionals

Conditionals work in a single line with commas. Let's see some examples:

```
store 1 in number
if 1 equals number, then print It is equal, store equal in how_is
```

```
store 2 in number
if 3 is less than number, then print It is less, else print It is greater
```

### Loops

We have several types of loops, starting with the easiest ones.

Repeat something `n` times.

Example:
```
repeat 32 times print 23
```
(It would print `23` 32 times).

Another example:
```
store 0 in counter
repeat 10 times add 1 to counter into counter
print counter
```

It is obvious that this code needs optimization, but this is version 0.1.1v, so it is possible that there are errors as well as optimization failures.

Another type is while something happens, do something.

```
store 0 in counter
while counter is less than 10, do print It is less, add 1 to counter into counter
```

There is another type that iterates over lists but still presents errors, for now, we have these two.

### Operators

There is not much to explain about the operators, they are just these:

- equals
- is different from
- is greater than
- is less than
- is greater or equal to
- is less or equal to
```