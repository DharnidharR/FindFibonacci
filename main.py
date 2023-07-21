def fibnoci_number(a):
    if (a==0):
        return 0
    if (a==1):
        return 1
    return fibnoci_number(a-1)+fibnoci_number(a-2)
print(fibnoci_number(int(input())))
