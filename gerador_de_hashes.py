import hashlib

string = input("Digite o texto a ser gerado a hash: ")
menu = -1

while menu != 0:
    print("Escolha o tipo de Hash: ")
    print("1) MD5")
    print("2) SHA1")
    print("3) SHA256")
    print("4) SHA512")
    menu = int(input(" Digite o número do hash a ser gerado: "))

    if menu == 1:
        resultado = hashlib.md5(string.encode("utf-8"))
        print("A hash MD5 da string: ", string, "é: ", resultado.hexdigest())

    elif menu == 2:
        resultado = hashlib.sha1(string.encode("utf-8"))
        print("A hash SHA1 da string: ", string, "é: ", resultado.hexdigest())

    elif menu == 3:
        resultado = hashlib.sha256(string.encode("utf-8"))
        print("A hash SHA256 da string: ", string, "é: ", resultado.hexdigest())

    elif menu == 4:
        resultado = hashlib.sha512(string.encode("utf-8"))
        print("A hash SHA512 da string: ", string, "é: ", resultado.hexdigest())

    elif menu > 4: print("Erro")
