import CSV
import os

class CSVCalculatorHandler:
    def __init__(self):
        self.history = []
        self.calculator = Calculator()

    def process_csvs(self, filenames, output_prefix="output"):
        for filename in filenames:
            if not os.path.isfile(filename):
                continue
            with open(filename, 'r') as file:
                reader = CSV.reader(file)
                for row in reader:
                    if len(row) < 3:
                        continue
                    operation = row[0].strip().lower()
                    numbers = list(map(float, row[1:]))

                    try:
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
                            self.save_to_history(filename, operation, None, "Unknown operator")
                            continue
                        self.save_to_history(filename, operation, result, None)
                    except ValueError as e:
                        self.save_to_history(filename, operation, None, str(e))

                    output_data.append([result, error_code])
                    self.save_to_history(filename, operation, result, error_code)

            # Save output CSV
            output_filename = f"{output_prefix}_{index}.csv"
            with open(output_filename, 'w', newline='') as out_file:
                writer = csv.writer(out_file)
                writer.writerow(["result", "error"])  # add headers
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
