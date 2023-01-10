def add_two_num(a,b):
    print("ADDITION FUNCTION")
    try:
        return a+b
    except ValueError as val2:
        val2=str(val2)
        return str(val2)
    except TypeError as val3:
        val3=str(val3)
        return val3
    except NameError as val1:
        val1=str(val1)
        return str(val1)
print(add_two_num(2,87))
print(add_two_num(2,3.4))
print(add_two_num(2,"hii"))
