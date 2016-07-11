# Edge_detection_python3_OpenCv3
this is a python project that consists of detecting edges of a white board and recreating a new improoved image of the white board
Whiteboard Scanning and Image Enhancement :


Ce projet est un Package Python qui sert à traiter le problème du "Whiteboard Scanning and Image Enhancement".
Le Package est composé de 5 Classes :
- imageProp
- Sobel
- Hough
- LinesHandler
- Perspective


1- imageProp :

Cette classe permet de récupérer quelques propriétés de l'image d'entrée, telles que la longueur, la largeur et la diagonale.


2- Sobel :

Cette classe applique le filtre Sobel:
- Elle commence par supprimer le bruit de l'image.
- Elle convertit l'image en niveaux de gris.
- Elle applique une égalisation de l'histogramme pour mieux faire apparaitre les contours.
- Puis elle applique un filtre Sobel horizontal pour détecter les contours verticaux, et un filtre Vertical pour détecter les contours horizontaux.
- Elle fusionne les deux images produites pour avoir tous les contours.


3- Hough :

Elle prend en entrée deux images; la première correspond à l’image en noir et blanc avec les contours détectés et la deuxième correspond à l'image originale.
La fonction drawLinesP retourne des segments de lignes et l'image originale avec les segments représentés dessus.


4- LinesHandler :

Cette classe traite les segments de lignes retournés par la fonction drawLines de la classe Hough.
Elle découpe l'image originale en 4 morceaux égaux et tente de trouver un point correspondant à un coin du tableau dans chacun de ces morceaux.


5- Perspective :

Cette classe applique une transformation géométrique sur l'image en utilisant les quatre points retournés par LinesHandler de façon à avoir une vue de face sur le tableau.


Conclusion :

Ce travail est le fruit de deux mois de réflexion sur le sujet. Nous avons pris beaucoup de chemins avant d'arriver à ce résultat (qui n'est pas le plus optimal mais fonctionne en grande partie).
Ce projet a rendu plus concrets les cours de Python et en Traitements d'images sans lesquels ce projet n'aurait jamais vu jour.
