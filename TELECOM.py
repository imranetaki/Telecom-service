def TTP(X):
    T = [] 
    prix1 = 200
    if X > 120:
        prix2 = 100 + (X - 120) * 0.5
    else:
        prix2 = 100
    if X > 60:
        prix3 = 50 + (X - 60) * 1
    else:
        prix3 = 50
    if X > 30:
        prix4 = 20 + (X - 30) * 1.5
    else:
        prix4 = 20
    prix5 = X * 2

    T.append(prix1)
    T.append(prix2)
    T.append(prix3)
    T.append(prix4)
    T.append(prix5)

    return T

X = 0

while True:
    print("Menu:")
    print("1- Enter the duration  of communication : " )
    print("2- Display the monthly cost for each plan : ")
    print("3- Display the most able offer financially ")
    print("4- Quit the program")

    choix = input("Choose an option (1 or 2 or 3 or 4 ) (when you choose the option chose the next one please ) : ")

    if choix == "1":
        X = int(input("Enter the communication duration in minutes: "))

    elif choix == "2":
        TOUTPRIX = TTP(X)
        print("Monthly cost per plan:")
        for i in range(len(TOUTPRIX)):
            print(f"{i + 1}- Plan {i + 1}: {TOUTPRIX[i]} DH")

    elif choix == "3":
        TOUTPRIX = TTP(X)
        LOWESTPRICE = min(TOUTPRIX)
        THEGOODOFFER = TOUTPRIX.index(LOWESTPRICE) + 1 
        print(f"The most cost-effective plan is Plan {THEGOODOFFER} with a cost of {LOWESTPRICE} DH.")

    elif choix == "4":
        print("Program terminated.")
        break
    else:
        print("Invalid option. Please choose a valid option (1/2/3/4).")