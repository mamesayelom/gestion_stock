from Models.categoris import creer_categorie,afficher_categorie
from Models.produit import AjouterProduit,afficher_produit,afficher_produits_stock_faible
from Models.mouvement import appelle_mouvement,Afficher_mouvement

from Models.authentification import login
from Models.authentification import inscription


def menu_admin(user):

    while True:
        print("---------------Menu ADMIN-------------")
        print('1- Ajouter categorie')
        print('2- Afficher les categories')
        print('3- Ajouter un produit')
        print('4- Afficher les produits')
        print('5- Afficher les produits dont le stock est inférieur à 5 unités')
        print('6- Faire un mouvement')
        print('7- Afficher les mouvements')
        print('0. Déconnexion')

        choix= input('Faites votre choix : ')
        if choix.isnumeric():
            choix=int(choix)
            match choix:
                case 1:
                    creer_categorie()
                case 2:
                    afficher_categorie()
                case 3:
                    AjouterProduit()
                case 4:
                    afficher_produit()
                case 5:
                    afficher_produits_stock_faible()
                case 6:
                    appelle_mouvement()
                case 7:
                    Afficher_mouvement()
                case 0:
                    print("Vou êtes déconnecté. 👋")
                    break
                case _:
                    print('choix invalide')

        else:
            print('choix doit etre un nombre')


def menu_user(user):

    while True:
        print("---------------Menu USER-------------")
        
        print('1- Afficher les categories')
        print('2- Afficher les produits')
        print('3- Afficher les produits dont le stock est inférieur à 5 unités')
        print('4- Faire un mouvement')
        print('5- Afficher les mouvements')
        print('0- Déconnexion')

        choix= input('Faites votre choix : ')

        if choix.isnumeric():
            choix=int(choix)
            match choix:
                case 1:
                    afficher_categorie()
                case 2:
                    afficher_produit()
                case 3:
                    
                    afficher_produits_stock_faible()
                case 4:
                    appelle_mouvement() 
                case 5:
            
                    Afficher_mouvement()
                case 0:
                    print("Vou êtes déconnecté. 👋")
                    break
                case _:
                    print('choix invalide')

        else:
            print('choix doit etre un nombre')

def main():
    while True:
        print("\n" + "-" * 40)
        print("      GESTION DE STOCK")
        print("-" * 40)
        print("1. Se connecter")
        print("2. S'inscrire")
        print("0. Quitter")
        print("-" * 40)

        choix = input("Faites votre choix : ")

        if not choix.isdigit():
            print("Choix invalide")
            continue

        choix = int(choix)

        match choix:
            case 1:
                user = login()
                if user:
                    if user['role'] == 'admin':
                        menu_admin(user)
                    else:
                        menu_user(user)

            case 2:
                inscription()

            case 0:
                print("Au revoir 👋")
                break

            case _:
                print("Choix invalide")
main()
    
