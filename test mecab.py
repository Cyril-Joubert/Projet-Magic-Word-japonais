#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

# Simple test sur une petite partie
import MeCab


dump = MeCab.Tagger("-Odump")
print(dump.parse("食べます"))							# 10 253
print(dump.parse("食べろう"))							# 17 390
print(dump.parse("食べませんでした"))					# 14 031
print(dump.parse("食べなかった"))						# 14 712
print(dump.parse("食べさせます"))						# 14 536
print(dump.parse("食べさせられません"))				# 19 647
print(dump.parse("食べられそうでしたろう"))				# 24 859
print(dump.parse("食べぬ"))							# 13 413
print(dump.parse("食べさされやすくなさそうでしたり"))	# 38 599


# ~ 食べます							10 253			
# ~ 食べぬ							13 413
# ~ 食べませんでした					14 031
# ~ 食べさせます						14 536
# ~ 食べなかった						14 712
# ~ 食べろう							17 390
# ~ 食べさせられません					19 647
# ~ 食べられそうでしたろう				24 859
# ~ 食べさされやすくなさそうでしたり		38 599"""


import MeCab
from mergeSort import * # récupère les fonctions merge et mergesort

tab = []	# tableau taberu
tabFr = []	# tableau des fréquences détaillés 
fr = []		# tableau de transition pour le split
nb = []		# tableau des fréquences finales
smolList = [] #tableau de tuple pour utiliser l'algorithme de tri

'''fonction qui permet d'ouvrir les fichier contenant les formes et enlève les \n 
    il prend en entrée le nom du fichier à ouvrir, donne en sortie le tableau contenant une forme par ligne'''
def ouvrirNorm(handle):
    # On stock les formes de taberu en enlevant les \n
    with open( handle, "r", encoding="utf-8") as f:
        for line in f:
            if line != "\n":
                lineNorm = line.strip("\n")
                if lineNorm not in tab: # structure conditionnelle pour supprimer les doublons
                    tab.append(lineNorm)
    return tab

''' fonction qui prend en entrée, le nom du fichier qui contiendra la sortie et le dictionnaire forme-fréquence
    elle permet d'exporter nos données dans un fichier.
'''
def closeExport(handle, smol):
    # On concatène les formes(clé) et les fréquences(valeur) dans un fichier taberuFinal.txt séparé par une tabulation et on les tris par ordre décroissant
    with open (handle, "w", encoding="utf-8") as f:
        for i, j in sorted(smol.items(), key=lambda t: t[1], reverse=True):
            f.write(i + "   " + j)
    return


''' Fonction qui calcule les fréquences de toutes les entrées, 
prend en entrée le tableau des formes à analyser 
en sortie renvoie un dictionnaire avec forme et fréquence associée.
'''
def wordFreq(tableau):
    dump = MeCab.Tagger("-Odump")
    # Ici, on isole les fréquences finales dans un tableau nb qui est de même longueur que le tableau tab pour que les fréquences match avec les formes correspondantes
    for i in range (0, len(tableau)-1):
        tabFr.append(dump.parse(tableau[i]))
        fr.append(tabFr[i].split(" "))
        nb.append(fr[i][len(fr[i])-1])

    # On utilise un tableau associatif car la structure est plus pertinante
    smol = {}   # tableau associatif pour la structure finale
    for i in range(0, len(tableau)-1):
        if tableau[i] not in smol:
            smol.update({tableau[i]: nb[i]})
    return smol


##############  PYTHON #################
# #On créé une liste de tuple à partir du dictionnaire pour pouvoir y appliquer un MergeSort
# smolList = list(smol.items())
# print(smolList)
# #On utilise un algorithme de tri de type mergeSort pour trier toutes fréquences par ordre décroissant

# result = mergeSortDesc(smolList)
# # print(result)

#######################################



    #Ici, on ouvre les 2 textes qui contenaient les entrée avec et sans Kanji.
tabKanji = ouvrirNorm("taberu1Kanji.txt")
tabNorm = ouvrirNorm("taberu1.txt")

    #ici on calcule les fréquences des tableaux d'entrée.
FreqKanji = wordFreq(tabKanji) 
FreqSans = wordFreq(tabNorm) 

    #ici on envoie le dictionnaire dans un fichier, c'est la forme finale de notre code.
closeExport(FormeFinalKanji.txt)
closeExport(FormeFinalKanji.txt)


# problème : 3 premières entrées sont les dernières