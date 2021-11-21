print("\n\nLevel 1. To pass the level, you need to insert an input greater than 10")
x = input("Insert you input:\t")

try:
    x = int(x)

    if x < 10:
        print("Minore 10")
        score = x
    else:
        print("Maggiore 10")
        score = 1
except:
    x_vec = x.split("7")
    print("dentro eccezione, inserito input non convertibile")
    print("Lunghezza vettore")
    print(x_vec)
    if len(x_vec) == 2:
        print("stringa splittata da 7 è un vettore di due elementi")
        try:
            #ultimo elemento del primo == primo del secondo
            x_vec[0] = x_vec[0][-1]
            x_vec[1] = x_vec[1][0]
            #sommo due vettori
            score = int(x_vec[0]) + int(x_vec[1])
        except:
            print("Non credo")
            score = 2
    else:
        print("OK")
        score = 8
if score > 10:
    print (4)
else:
    print (0)
