import random

def transformation(input):
    input = list(input)
    input.append(input[0])
    input.pop(0)
    return "".join(input)


def encrypt(input, seed):
    input = transformation(input)
    input = list(input)
    random.seed(seed)
    input = [chr(ord(x) ^ random.randint(80, 120)) for x in input]
    input = "".join(input)
    return input


with open("./secret.txt", "r") as file:
    cipher = file.read()
