from database.db_connection import ma_connexion

def ajouter_categorie(nom):
    conn=ma_connexion()
    curseur=conn.cursor()
    try:
        sql='insert into categories(nom_categorie)values(%s)'
        curseur.execute(sql,(nom,))
        conn.commit()
        print('categorie ajouter avec succees')
    except Exception as e:
        print('vous avez une erreur ',e)
    finally:
        curseur.close()
        conn.close()

def creer_categorie():
    try:
        while True:
            nom=input('entrer le nom de la categorie ').strip()
            if not nom.isnumeric():
                if len(nom) >= 3:
                    break
                else:
                    print('saisi invalide')
            else:
                print('le nom ne doit pas etre un nombre')
        return ajouter_categorie(nom)
    except Exception as e:
        print('Erreur',e)

def afficher_categorie():
    conn=ma_connexion()
    curseur=conn.cursor()
    try:
        sql='select * from categories order by id'
        curseur.execute(sql)
        categories=curseur.fetchall()
        if len(categories)==0:
            print('pas de categories')
        liste=[]
        for categorie in categories:
            print(categorie[0],':',categorie[1])
            liste.append(categorie[0])
        return liste
    except Exception as e:
        print("erreur lors de l'affichage",e)
    finally:
        curseur.close()
        conn.close()

def modifier_categorie(nom,id):
    conn=ma_connexion()
    cursseur=conn.cursor()
    try:
        sql="update categories set nom_categorie=%s where id=%s"
        cursseur.execute(sql,(nom,id))
        conn.commit()
        print('la categorie a ete modifier avec succes')
    except Exception as e:
        print('erreur lors de la modification',e)
    finally:
        cursseur.close()
        conn.close()
def modifiercategorie1():
    while True:
        liste=afficher_categorie()
        print(liste)
        id=input('choisir une categorie ').strip()
        if id.isnumeric():
            id=int(id)
            if id not in liste:
                print('choix invalide')
            else :
                while True:
                    nom=input('entrer un nouveau nom ').strip()
                    if nom.isnumeric():
                        print('le nom ne doit pas etre un nombre')
                    else:
                        return modifier_categorie(nom,id)
        else:
            print('saisir un nombre')

def supprimer_categorie(id):
    conn=ma_connexion()
    curseur = conn.cursor()
    try:
        sql = "DELETE FROM categories WHERE id = %s"
        curseur.execute(sql, (id,))
        conn.commit()
        print(f"categorie {id} a ete supprimer.")
    except Exception as e:
        print('erreur lors de la suppression ',e)
    finally:
        curseur.close()
        conn.close()

