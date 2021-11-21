# plaintext = "here_the_message_with_the_flag"
# key = 'password'

import random
import datetime

def some_fancy_struggling_function(n):
    if n<=0:
        raise Exception("Incorrect input")
    elif n==1: // se 
        return 0
    elif n==2:
        return 1
    else:
        return (some_fancy_struggling_function(n-1) +
                some_fancy_struggling_function(n-2))

#if c = pari then this return a
def hello_world(a, b, c):
    for i in range(c):
        a = a ^ b

    return a


def most_secure_encryption_of_the_world(plaintext, key):

    year = datetime.date.today().year # ANNO = 2021

    w = len(key)  #W = ??

    junk = []
    fooo = []
    #foo alla prima iterazione è 0
    #foo alla seconda iterazione è 1
    #alla 3 iterazione è (call(3-1) = 1) + (call(3-2) = 0) => 1
    #alla 4 iterazione è (call(3) = 1 + call(4-2) = 1 => 2
    #alla 5 iterazione è (call(4) + call(3) = 2+1
    #n => n-1 + n-2
    #abbiamo gettatto foooo, si basa solamente sulla lunghezza della chiave
    for i in range(len(key)): #i parte da 0 e arriva a ??
        foo = some_fancy_struggling_function(i + 1) #foo = ricavabile
        fooo.append(foo)
        #random seed è ricavabile
        random.seed(foo)
        #quindi junk è vulnerabile
        junk.append(random.randint(0, 10))

    plaintext_not_so_plain = [ord(x) for x in (plaintext)]
    #pnsp = ord(plaintext) => numero ascii della chiave

    definetely_not_a_plain_text = []
    #i = 0=>len(plaintext)
    #x = lettere in numero ascii
    for i, x in enumerate(plaintext_not_so_plain):
        #idx = resto di i diviso dalla lunghezza di key, quindi finchè i<key idx = i
        idx = i % len(key)
        #seed = 2021
        random.seed(year)
        #rand = len(key) xor x(questo è vulnerabile), x può essere ricavato
        rand = w ^ random.randint(0, 10)
        #y = vulnerabile
        y = junk[idx]
        #z = vulnerabilissimo
        z = fooo[idx]
        #dnpt = dnpt + (x%2=0? x : x xor y)
        definetely_not_a_plain_text.append(chr(hello_world(x, y, z)))
    #add padding
    definetely_not_a_plain_text.append(chr(rand))
    #crea una stringa dal vettore 
    definetely_not_a_plain_text = ''.join(definetely_not_a_plain_text)

    return definetely_not_a_plain_text


#execute the algorithm
ciphertext = most_secure_encryption_of_the_world(plaintext, key)

#save the message
with open('./enc_message.txt', 'w') as file:
    file.writelines(ciphertext)
