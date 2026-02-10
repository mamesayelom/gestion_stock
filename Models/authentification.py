from database.db_connection import ma_connexion

def login():
    conn = ma_connexion()
    cursor = conn.cursor(dictionary=True)

    email = input("Email : ").strip()
    password = input("Mot de passe : ").strip()

    cursor.execute(
        "SELECT * FROM utilisateurs WHERE email = %s",
        (email,)
    )
    user = cursor.fetchone()
    
    if user and user['email'] == email and user['password'] == password:
        print(f"\nBienvenue {user['prenom']} {user['nom']} 👋")
        print("\n")

        return user   # on retourne l'utilisateur connecté
        
    else:
        print("\nIdentifiants incorrects. Réessayer")
        return None