#!/usr/bin/env python
# coding: utf-8

# In[43]:


original_string = "abracadabrada"
tableau = [[caractere] for caractere in original_string]
print(tableau)


# In[44]:


original_string = "abracadabrada"
tableau = []
for caractere in original_string:
    tableau.append([caractere])
tableau.sort()
print(tableau)


# In[45]:


original_string = "abracadabrada"

# Compter les occurrences de chaque caractère
occurrences = {}
for caractere in original_string:
    if caractere in occurrences:
        occurrences[caractere] += 1
    else:
        occurrences[caractere] = 1

# Calculer la probabilité d'apparition de chaque caractère
total_caracteres = len(original_string)
probabilites = {caractere: nb_occurrences / total_caracteres for caractere, nb_occurrences in occurrences.items()}

# Créer le tableau 2D
tableau = [[caractere, probabilites[caractere]] for caractere in probabilites.keys()]

# Trier le tableau par ordre de probabilité décroissante
for i in range(len(tableau)):
    for j in range(i+1, len(tableau)):
        if tableau[j][1] > tableau[i][1]:
            tableau[i], tableau[j] = tableau[j], tableau[i]

print(tableau)


# In[46]:


original_string = "abracadabrada"

# Compter les occurrences de chaque caractère
occurrences = {}
for caractere in original_string:
    if caractere in occurrences:
        occurrences[caractere] += 1
    else:
        occurrences[caractere] = 1

# Calculer la probabilité d'apparition de chaque caractère
total_caracteres = len(original_string)
probabilites = {caractere: nb_occurrences / total_caracteres for caractere, nb_occurrences in occurrences.items()}

# Créer le tableau 2D
tableau = [[caractere, probabilites[caractere]] for caractere in probabilites.keys()]

# Trier le tableau par ordre de probabilité décroissante
for i in range(len(tableau)):
    for j in range(i+1, len(tableau)):
        if tableau[j][1] > tableau[i][1]:
            tableau[i], tableau[j] = tableau[j], tableau[i]

# Sommation des deux plus petites probabilités
somme_proba = tableau[-1][1] + tableau[-2][1]
tableau = tableau[:-2]
tableau.append(["Autres", somme_proba])

# Trier le tableau par ordre de probabilité décroissante
for i in range(len(tableau)):
    for j in range(i+1, len(tableau)):
        if tableau[j][1] > tableau[i][1]:
            tableau[i], tableau[j] = tableau[j], tableau[i]

print(tableau)


# In[47]:


original_string = "abracadabrada"

# Compter les occurrences de chaque caractère
occurrences = {}
for caractere in original_string:
    if caractere in occurrences:
        occurrences[caractere] += 1
    else:
        occurrences[caractere] = 1

# Calculer la probabilité d'apparition de chaque caractère
total_caracteres = len(original_string)
probabilites = {caractere: nb_occurrences / total_caracteres for caractere, nb_occurrences in occurrences.items()}

# Créer le tableau 2D
tableau = [[caractere, probabilites[caractere]] for caractere in probabilites.keys()]

# Trier le tableau par ordre de probabilité décroissante
for i in range(len(tableau)):
    for j in range(i+1, len(tableau)):
        if tableau[j][1] > tableau[i][1]:
            tableau[i], tableau[j] = tableau[j], tableau[i]

# Afficher tableau avant sommer
print("Tableau avant sommer: ")
print(tableau)

# Sommation des deux plus petites probabilités
somme_proba = tableau[-1][1] + tableau[-2][1]
tableau = tableau[:-2]
tableau.append(["Autres", somme_proba])

# Trier le tableau par ordre de probabilité décroissante
for i in range(len(tableau)):
    for j in range(i+1, len(tableau)):
        if tableau[j][1] > tableau[i][1]:
            tableau[i], tableau[j] = tableau[j], tableau[i]

# Afficher tableau après sommer
print("Tableau après sommer: ")
print(tableau)


# In[48]:


original_string = "abracadabrada"

# Compter les occurrences de chaque caractère
occurrences = {}
for caractere in original_string:
    if caractere in occurrences:
        occurrences[caractere] += 1
    else:
        occurrences[caractere] = 1

# Calculer la probabilité d'apparition de chaque caractère
total_caracteres = len(original_string)
probabilites = {caractere: nb_occurrences / total_caracteres for caractere, nb_occurrences in occurrences.items()}

