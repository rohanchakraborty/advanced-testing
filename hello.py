def add_this(x,y):
    print(f"This is x: {x} x-type: {type(x)} and this is y:{y} y-type: {type(y)}")
    try:
        result = x+y
    except TypeError, exception:
        print(f"The wrong type passed")
        result = int(x)+int(y)

    print(f"This is result: {result}")    
    return result

print(add_this(1,2.3))