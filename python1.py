def swapthedata():
    1stfile=input('enter the file name: ')
    2ndfile=input('enter the file name: ')
    with open(1stfile,'r') as a:
        data_a=a.read()
        
        with open(2ndfile,'r') as b:
            data_b=b.read()
    with open(1stfile,'w') as a:
        a.write(data_b)
    with open(2ndfile,'w') as b:
        b.write(data_a)
swapthedata() 