# Créer le tableau 2D
tableau = [[caractere, probabilites[caractere]] for caractere in probabilites.keys()]

while len(tableau) > 2:
    # Trier le tableau par ordre de probabilité décroissante
    for i in range(len(tableau)):
        for j in range(i+1, len(tableau)):
            if tableau[j][1] > tableau[i][1]:
                tableau[i], tableau[j] = tableau[j], tableau[i]

    # Afficher tableau avant sommer
    print("Tableau avant sommer: ")
    print(tableau)

    # Sommation des deux plus petites probabilités
    somme_proba = tableau[-1][1] + tableau[-2][1]
    tableau = tableau[:-2]
    tableau.append(["Autres", somme_proba])

# Trier le tableau final par ordre de probabilité décroissante
for i in range(len(tableau)):
    for j in range(i+1, len(tableau)):
        if tableau[j][1] > tableau[i][1]:
            tableau[i], tableau[j] = tableau[j], tableau[i]

# Afficher tableau final
print("Tableau final: ")
print(tableau)


# In[49]:


original_string = "abracadabrada"

# Compter les occurrences de chaque caractère
occurrences = {}
for caractere in original_string:
    if caractere in occurrences:
        occurrences[caractere] += 1
    else:
        occurrences[caractere] = 1

# Calculer la probabilité d'apparition de chaque caractère
total_caracteres = len(original_string)
probabilites = {caractere: nb_occurrences / total_caracteres for caractere, nb_occurrences in occurrences.items()}

# Créer le tableau 2D
tableau = [[caractere, probabilites[caractere]] for caractere in probabilites.keys()]

while len(tableau) > 2:
    # Trier le tableau par ordre de probabilité décroissante
    for i in range(len(tableau)):
        for j in range(i+1, len(tableau)):
            if tableau[j][1] > tableau[i][1]:
                tableau[i], tableau[j] = tableau[j], tableau[i]

    # Afficher tableau avant sommer
    print("Tableau avant sommer: ")
    print(tableau)

    # Sommation des deux plus petites probabilités
    somme_proba = tableau[-1][1] + tableau[-2][1]
    caracteres_somme = [tableau[-1][0], tableau[-2][0]]
    tableau = tableau[:-2]
    tableau.append([caracteres_somme, somme_proba])

# Trier le tableau final par ordre de probabilité décroissante
for i in range(len(tableau)):
    for j in range(i+1, len(tableau)):
        if tableau[j][1] > tableau[i][1]:
            tableau[i], tableau[j] = tableau[j], tableau[i]

# Afficher tableau final
print("Tableau final: ")
print(tableau)


# In[56]:


original_string = "abracadabrada"

# Compter les occurrences de chaque caractère
occurrences = {}
for caractere in original_string:
    if caractere in occurrences:
        occurrences[caractere] += 1
    else:
        occurrences[caractere] = 1

# Calculer la probabilité d'apparition de chaque caractère
total_caracteres = len(original_string)
probabilites = {caractere: nb_occurrences / total_caracteres for caractere, nb_occurrences in occurrences.items()}

# Créer le tableau 2D
tableau = [[caractere, probabilites[caractere]] for caractere in probabilites.keys()]

# Enregistrer les codes Huffman pour chaque caractère dans un dictionnaire
codes_huffman = {caractere: "" for caractere in probabilites.keys()}

while len(tableau) > 2:
    # Trier le tableau par ordre de probabilité décroissante
    for i in range(len(tableau)):
        for j in range(i+1, len(tableau)):
            if tableau[j][1] > tableau[i][1]:
                tableau[i], tableau[j] = tableau[j], tableau[i]

    # Afficher tableau avant sommer
    print("Tableau avant sommer: ")
    print(tableau)

    # Sommation des deux plus petites probabilités
    somme_proba = tableau[-1][1] + tableau[-2][1]
    caractere1 = tableau[-1][0]
    caractere2 = tableau[-2][0]
    tableau = tableau[:-2]
    tableau.append([caractere1 + caractere2, somme_proba])

    # Mettre à jour les codes Huffman pour les deux derniers caractères
    codes_huffman[caractere1] = "0" + codes_huffman[caractere1]
    codes_huffman[caractere2] = "1" + codes_huffman[caractere2]

# Afficher les codes Huffman
print("Codes Huffman: ")
print(codes_huffman)


# In[ ]:




