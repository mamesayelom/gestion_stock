from database.db_connection import ma_connexion
from Models.produit import afficher_produit
from Models.produit import get_quantite,modifier_quantite_produit,modifier_etat_produit

def Faire_mouvement(id_produit,quantite,type):
    conn=ma_connexion()
    curseur=conn.cursor()
    try:
        sql='insert into mouvement(id_produit,quantite,type)values(%s,%s,%s)'
        curseur.execute(sql,(id_produit,quantite,type))
        conn.commit()
        return 'mouvement effectuer avec succes'
    except Exception as e:
        return "Erreur lors de l'enregistrement de mouvement: ",e
    finally:
        curseur.close()
        conn.close()
def appelle_mouvement():
    while True:
        liste=afficher_produit()
        choix= input('Choisir un produit ').strip()
        if choix.isnumeric():
            choix=int(choix)
            if choix in liste:
                id_produit=choix
                stock=get_quantite(id_produit)
                print(stock)
                while True:
                    quantite=input('saisir une quantite')
                    if quantite.isnumeric():
                        quantite=int(quantite)
                        break
                    else:
                        print('la quantite doit etre un nombre')
                while True:
                    print('1 ENTREE')
                    print('2 SORTIE')
                    choix_type=input('Faire votre choix')
                    match choix_type:
                        case '1':
                            type='ENTREE'
                        case '2':
                            type='SORTIE'
                        case _:
                            print('choix type invalide')
                    if type=='SORTIE':
                        if stock < quantite:
                            print("le stock du produit n'est pas suffisant")
                        else:
                            Faire_mouvement(id_produit,quantite,type)
                            q=stock-quantite
                            modifier_quantite_produit(q)
                    if type=='ENTREE':
                        Faire_mouvement(id_produit,quantite,type)
                        q=stock+quantite
                        modifier_quantite_produit(q)
                    if q < 5:
                        modifier_etat_produit('En rupture')
                        break
                    else:
                        modifier_etat_produit('Disponible')
                        break

                    
            else:
                print('choix invalide')
            
        else:
            print('vous devez saisir un nombre')
