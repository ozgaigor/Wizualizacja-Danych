def fibonacciego(n):
    a = 0
    b = 1
    for x in range(n):
        yield a
        tmp = a+b
        a = b
        b = tmp
#-------------------------------------------------------------------------------------------------------
print(list(fibonacciego(20)))
#-------------------------------------------------------------------------------------------------------
