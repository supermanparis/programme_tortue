import turtle # pour utiliser le module turtle qui va nous permettre de dessiner des lignes

t = turtle.Turtle() # ici crétion d'un objet.

# début code pour deplacer la tortue

# exo : 5 marches de 30 pixels :
'''

def dessiner_marche(pixels,marches):  # ici definition d'une fonction ayant pour parametres pixels et marches
    for i in range(0,marches):
            t.forward(pixels)
            t.left(90)
            t.forward(pixels)
            t.right(90)
    t.forward(pixels)

dessiner_marche(30,5) # appel de la fonction dessiner_marche, avec pour parametre 30 pixels, et 5 marches


def escalier(taille,nb):  # ici definition d'une fonction ayant pour parametres pixels et marches
    for i in range(0,nb):
            t.forward(taille)
            t.left(90)
            t.forward(taille)
            t.right(90)
    t.forward(taille)

escalier(30,5) # appel de la fonction dessiner_marche, avec pour parametre 30 pixels, et 5 marches


def escalier(taille,nb):  # ici exemple de decrementation où la taille de la marche diminue a chaque tour
    for i in range(0,nb):
            t.forward(taille)
            t.left(90)
            t.forward(taille)
            t.right(90)
            taille = taille - 5 # ou taille -=5
            
    t.forward(taille)

escalier(50,10)

'''


def escalier(taille,nb):  # ici exemple d' incrémentation où la taille de la marche augmante a chaque tour
    for i in range(0,nb):
            t.forward(taille)
            t.left(90)
            t.forward(taille)
            t.right(90)
            taille = taille + 10 # ou taille +=5
    t.forward(taille)

# escalier(50,10)

'''
def dessiner_carre(pixels):
    t.forward(pixels)
    t.left(90)
    t.forward(pixels)
    t.left(90)
    t.forward(pixels)
    t.left(90)
    t.forward(pixels)

dessiner_carre(200)

'''

def dessiner_carre(taille_pixels):
    for i in range(0,4):
        t.forward(taille_pixels)
        t.left(90)

dessiner_carre(300)




# fin code pour deplacer la tortue

turtle.done() # pour garder la fenetre active tant que l'on ne la ferme pas de manière explicite