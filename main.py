from data_structure.stack import Stack

class BracketError(Exception):

    def __init__(self, text: str):
        self.text = text

class ExpressionConverter:

    operation_priority = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    @staticmethod
    def __normalize_infix_expression(expression: str) -> str:

        """
        Метод который учитывает отрицательные значения и приводит инфиксную
        запись выражения к виду пригодному для перевода в постфиксную запись
        :param expression:
        :return:
        """

        if expression[0] == "-":
            expression = "0" + expression
        if "(-" in expression:
            expression = expression.replace("(-", "(0-")
        return expression

    @staticmethod
    def __add_space_expression(expression: str) -> str:
        """

        Добавляет пробелы между операндами и знаками.
        :param expression: str: строка.
        :return:
            str: строка с расставленными пробелами.
        """
        res_str = ""
        for symbol in expression:
            if symbol.isdigit():
                res_str += symbol
            elif symbol in "+-*/()":
                res_str += " " + symbol + " "
        return res_str
    @staticmethod
    def __check_brackets(expression: str) -> bool:
        """
        Проверка правильно ли раставлены скобки в выражении '()'
        :param expression str: строка
        :return:
            True: Корректно
            False: Не корректно
        """
        brackets = {
            "(": ")",
        }
        stack = Stack()
        for symbol in expression:
            if symbol in brackets.keys():
                stack.push(symbol)
            elif not stack.is_empty() and symbol == brackets[stack.peek()]:
                stack.pop()
            elif symbol.isdigit() or symbol in "+-*/ ":
                continue
            else:
                return False
        if stack.is_empty():
            return True
        return False


    @staticmethod
    def to_postfix(expression: str) -> list:
        """
        Вощзвращает  выражение в постфиксной форме записи

        :param expression: str
        :return:
                list
        """
        result_str = ""
        stack = Stack()
        check_brackets = ExpressionConverter.__check_brackets(expression)
        if check_brackets:
            expression = ExpressionConverter.__normalize_infix_expression(expression)
            expression = ExpressionConverter.__add_space_expression(expression)
            operation_value = ExpressionConverter.operation_priority
        else:
            raise BracketError(f"Не корректно расставлены скобки: {expression}.")
        for symbol in expression:
            # 1.1
            if symbol.isdigit():
                result_str += symbol
            # 1.2
            elif symbol == "(":
                stack.push(symbol)
            # 1.3
            elif symbol == ")":
                while stack.peek() != "(":
                    result_str += " " + stack.peek()
                    stack.pop()
                stack.pop()
            elif symbol == " ":
                result_str += symbol
            # 1.4
            elif symbol in "+-*/":
                if len(stack) == 0:
                    stack.push(symbol)
                elif not stack.is_empty() and operation_value[symbol] <= operation_value[stack.peek()]:
                    while not stack.is_empty() and operation_value[stack.peek()] >= operation_value[symbol]:
                        result_str += " " + stack.peek()
                        stack.pop()
                    stack.push(symbol)
                else:
                    stack.push(symbol)

        # 2
        while len(stack) != 0:
            result_str += " " + stack.pop()
        return result_str

