"""一个简单的计算器模块，用于学习 CI/CD。"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b

# 嘿嘿修复修复
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
