class Finall_Python:
    def Menu(self):
        while True:
            print("1", ".", "Shapes")
            print("2", ".", "Calculator")
            print("3", ".", "Water bill")
            print("4", ".", "Stars")
            print("5", ".", "Factorial")
            print("6", ".", "Multiplication table")
            print("7", ".", "Product list")
            print("8", ".", "Age")
            b = input("choose your options => ")
            if b == "end".upper():
                exit()
            elif b == "end".lower():
                exit()
            elif b == "1":
                menu.pr1()
            elif b == "2":
                menu.pr2()
            elif b == "3":
                menu.pr3()
            elif b == "4":
                menu.pr4()
            elif b == "5":
                menu.pr5()
            elif b == "6":
                menu.pr6()
            elif b == "7":
                menu.pr7()
            elif b == "8":
                menu.pr8()
            elif b == "end":
                quit()

    def pr1(self):
        p = 3.14
        while True:
            try:
                object = input("choose one of the options: square - rectangle - circle - triangle=> ")
                if object == "end":
                    menu.Menu()
                    break
                Qustions = input("Do you want Environment or Area? ")
                if Qustions == "end":
                    menu.Menu()
                    break
                if object == "square":
                    length = input("Enter the number for length: ")
                    if length == "end":
                        menu.Menu()
                        break
                    width = input("Enter the number for width: ")
                    if width == "end":
                        menu.Menu()
                        break
                    diameter = input("Enter the number for diameter: ")
                    if diameter == "end":
                        menu.Menu()
                        break
                    diameter = int(diameter)
                    length = int(length)
                    width = int(width)
                    if length == width:
                        if diameter > length or width:
                            if Qustions == "Environment":
                                E = (length or width) * 4
                                print("Environment is:", E)
                            elif Qustions == "Area":
                                A = (length or width) ** 2
                                print("Area is:", A)
                elif object == "rectangle":
                    length = input("Enter the number for length: ")
                    if length == "end":
                        menu.Menu()
                        break
                    width = input("Enter the number for width: ")
                    if width == "end":
                        menu.Menu()
                        break
                    diameter = input("Enter the number for diameter: ")
                    if diameter == "end":
                        menu.Menu()
                        break
                    diameter = int(diameter)
                    length = int(length)
                    width = int(width)
                    if length > width or length < width:
                        if diameter > length and width:
                            if Qustions == "Environment":
                                E = (length + width) * 2
                                print("Environment is:", E)
                            elif Qustions == "Area":
                                A = length * width
                                print("Area is:", A)
                elif object == "circle":
                    diameter = input("Enter the number for diameter: ")
                    if diameter == "end":
                        menu.Menu()
                        break
                    diameter = int(diameter)
                    r = diameter / 2
                    if Qustions == "Environment":
                        E = p * diameter
                        print("Environment is:", E)
                    elif Qustions == "Area":
                        A = p * r * r
                        print("Area is", A)
                elif object == "triangle":
                    if Qustions == "Environment":
                        t1 = input("Enter the number for district: ")
                        t1 = int(t1)
                        E = t1 * 3
                        print("Environment is:", E)
                    elif Qustions == "Area":
                        t4 = input("Enter the number for rule")
                        t5 = input("Enter the number for height")
                        t4 = int(t4)
                        t5 = int(t5)
                        A = (t4 * t5) / 2
                        print("Area is:", A)
            except:
                menu.Menu()

    def pr2(self):
        while True:
            import math
            try:
                Symbol = input("Choose the symbol: / , - , + , * , Log , ** , Radical => ")
                if Symbol == "end".upper():
                    menu.Menu()
                    break
                elif Symbol == "end".lower():
                    menu.Menu()
                    break
                Number1 = input("Enter the first number: ")
                if Number1 == "end".lower():
                    menu.Menu()
                    break
                elif Number1 == "end".upper():
                    menu.Menu()
                    break
                Number2 = input("Enter the second number: ")
                if Number2 == "end".lower():
                    menu.Menu()
                    break
                elif Number2 == "end".upper():
                    menu.Menu()
                    break
                Number1 = int(Number1)
                Number2 = int(Number2)
                if Symbol == "/":
                    text = "{} / {} = {}".format(Number1, Number2, Number1 / Number2)
                    print(text)
                elif Symbol == "+":
                    text = "{} + {} = {}".format(Number1, Number2, Number1 + Number2)
                    print(text)
                elif Symbol == "-":
                    text = "{} - {} = {}".format(Number1, Number2, Number1 - Number2)
                    print(text)
                elif Symbol == "*":
                    text = "{} * {} = {}".format(Number1, Number2, Number1 * Number2)
                    print(text)
                elif Symbol == "log":
                    text = "log{},{} = {}".format(Number1, Number2, math.log(Number1, Number2))
                    print(text)
                elif Symbol == "**":
                    text = "{} ** {} = {}".format(Number1, Number2, Number1 ** Number2)
                    print(text)
                elif Symbol == "Radical":
                    text = "Radical{} = {}".format(Number1, math.sqrt(Number1))
                    print(text)
            except:
                menu.Menu()

    def pr3(self):
        while True:
            try:
                a = 0
                Water_bill = input("Enter your water bill amount: ")
                if Water_bill == "end".lower():
                    menu.Menu()
                    break
                elif Water_bill == "end".upper():
                    menu.Menu()
                    break
                Units = {1: 4, 2: 4, 3: 0, 4: 2, 5: 4, 6: 0, 7: 5, 8: 5, 9: 2}
                Water_bill = int(Water_bill)
                personal_bill = Water_bill // 26
                for b in Units.values():
                    a += 1
                    text = "{} = {} {}".format(a, b * personal_bill, "toman")
                    print(text)
            except:
                menu.Menu()

    def pr4(self):
        while True:
            try:
                Number = input("Enter the number: ")
                if Number == "end".upper():
                    menu.Menu()
                    break
                elif Number == "end".lower():
                    menu.Menu()
                    break
                Number = int(Number)
                for stars in range(1, Number + 1):
                    print(stars, stars * "*")
            except:
                menu.Menu()

    def pr5(self):
        while True:
            try:
                a = 1
                b = input("Enter the number: ")
                b = int(b)
                if b == "end".lower():
                    exit()
                elif b == "end".upper():
                    exit()
                Numbers = range(1, b + 1)
                for numbs in Numbers:
                    a = a * numbs
                    print(numbs, "*", end=" ", )
                print("=", a)
                break
            except:
                menu.Menu()

    def pr6(self):
        while True:
            b = []
            L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            try:
                Numbers = input("Enter the number: ")
                Numbers = int(Numbers)
                if Numbers == "end".lower():
                    exit()
                elif Numbers == "end".upper():
                    exit()
                L = list(map(lambda x: x * Numbers, L))
                print(L)
            except:
                menu.Menu()

    def pr7(self):
        a = []
        b = 0
        c = 0
        m = 0
        try:
            while True:
                Product = input("Enter the product name: ")
                if Product == "end":
                    menu.Menu()
                    exit()
                Price = input("Enter the price of product: ")
                if Price == "end":
                    menu.Menu()
                    exit()
                Number = input("Enter the number of product: ")
                if Number == "end":
                    menu.Menu()
                    exit()
                Price = int(Price)
                Number = int(Number)
                text1 = "{} |      {}     {}".format("Name", "Price", "Number")
                text2 = "{}".format("----------------------------------")
                text3 = "{} |      {}      {}".format(Product, Price, Number)
                print(text1)
                print(text2)
                a.append(text3)
                for i in a:
                    print(i)
                if isinstance(Product, str):
                    b += 1
                    if isinstance(Price, int):
                        m += Price * Number
                        if isinstance(Number, int):
                            c += Number
                            print(text2)
                            text0 = "{} :".format("Total")
                            text9 = "{} |      {}      {}".format(b, m, c)
                            print(text0)
                            print(text9)
        except:
            menu.Menu()

    def pr8(self):
        from datetime import date
        birthday = input('Enter your date birth: ').split('/')
        if (int(birthday[1])>12) or (int(birthday[2])>31 ):
            print("WRONG")
        else:
            today = date.today()
            age = today.year - int(birthday[0]) - ((today.month, today.day) < (int(birthday[1]), int(birthday[2])))
            print(age)
            

menu = Finall_Python()
menu.Menu()
