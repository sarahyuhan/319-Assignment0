### Homework Assignment: Advanced Calculator with CSV Support

**Objective:** In this assignment, you'll create a calculator program that reads operations and operands from CSV files,
performs the operations, and saves the result to another CSV file. Furthermore, the program will maintain a history of
all operations and results.

**1. Overview:**

Your program will consist of:

- A `Calculator` class that supports basic arithmetic operations.
- A `CSVCalculatorHandler` class responsible for:
  - Processing one or multiple CSV files.
  - Storing the history of all the operations.
  - Exporting the history to a specified CSV file.

---

**2. Program Specifications:**

- **Input Format:** A set of CSV files, each CSV file will contain multiple rows. Each row will have between 1 to n numbers (both
  integers and floats) followed by an operation (e.g., `add`, `subtract`, `multiply`, `divide`, `exponentiate`). The
  operation will determine what the calculator should do with the preceding numbers. For instance:

  ```
  5.2, 10.3, add
  8, 2, divide
  2, 3, exponentiate
  ```

  It is possible that some lines have invalid operators, not enough operands, too many operands etc. All operators require at least two
  operands. You will need to handle these errors, more details in later section.

- **Output Format:** For each input CSV file, an output CSV file should be generated containing two columns: the result
  of the operation and an error code. The filename should be constructed as follows `output_n.csv` where `n` is the index of the file from the original input parameters given. This means that `n` will range from `0` to `(k-1)` where `k` is the total number of input files (since we use array style indexing).

- **History Output Format:** Each line from each input file should be saved to a history file that contains all the relevant information. The required columns are, `input_file,operation,result,error`. See below sections for an example.

- **Output Ordering**:
  All output should be saved/recorded in the same order as the input. Thus, line `n` of the input file should be line `n` of the output file. For this history file this means you should have all lines of file 1 before lines of file 2 etc.

- **Error Codes**:
  Below is a table of error codes, your program is expected to categorize and record errors according to this table.

  | Error                | Code |
  | -------------------  | ---- |
  | No Error             | 0    |
  | Division by Zero     | 1    |
  | Bad Number of Params | 2    |
  | Unknown Operator     | 3    |
  | Unknown Error        | 4    |

- **Operator Specifications**:
  - **Addition:** The result of adding all the numbers together. Supports any number of operands greater than 2.
  - **Subtraction:** The result of subtracting all the numbers from the first number. Supports any number of operands greater than 2.
  - **Multiplication:** The result of multiplying all the numbers together. Supports any number of operands greater than 2.
  - **Division:** The result of dividing the first number by the second number. Supports only two operands.
  - **Exponentiation:** The result of raising the first number to the power of the second number. Supports only two operands.
---

**3. Requirements:**

### **a. `Calculator` Class:**

#### **Stub:**

```python
class Calculator:
   # Your functions for basic calculations.
   # IE, one for add, subtract etc
```

#### **Specifications:**

- Each method should take a variable number of arguments and return the result of the arithmetic operation.
- Handle potential exceptions gracefully. For instance, division by zero. In addition, these errors should be correctly
  reported in the CSV export of the operation.

### **b. `CSVCalculatorHandler` Class:**

#### **Stub:**

```python
class CSVCalculatorHandler:
    def __init__(self):
        pass

    def process_csv(self, filenames, output_prefix="output"):
        pass

    def save_to_history(self, filename, operation, result, error_code):
        pass

    def history_export(self, export_filename):
        pass
```

#### **Specifications:**

- **process_csv:** This method should read each CSV file provided in the `filenames` list, calculate results using
  the `Calculator` class, and save the results to a new CSV file prefixed with `output_prefix`. Each input file should have exactly one output file.

- **save_to_history:** After processing each row in the input CSV, this method should save details about the operation,
  its result, and any errors to the history of the `CSVCalculatorHandler` class. The history should be stored on the class and not saved to a file until the user calls the `history_export()` function.

- **history_export:** This method should export the entire history of operations, results, and errors to a CSV file
  specified by `export_filename`.

---

**4. Example:**

Below is an example input and output:

File name: `input.csv`

```
5,10,add
8,2.5,3.5,multiply
7,3,subtract
9,0,divide
2,3,exponentiate
10,divide
10,2,unknown_operator
```

File name: `output_0.csv`

```
result,error
15.0,0
70.0,0
4.0,0
,1
8.0,0
,2
,3

```

File name: `history.txt`

```
input_file,operation,result,error
input.csv,"5,10,add",15.0,0
input.csv,"8,2.5,3.5,multiply",70.0,0
input.csv,"7,3,subtract",4.0,0
input.csv,"9,0,divide",,1
input.csv,"2,3,exponentiate",8.0,0
input.csv,"10,divide",,2
input.csv,"10,2,unknown_operator",,3

```

**5. Submission:**

After implementing the two classes, write a main block of code that demonstrates the functionality of your classes by:

1. Processing CSV files provided via program arguments. The list of file names will be provided to your program via arguments. At least one file will always be provided.
2. Exporting the history to a CSV after all files have been processed. The output name should be exactly `history.txt` no other name will be acceptable.
3. Your code must have a main method so that it is executable from the command line

Our test system will run your code with a command similar to the following:

```shell
python3 CSVCalculatorHandler.py file_name_1.csv file_name_2.csv file_name_2.csv
```

The number of file names will vary from `1->n` and thus your program should be able to handle this. See [this](https://machinelearningmastery.com/command-line-arguments-for-your-python-script/) link for some ways to parse arguments to your python code.

You're required to include:

- Inline comments explaining your logic.
- Proper error handling for invalid inputs and operations.

NOTE: Please upload only the files `Calculator.py` and `CSVCalculatorHandler.py`. Please don't upload them inside a directory or the Autograder won't run correctly.

---

**5. Tips and Guidance:**

- Remember to handle floating-point numbers in your operations.
- Think about the edge cases, such as division by zero.
- Consider utilizing Python's built-in libraries like `csv` for easier CSV file processing.

---

**6. Evaluation Criteria:**

Your assignment will be graded based on:

- Correctness and completion of the functionality.
- Code readability and organization.
- Handling of edge cases and potential exceptions.

---

Best of luck, and happy coding!

---
