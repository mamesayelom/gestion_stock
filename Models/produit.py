from database.db_connection import ma_connexion
from Models.categoris import afficher_categorie

def Ajouter_produit(designation,prix,id_categorie):
    conn=ma_connexion()
    curseur=conn.cursor()
    try:
        sql='insert into produits(designation,prix,id_categorie)values(%s,%s,%s)'
        curseur.execute(sql,(designation,prix,id_categorie))
        conn.commit()
        print('produit ajouter avec succees')
    except Exception as e:
        print("erreur lors de l'enregistrement ",e)
    finally:
        curseur.close()
        conn.close()
def AjouterProduit():
    while True:
        designation=input('ajouter un designaton ').strip()
        if designation.isnumeric():
            print('ne doit pas etre un nombre')
        else:
            break
    while True:
        prix=input('ajouter le prix du produit ').strip()
        if prix.isnumeric():
            prix=int(prix)
            break
        else:
            print('le prix doit etre un nombre')
    while True:
        liste= afficher_categorie()
        id=input('choisir une categorie ').strip()
        if id.isnumeric():
            id=int(id)
            if id not in liste:
                print('choix invalide')
            else:
                return Ajouter_produit(designation,prix,id)
        else:
            print('saisir un nombre')

def afficher_produit():
    conn=ma_connexion()
    curseur=conn.cursor()
    liste=[]
    try:
        sql='select p.id,p.designation,p.prix,p.quantite,c.nom_categorie,p.etat from produits p join categories c on p.id_categorie=c.id'
        curseur.execute(sql)
        produits=curseur.fetchall()
        for produit in produits :
            print(
                    f"ID: {produit[0]} | "
                    f"Designation: {produit[1]} | "
                    f"Prix: {produit[2]} | "
                    f"quantite: {produit[3]} | "
                    f"Categorie: {produit[4]} | "
                    f"etat: {produit[5]}"
                )
            liste.append(produit[0])
        return liste
    except Exception as e:
        print("erreur lors de l'affichage ",e)
    finally:
        curseur.close()
        conn.close()

def afficher_produits_stock_faible():
    conn=ma_connexion()
    curseur=conn.cursor()
    liste=[]
    try:
        sql='select p.id,p.designation,p.prix,p.quantite,c.nom_categorie,p.etat from produits p join categories c on p.id_categorie=c.id where p.quantite < 5'
        curseur.execute(sql)
        produits=curseur.fetchall()
        for produit in produits :
            print(
                    f"ID: {produit[0]} | "
                    f"Designation: {produit[1]} | "
                    f"Prix: {produit[2]} | "
                    f"quantite: {produit[3]} | "
                    f"Categorie: {produit[4]} | "
                    f"etat: {produit[5]}"
                )
            liste.append(produit[0])
        return liste
    except Exception as e:
        print("erreur lors de l'affichage ",e)
    finally:
        curseur.close()
        conn.close()


def get_quantite(id_produit):
    conn=ma_connexion()
    curseur=conn.cursor()
    liste=[]
    try:
        sql='select quantite from produits where id=%s'
        curseur.execute(sql,(id_produit,))
        produit=curseur.fetchone()
        return produit[0]
    except Exception as e:
        print("erreur lors de la recuperation de la quntite ",e)
    finally:
        curseur.close()
        conn.close()

def modifier_quantite_produit(quantite):
    conn=ma_connexion()
    curseur=conn.cursor()
    try:
        sql='update produits set quantite=%s'
        curseur.execute(sql,(quantite,))
        conn.commit()
        print('success')
    except Exception as e:
        print("erreur lors de la modification de la quntite du produit ",e)
    finally:
        curseur.close()
        conn.close()

def modifier_etat_produit(etat):
    conn=ma_connexion()
    curseur=conn.cursor()
    try:
        sql='update produits set etat=%s'
        curseur.execute(sql,(etat,))
        conn.commit()
        print('success')
    except Exception as e:
        print("erreur lors de la modification de l'etat du produit ",e)
    finally:
        curseur.close()
        conn.close()


