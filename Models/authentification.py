from database.db_connection import ma_connexion

import hashlib
import getpass

import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

# Fonction pour se connecter
def login():
    conn = ma_connexion()
    if conn is None:
        return
    
    cursor = conn.cursor(dictionary=True)

    email = input("\nEmail : ").strip()
    password = getpass.getpass("Mot de passe : ").strip()

    try:
        cursor.execute(
            "SELECT prenom, nom, role , password FROM utilisateurs WHERE email = %s",
            (email,)
        )
        user = cursor.fetchone()

        if user and check_password(password, user["password"]):
            if user:
                print(f"\nBienvenue {user['prenom']} {user['nom']} 👋 Role : {user['role']}")
                print("\n")

                return user   # on retourne l'utilisateur connecté
            
        else:
            print("\nIdentifiants incorrects. Réessayer")
            return None
    except Exception as e:
        print("Erreur de la connexion :", e)

    finally:
        cursor.close()
        conn.close()

# inscrire un nouvel utilisateur
def inscription():
    conn = ma_connexion()
    if conn is None:
        return

    while True:
        prenom = input("Prénom : ").strip()

        if len(prenom) == 0:
            print("Le Prénom ne doit pas etre vide")
            continue

    
        if prenom.isdigit():
            print("Le prénom ne peut pas contenir uniquement des chiffres")
            continue 

        break

    while True:
        nom = input("Nom : ").strip()

        if len(nom) == 0:
            print("Le nom ne doit pas etre vide")
            continue

        if nom.isdigit():
            print("Le nom ne peut pas contenir uniquement des chiffres")
            continue 

        break

    email = input("Email : ")

    while True:
       
        password = input("Mot de passe : ")
    
        if len(password) < 8:
            print("Le mot de passe doit etre au mois 8 caractères")
        else:
            break

    password_hash = hash_password(password)

    try:
        cursor = conn.cursor()
        query = "INSERT INTO utilisateurs(prenom, nom, email, password) VALUES(%s, %s, %s, %s)"
        cursor.execute(query, (prenom, nom, email, password_hash))
        conn.commit()
        print("\nUtilisateur inscrit avec succès.")
        return

    except Exception as e:
        print("Erreur de l'inscription", e)
    finally:
        cursor.close()
        conn.close()