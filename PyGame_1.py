#-----------------------------Initialisation pygame----------------------------#

import pygame                   # Les 3 lignes permettent d'initialiser pygame
from pygame.locals import *
pygame.init()


#---------------------------------------Son-----------------------------------#


son = pygame.mixer.Sound("official_ground_theme.wav")

son.play(1000)




#-----------------------Configuration de la fenêtre du jeux--------------------#

fenetre = pygame.display.set_mode((540, 540)) # redimensionner la fenetre.
fenetre_2 = pygame.display.set_caption("Zelda©")
icon_32x32 = pygame.image.load("icone_1.png").convert_alpha()
pygame.display.set_icon(icon_32x32)


#------------------------------------Code--------------------------------------#

#-------------------------------Configuration des personnages------------------#

fond= pygame.image.load("plage.jpg").convert() # La ligne permet d inserer une image de fond dans la fenetre.

fenetre.blit(fond,(0,0)) # permet d'initialiser la position de l'image (il sera positionner au coin superieur gauche).

perso = pygame.image.load("character.png").convert_alpha() # On insere l'image dans sa position initiale.

perso = pygame.transform.scale(perso,(180,180))

#perso_2 = pygame.image.load("monstre_1.png").convert_alpha() # On insere l'image dans sa position initiale.
#perso_2 = pygame.transform.scale(perso_2,(0,0))

fenetre.blit(perso,(17,17)) # Position du personnage.
#fenetre.blit(perso_2,(17,17))
pygame.display.flip()


#----------------------------Evenement du personnage---------------------------#

# Ces lignes suivantes permettent de libere la fenetre graphique ( eviter l'erreur ne repond pas).
position_perso=0
position_perso_y=0
position_perso_x=0
continuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type==QUIT:
            continuer=0

        if event.type==KEYDOWN:
            if event.key==K_DOWN:
                if position_perso<2:
                    position_perso =position_perso+1
                print(position_perso)

            if event.key==K_UP:
                 if position_perso>0:
                    position_perso=position_perso-1
            if event.key==K_LEFT:
                position_perso_x=position_perso_x+1







        fenetre.blit(fond, (0,0))  #collage du fond

        fenetre.blit(perso, (75,position_perso*180))

        pygame.display.flip()

pygame.quit()


