from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key() #encrypt

    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


main_pwd = input("Cual es tu contrasena?: ")

key = load_key()
fer = Fernet(key)



def mirar():
    with open('contras.txt', 'r') as f:
        for line in f.readlines():
            datos = line.rstrip()
            user, contra = datos.split("|")
            print("Usuario:", user, ", Contraseña:", fer.decrypt(contra.encode()).decode())
                                                  
            
    

def anadir():
    nombre = input("Inserte su usuario: ")
    pwd = input("inserte su contraseña: ")

    with open('contras.txt', 'a') as f:

        f.write(nombre + "|" + fer.encrypt(pwd.encode()).decode() + "\n") 

while True:
    mode = input("Te gustaria anyadir alguna PW o ver las que ya existen? (mirar, anadir): ").lower()

    if mode == "q":
        break

    if mode == "mirar":
        mirar()

    elif mode == "anadir":
        anadir()

    else:
        print("opcion invalida.")
        continue