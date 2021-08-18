class Conversion:

    def __init__(self, stackSize):
        self.array = []
        self.stackSize = stackSize
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def size(self):
        return len(self.array)

    def top(self):
        """Checking whether the stack is empty, if not we return the last element"""
        if self.isEmpty():
            print("Stack empty")
            return -1
        else:
            last_ele = self.array[-1]
            return last_ele

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.size() == self.stackSize:
            return True
        else:
            return False

    def push(self, ele):
        """checks whether array size equals stack limit, if not pushes the new element into the array"""
        if self.isFull():
            print("Stack full, can't push")
            return
        else:
            self.array.append(ele)

    def pop(self):
        """checks whether stack is empty, if not removes the top most element from the stack"""
        if self.isEmpty():
            print("Stack empty, can't pop")
            return -1
        else:
            """it shouldn't just pop the element, but it has to return"""
            last_ele = self.array[-1]
            self.array.pop()
            return last_ele

    def printStack(self):
        if self.isEmpty():
            print("Stack Empty")
        else:
            for i in reversed(self.array):
                print(i)

    '''Operations specific to Infix to Postfix conversion'''

    def checkGreaterPrecedence(self, char):
        i = self.precedence[char]
        j = self.precedence[self.top()]
        return True if i > j else False

    def isOperand(self, val):
        return ("A" <= val <= "Z") or ("a" <= val <= "z")

    def infixToPostfix(self, expression):
        result = ""

        for char in expression:
            '''If an operand is encountered, we just print it'''
            if self.isOperand(char):
                result += char

            elif char == '(':
                '''If a '(' is encountered, we push it to the stack'''
                self.array.append(char)

            elif char == ')':
                '''If a ')' is encountered, we pop everything until a '(' is found and print it one by one'''
                popVal = self.array.pop()
                while popVal != '(':
                    result += popVal
                    popVal = self.array.pop()

            else:
                '''If an operator is encountered, these cases follow'''
                while True:
                    if self.isEmpty() or self.top() == '(':
                        '''If the stack is empty or the stackTop has '(', we do not check other cases, but directly push the operator'''
                        self.array.append(char)
                        break

                    else:
                        '''Here, we check for precedence because either stack is not empty or stackTop isn't '(' '''
                        if self.checkGreaterPrecedence(char):
                            self.array.append(char)
                            break

                        else:
                            popped = self.array.pop()
                            result += popped

        while not self.isEmpty():
            result += self.array.pop()

        return result

    #


if __name__ == '__main__':
    # exp = "a+b*(c^d-e)^(f+g*h)-i"
    # infix = Conversion(len(exp))
    # print("Infix -> " + exp)
    # postfix = infix.infixToPostfix(exp)
    # print("Postfix -> " + postfix)

    infixExps = [
        'A*B+C',  # AB*C+
        'A+B*C',  # ABC*+
        'A*B+C*D',  # AB*CD*+
        'A*B^C+D',  # ABC^*D+
        'A*(B+C*D)+E',  # ABCD*+*E+
        'A+(B*C-(D/E^F)*G)*H',  # ABC*DEF^/G*-H*+
        '(A+B)*C+D/(E+F*G)-H',  # AB+C*DEFG*+/+H-
        'A-B-C*(D+E/F-G)-H'  # AB-CDEF/+G-*-H-
    ]

    for exp in infixExps:
        p = Conversion(len(infixExps))
        postfix = p.infixToPostfix(exp)
        print(f'Infix: {exp} -> Postfix: {postfix}')
