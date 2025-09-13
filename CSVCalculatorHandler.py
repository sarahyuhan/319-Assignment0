import csv
import os
from Calculator import Calculator

class CSVCalculatorHandler:
    def __init__(self):
        self.history = []
        self.calculator = Calculator()

    def process_csvs(self, filenames, output_prefix="output"):
        for index, filename in enumerate(filenames):
            output_data = []  # ✅ Define here for each file

            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if not row:
                        continue
                    try:
                        numbers = list(map(float, row[:-1]))
                        operation = row[-1].strip().lower()

                        result = None
                        if operation == "add":
                            result = self.calculator.add(numbers)
                        elif operation == "subtract":
                            result = self.calculator.subtract(numbers)
                        elif operation == "multiply":
                            result = self.calculator.multiply(numbers)
                        elif operation == "divide":
                            if len(numbers) != 2:
                                raise ValueError("Bad number of params")
                            result = self.calculator.divide(numbers[0], numbers[1])
                        else:
                            raise ValueError("Unknown operation")

                        error_code = 0

                    except Exception as e:
                        result = None
                        error_code = 1

                    output_data.append([result, error_code])
                    self.save_to_history(filename, operation, result, error_code)

            output_filename = f"{output_prefix}_{index}.csv"
            with open(output_filename, 'w', newline='') as out_file:
                writer = csv.writer(out_file)
                writer.writerow(["result", "error"])
                writer.writerows(output_data)

    def save_to_history(self, filename, operation, result, error_code):
        self.history.append({
            'input_file': filename,
            'operation': operation,
            'result': result,
            'error': error_code
        })

    def history_export(self, export_filename):
        with open(export_filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['input_file', 'operation', 'result', 'error'])
            writer.writeheader()
            writer.writerows(self.history)


if __name__ == '__main__':
    input_file = ['input.csv']
    calculator = CSVCalculatorHandler()
    calculator.process_csvs(input_file)
    calculator.history_export('history_export.csv')
