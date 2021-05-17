#!/usr/bin/python3
def safe_print_division(a, b):
    """print the division

    Args:
        a: first num
        b: second num
    returns:
        result
        """
    result = 0
    try:
        result = a / b
    except (TypeError):
        print("Inside result: None")
    finally:
        print("Inside result: {}".format(result));

        return result
