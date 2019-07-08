class Parser:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def getValue(self):
        value = self.parseExpression()
        
        # if self.hasNext():
        #     raise Exception(
        #         "Unexpected character found: '" + 
        #         self.peek() + 
        #         "' at index " + 
        #         str(self.index))
        return value
    
    def peek(self):
        return self.string[self.index:self.index + 1]
    
    def hasNext(self):
        return self.index < len(self.string)
    
    def parseExpression(self):
        return self.parseAddition()
    
    def parseAddition(self):
        values = [self.parseMultiplication()]
        while True:
            char = self.peek()
            if char == '+':
                self.index += 1
                values.append(self.parseMultiplication())
            elif char == '-':
                self.index += 1
                values.append(-1 * self.parseMultiplication())
            else:
                break
        return sum(values)
    
    def parseMultiplication(self):
        values = [self.parseValue()]
        while True:
            char = self.peek()
            if char == '*':
                self.index += 1
                values.append(self.parseValue())
            elif char == '/':
                div_index = self.index
                self.index += 1
                denominator = self.parseValue()
                values.append(1.0 / denominator)
            else:
                break
        value = 1.0
        for factor in values:
            value *= factor
        return value
    
    
    def parseValue(self):
        char = self.peek()
        if char in '0123456789.':
            return self.parseNumber()
        
    def parseNumber(self):
        strValue = ''
        decimal_found = False
        char = ''
        
        while self.hasNext():
            char = self.peek()
            if char == '.':
                decimal_found = True
                strValue += '.'
            elif char in '0123456789':
                strValue += char
            else:
                break
            self.index += 1
        
        return float(strValue)
    
def evaluate(expression):
    try:
        p = Parser(expression)
        value = p.getValue()
    except ValueError:
        raise 'This arithmetic expression is not valid. Please reexamine input'

    if int(value) == value:
        return int(value)
    
    return value


print(evaluate('1+2'))
print(evaluate('34-5*100'))
print(evaluate('10-20*30+40/50'))