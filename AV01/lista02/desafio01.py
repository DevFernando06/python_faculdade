def finonacci(max_value) :
    a = 0
    b = 1

    while a <= max_value :
        print(a, end= " ")
        count = a
        a = b
        b = count + a      

finonacci(500)
