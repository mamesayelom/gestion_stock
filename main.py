from Models.categoris import creer_categorie,afficher_categorie
from Models.produit import AjouterProduit,afficher_produit,afficher_produits_stock_faible
from Models.mouvement import appelle_mouvement,Afficher_mouvement


#conn=ma_connexion()
#if conn.is_connected():
    #print('connexion reussi')
#else:
    #print('pas de connexion')

#print(creer_categorie())
#print(afficher_categorie())
#print(modifiercategorie1())
#print(AjouterProduit())
#print(afficher_produit())
#appelle_mouvement()

def main():
    while True:
        print("---------------Menu-------------")
        print('1- Ajouter categorie')
        print('2- Afficher les categories')
        print('3- Ajouter un produit')
        print('4- Afficher les produits')
        print('5- Afficher les produits dont le stock est inférieur à 5 unités')
        print('6- Faire un mouvement')
        print('7- Afficher les mouvements')
        choix= input('Faites votre choix')
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
                case _:
                    print('choix invalide')

        else:
            print('choix doit etre un nombre')
main()
    
