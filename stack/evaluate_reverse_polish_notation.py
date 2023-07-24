class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                # rounds towards zero. 
                # // rounds down
                stack.append(int(b / a))
            else:
                # alterately, you can use try/except int() to determine if it's an int
                # this only works because we're guaranteed token is +-*/ or an int
                stack.append(int(c))
        return stack[0]
