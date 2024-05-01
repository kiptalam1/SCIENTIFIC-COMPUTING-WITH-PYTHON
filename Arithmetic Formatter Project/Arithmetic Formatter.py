def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_line = []
    bottom_line = []
    dash_line = []
    answer_line = []

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        # Check for valid operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if operands are digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if operands have more than four digits
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the maximum length among the operands
        max_length = max(len(operand1), len(operand2))

        # Append formatted strings to each line list
        top_line.append(operand1.rjust(max_length + 2))
        bottom_line.append(operator + operand2.rjust(max_length + 1))
        dash_line.append("-" * (max_length + 2))

        # Calculate the answers if needed
        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            answer_line.append(answer.rjust(max_length + 2))

    # Combine all lines
    arranged_problems = "    ".join(top_line) + '\n' + "    ".join(bottom_line) + '\n' + "    ".join(dash_line)

    if show_answers:
        arranged_problems += '\n' + "    ".join(answer_line)

    return arranged_problems

# Test cases
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
