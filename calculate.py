def calculate():
    newInput = input('Lutfen islemi giriniz   ')
    newInput = newInput.replace(" ", "")  # removes all ' ' spaces
    islemList = ['+', '-', '*', '/']
    count = 0
    for i in islemList:
        if newInput.find(i) >= 0:  # if any of the + - * / exists, execute the calculation
            count = count + 1
            if i == '+':
                # basically splits the string into 2 pieces and assignes the values to a and b
                a, b = newInput.split('+')
                print(float(a) + float(b))

            elif i == '-':
                a, b = newInput.split('-')
                print(float(a)-float(b))
            elif i == '*':
                a, b = newInput.split('*')
                print(float(a)*float(b))
            elif i == '/':
                a, b = newInput.split('/')
                print(float(a)/float(b))
    if count < 1:          # if there is no + - * /
        print('Lutfen formati dogru giriniz. 4+4, 3*2 etc.')
    yesNo = input('Yeni bir islem yapmak ister misiniz?  Y/N?  ')
    if yesNo == 'y' or yesNo == 'Y':
        calculate()
    else:
        print('Tesekkurler')


calculate()
