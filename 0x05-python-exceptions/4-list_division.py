#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []

    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
            if isinstance(res, (int, float)):
                res_list.append(res)
            else:
                print("wrong type")
                res_list.append(0)
        except (ZeroDivisionError, IndexError):
            if isinstance(my_list_1, (int, float)) and isinstance(my_list_2, (int, float)):
                print("division by 0")
            else:
                print("out of range")
            res_list.append(0)
        except Exception:
            print("wrong type")
            res_list.append(0)

    return res_list
