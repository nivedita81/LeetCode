import operator


def romanToInt(s: str) -> int:
    if not s:
        return 0
    numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    n = len(s)
    total = numerals[s[n - 1]]
    for i in range(n - 1, 0, -1):
        curr_num = numerals[s[i]]
        prev_num = numerals[s[i - 1]]
        if prev_num < curr_num:
            total = total - prev_num
        else:
            total = total + prev_num
    return total


def calc(s):
    def compute(operands, operators):
        right, left = operands.pop(), operands.pop()
        operands.append(ops[operators.pop()](left, right))

    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}
    precedence = {'+': 0, '-': 0, '*': 1, '/': 1}
    operands, operators, operand = [], [], 0
    for i in range(len(s)):
        if s[i].isdigit():
            operand = operand * 10 + int(s[i])
            if i == len(s) - 1 or not s[i + 1].isdigit():
                operands.append(operand)
                operand = 0
        elif s[i] == '(':
            operators.append(s[i])
        elif s[i] == ')':
            while operators[-1] != '(':
                compute(operands, operators)
            operators.pop()
        elif s[i] in precedence:
            while operators and operators[-1] in precedence and \
                    precedence[operators[-1]] >= precedence[s[i]]:
                compute(operands, operators)
            operators.append(s[i])
    while operators:
        compute(operands, operators)
    return operands[-1]
#     operands, operators = [], []
#     operand = ""
#     for i in reversed(range(len(s))):
#         if s[i].isdigit():
#             operand += s[i]
#             if i == 0 or not s[i - 1].isdigit():
#                 operands.append(int(operand[::-1]))
#                 operand = ""
#         elif s[i] == ')' or s[i] == '*' or s[i] == '/':
#             operators.append(s[i])
#         elif s[i] == '+' or s[i] == '-':
#             while operators and \
#                     (operators[-1] == '*' or operators[-1] == '/'):
#                 compute(operands, operators)
#             operators.append(s[i])
#         elif s[i] == '(':
#             while operators[-1] != ')':
#                 compute(operands, operators)
#             operators.pop()
#
#     while operators:
#         compute(operands, operators)
#
#     return operands[-1]
#
#
# def compute(operands, operators):
#     left, right = operands.pop(), operands.pop()
#     op = operators.pop()
#     if op == '+':
#         operands.append(left + right)
#     elif op == '-':
#         operands.append(left - right)
#     elif op == '*':
#         operands.append(left * right)
#     elif op == '/':
#         operands.append(left / right)


def solution(exp):
    temp_s = ""
    st = []
    text = ""
    if len(exp) == 0:
        return 0
    for i in range(len(exp)):
        if i < len(exp) and (
                exp[i] == "(" or exp[i] == ")" or exp[i] == "+" or exp[i] == "-" or exp[i] == "*" or exp[i] == "/"):
            while len(st):
                if st:
                    st = st[::-1]
                    text += st.pop()
            if text:
                val = romanToInt(text)
                text = ''
                temp_s += str(val)
            temp_s += exp[i]
        else:
            st.append(exp[i])
    if i == len(exp):
        while len(st):
            if st:
                st = st[::-1]
                text += st.pop()
        if text:
            val = romanToInt(text)
            text = ''
            temp_s += str(val)
    result = calc(temp_s)
    return result


if __name__ == '__main__':
    inp = '(II+III)*IV'
    print(f'{solution(inp)}')
