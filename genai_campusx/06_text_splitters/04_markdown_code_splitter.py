
# python code splitter

from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
# Python Code with Explanation

## Problem Statement

Write a brief description of the problem or task your Python code is solving.

---

## Python Code

```python
# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Input values
num1 = 10
num2 = 20

# Function call
result = add_numbers(num1, num2)

# Print output
print("Sum:", result)
```

---

## Code Explanation

### 1. Function Definition

```python
def add_numbers(a, b):
```

* `def` is used to define a function in Python.
* `add_numbers` is the function name.
* `a` and `b` are input parameters.

---

### 2. Return Statement

```python
return a + b
```

* The `return` keyword sends the result back to the caller.
* Here, the function returns the sum of `a` and `b`.

---

### 3. Variable Initialization

```python
num1 = 10
num2 = 20
```

* Two variables are created and assigned integer values.

---

### 4. Function Call

```python
result = add_numbers(num1, num2)
```

* The function is called with `num1` and `num2` as arguments.
* The returned value is stored in the `result` variable.

---

### 5. Output Display

```python
print("Sum:", result)
```

* The `print()` function displays the final result on the console.

---

## Sample Output

```text
Sum: 30
```

---

## Key Concepts Used

* Functions
* Parameters and Arguments
* Return Statement
* Variables
* Print Function

---

## Time Complexity

* **Time Complexity:** `O(1)`
* **Space Complexity:** `O(1)`

---

## Conclusion

This program demonstrates how to create and use functions in Python to perform simple operations efficiently.

"""

# initialize the splitter
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=400,
    chunk_overlap=0,
)

# perform the split
chunks = splitter.split_text(text)

print(f"length of chunk: {len(chunks)}")
print(f"chunk content: {chunks[0]}")

