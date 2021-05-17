#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(0, list_length):
        try:
            result_list.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            result_list.append(0)
            print("wrong type")
        except ZeroDivisionError:
            result_list.append(0)
            print("division by 0")
        except IndexError:
            result_list.append(0)
            print("out of range")
        finally:
            print("", end="")

    return(result_list)
