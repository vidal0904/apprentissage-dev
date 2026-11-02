# Ce programme est particulierement ecrit pour calculer l'année de naissance d'un individu a partir de sa date de naissance 
# Ce programme permet egalement de calculer le prix total d'un article achété en multipliant le prix unitaire avec la quantité

annee_naissance = input("Quelle est ton année de naissance ? " ) #Demander et attendre la réponse
annee = int(annee_naissance)
age = 2026 - annee
print(f"Vous avez {age} ans" )

prix_article = input("Quel est le prix de l'article ? " ) # Demander le prix et attendre la reponse 
prix = int(prix_article)
quantite_choisie = input("Quelle est la quantité choisie ?" )
quantite = int(quantite_choisie)
cout_total = prix * quantite

print(f"{quantite} articles (s) à {prix} = {cout_total} FCFA")

