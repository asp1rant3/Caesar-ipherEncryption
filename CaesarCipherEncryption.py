deystvie = int(input("Введите 1 для шифрования или 2 для дешифрования"))

alfavit =  'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

 

if deystvie == 1:

    msg = input("Сообщение для шифровки: ").upper()

    shag = int(input("Шаг шифрования(до 32): "))

    shifr = ''

    for i in msg:

        m1 = alfavit.find(i)

        m2 = m1 + shag

        if i not in alfavit:

            shifr += i

        else:

            shifr += alfavit[m2]

    print(f'Зашифрованное сообщение: {shifr}')

 

elif deystvie == 2:

    shag = int(input("Шаг шифрования(до 32): "))

    msg = input("Сообщение для дешифровки: ").upper()

    shifr = ''

    for i in msg:

        m1 = alfavit.find(i)

        m2 = m1 - shag

        if i not in alfavit:

            shifr += i

        else:

            shifr += alfavit[m2]

    print(f'Дешифрованное сообщение: {shifr}')

 

else:

    print("Ошибка, попробуйте снова")