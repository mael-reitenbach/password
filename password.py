import string
import hashlib
import json

def check():
    maj = False
    minu = False
    chiff = False
    spe = False
    long = False
    test = input("Veuillez entrer votre mot de passe : ")
    
    #Vérification de la longueur
    if len(test) < 7:
        long = True
        print("Votre mot de passe est trop court, il doit avoir au moins 8 charactères")
    
    #Vérification de la présence d'une majuscule
    for x in list(string.ascii_uppercase):
        if test.count(x):
            maj = True
    if maj == False:
        print("Votre mot de passe doit contenir au moins une lettre majuscule")

    #Vérification de la présence d'une lettre minuscule    
    for x in list(string.ascii_lowercase):
        if test.count(x):
            minu = True
    if minu == False:
        print("Votre mot de passe doit contenir au moins une lettre minuscule")

    #Vérification de la présence d'un chiffre    
    for x in list(string.digits):
        if test.count(x):
            chiff = True
    if chiff == False:
        print("Votre mot de passe doit contenir au moins un chiffre")
    
    #Vérification de la présence d'un charactère spécial
    for x in list(string.punctuation):
        if test.count(x):
            spe = True
    if spe == False:
        print("Votre mot de passe doit contenir au moins un charactère spécial")
    if spe and chiff and min and maj:
        #Hashing du mot de passe
        lock = hashlib.new("SHA256")
        lock.update(test.encode())
        hash_go = lock.hexdigest()
        #Stockage du hash 
        try:
            with open("passwords_hash.json", "r") as f:
                print("OUVERT")
                pass
        except FileNotFoundError:
            with open('passwords_hash.json', 'w') as f:
                content = []
                json.dump(content, f)

        with open("passwords_hash.json", "r") as f:
            data = json.load(f)
            print(data)
            print(type(data))
            data.append(hash_go)
            print(data)
        with open("passwords_hash.json", "w") as f:
            json.dump(data, f)
        return True
    
while not check():
    check()

print("Le mot de passe choisi rempli les différents critères de sécurité")
