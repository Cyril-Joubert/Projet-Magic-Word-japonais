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

tab = []	# tableau taberu
tabFr = []	# tableau des fréquences détaillés 
fr = []		# tableau de transition pour le split
nb = []		# tableau des fréquences finales
smol = {}	# tableau associatif pour la structure finale

# On stock les formes de taberu en enlevant les \n
with open("taberu1Kanji.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line != "\n":
            lineNorm = line.strip("\n")
            if lineNorm not in tab: # structure conditionnelle pour supprimer les doublons
                tab.append(lineNorm)
	

"""
# génère un fichier avec seulement les formes de taberu
with open ("taberu1.txt", "w", encoding="utf-8") as f:
    for i in tab:
        f.write(i)
"""
dump = MeCab.Tagger("-Odump")

# Ici, on isole les fréquences finales dans un tableau nb qui est de même longueur que le tableau tab pour que les fréquences match avec les formes correspondantes
for i in range (0, len(tab)-1):
    tabFr.append(dump.parse(tab[i]))
    fr.append(tabFr[i].split(" "))
    nb.append(fr[i][len(fr[i])-1])

# On utilise un tableau associatif car la structure est plus pertinante
for i in range(0, len(tab)-1):
    if tab[i] not in smol:
        smol.update({tab[i]: nb[i]})

# On concatène les formes(clé) et les fréquences(valeur) dans un fichier taberuFinal.txt séparé par une tabulation et on les tris par ordre décroissant
with open ("FormeFinalKanji.txt", "w", encoding="utf-8") as f:
    for i, j in sorted(smol.items(), key=lambda t: t[1], reverse=True):
        f.write(i + "	" + j)

# problème : 3 premières entrées sont les dernières