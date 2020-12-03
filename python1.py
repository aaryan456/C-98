def swapthedata():
    firstfile=input('enter the file name: ')
    secondfile=input('enter the file name: ')
    with open(firstfile,'r') as a:
        data_a=a.read()
        
        with open(secondfile,'r') as b:
            data_b=b.read()
    with open(firstfile,'w') as a:
        a.write(data_b)
    with open(secondfile,'w') as b:
        b.write(data_a)
swapthedata() 
