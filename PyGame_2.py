#Importatinon et initialisation de la bibliothèque Pygame
import pygame
from pygame.locals import *
pygame.init()

#Son
son = pygame.mixer.Sound("foot_musique.wav")
son.play(10000)


#Affichage des images
fenetre = pygame.display.set_mode((849, 565))
fenetre_2 = pygame.display.set_caption("FOOT©")
icon_32x32 = pygame.image.load("character.png").convert_alpha()
pygame.display.set_icon(icon_32x32)

fond = pygame.image.load("plage.jpg").convert()
fenetre.blit(fond, (0,0))

perso = pygame.image.load("character.png").convert_alpha()
perso = pygame.transform.scale(perso,(100,100))
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)



pygame.display.flip()

#Rafraîchissement
pygame.display.flip()

#Pour la fluidité du déplacement
pygame.key.set_repeat(400, 30)

#Texte
print("Vous voila dans fifa 84! vous pouvez déplacer le ballon à votre guise ! Bonne partie ! PS : pour ceux qui veulent la musique : https://www.youtube.com/watch?v=0FqrsW-zsxo "  )

#Boucle Infinie
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                position_perso = position_perso.move(0,5)
                print(position_perso)
            if event.key == K_LEFT:
                position_perso = position_perso.move(-5,0)
                print(position_perso)
            if event.key == K_UP:
                position_perso = position_perso.move(0,-5)
                print(position_perso)
            if event.key == K_RIGHT:
                position_perso = position_perso.move(5,0)
                print(position_perso)


#Re-collage
    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, position_perso.move(375,228)) # Collage du ballon au lancement.

#Rafeaîchissement
    pygame.display.flip()

#Permet de quitter la fenêtre
pygame.quit()