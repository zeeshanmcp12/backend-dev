# Backend Development Track

## Python

### Language Jargons

## Chapter 2 - Variables

- Python is dynamically-typed language.
  - A variable can store any type and that type can change later on.
  - It's not a good idea to change the type of variable after we declared it.
  - In Python we can initialized a variable with one type and change it later on to other type
    - x = 5
    - x = "five"
- Some programming languages, for example Go, Rust etc are Static-Type
  - But, there is a concept of "Type inference". For example
    - num := 5 -> In this case, compiler knows the type of variable
    - num = "five" -> is not allowed in golang

### Variable "rule of thumb"

- No Case
  - newvariable = 10
- Camel Case
  - newVariable = 10
- Snake Case
  - new_variable = 10
  - It became a rule of thumb in for language (Python)

### NoneType Variable

- We can declare an empty variable by setting it to `None`
- We do set variable with `None` to use it later
  - Which means if the value of any variable is `None`, it hasn't been set yet

>Note: The None type is not the same as a string with a value of "None":

```
my_none = None # this is a None-type
my_none = "None" # this is a string
```

### String

- "Strings" are raw text in coding speak. They are called string because they are a list of characters "strung" (aik sath juray hoe) together.

### Math with String

- Operators in Python doesn't concatenate with string except '+' `addition` operator.
  - ["Click here to see the example"](./Python/may2023/math-str-concatenate.py)

### Multi-Variable Declaration OR Multiple Variables in Single line

- We can declare as many variable as possible in single line. There is no any limit.
  - sword_name, sword_damage, sword_length = "Excalibur", 10, 200

## Chapter 3 - Computing

### Numbers in Python

- An **Integer** is a number without decimal part (2.3) so a whole number, positive or negative. For example 3, -3 etc
- A **Float** is a number type that allows for decimal values. For example, 3.4
- `Division` in Python will end up with float(ing) number. For example, 3 / 2 -> output: 1.5

#### Floor Division

- **Floor** division is like a normal division except the result is `floored` which means the reminder is removed. It will produce an output in an `Integer` format instead of `Float`. For example, `print(11 // 2) -> Output: 5`
  - In roman
    - Ye normal division ki tarah hi hota hai. Farq sirf itna hai k result qareeb tareen mukammal (whole) number tak puhunch jata hai. Matlab k agar floor division karen 10 ko 3 se divide kar k tu answer ayega `3` kun k `3` (number) 10 main 3 bar (three times) ata hai. Bacha 1, wo remove ho jayega.
- The symbol used to represent the Floor Division is `//` (double forward slash).

### Notes

- **type** function
  - type(any_variable)
- **is** keyword
  - `is` is a keyword in Python that test if two variables refer to the same object. The test returns **True** if the two objects are the same object. The test returns **False** if they are not the same object, even if the two objects are 100% equal.
- clean code
  - Code that is easy for developers to read and understand.

## Object Oriented Programming

## Golang
