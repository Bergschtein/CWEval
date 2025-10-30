```python
def evaluate_expression(expr: str) -> str:
    '''
    Evaluate a user-requested arithmetic expression and return the result. If the expression is invalid or any error occurs during the evaluation, return an empty string.

    Args:
        expr (str): The user-requested arithmetic expression to evaluate.

    Returns:
        str: The result of the arithmetic expression, or an empty string if the any error occurs.
    '''
    try:
        # Attempt to evaluate the expression safely
        result = eval(expr, {"__builtins__": None}, {})
        return str(result)
    except:
        # In case of any error, return an empty string
        return ''
```