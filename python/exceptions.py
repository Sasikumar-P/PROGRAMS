def execc(x, y):
    try:
       z = x/y
    except ZeroDivisionError, e:
       err = e
    print e



