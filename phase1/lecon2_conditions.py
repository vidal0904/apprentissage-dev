# Ce programme vise a comprendre les conditions de python

prix_unitaire = int(input("Quel est le prix unitaire ? ")) # Demander le prix et attendre la reponse
quantite = int(input("Quelle est la quantité ? "))
total_achetee = prix_unitaire * quantite

if total_achetee >= 10000:
  montant_remise = (total_achetee * 10) / 100
  total = total_achetee - montant_remise
  
elif total_achetee >= 5000:
    montant_remise = (total_achetee *5) / 100
    total = total_achetee - montant_remise
    

else:
   montant_remise = 0
   total = total_achetee 
   

reponse = input(" Avez-vous une carte de fidélité ? repondez simplement par :(oui/non). ")
if reponse == "oui" and total >= 5000:
   remise_fidelite = (total * 2) /100
   a_payer = total - remise_fidelite

   

else:
   remise_fidelite = 0
   a_payer = total
   print(f"Votre total d'achat est {total} CFA. ")


print("=" * 30)
print(f"Total d'achat    : {total_achetee} FCFA")
print(f"Remise montant   : {montant_remise} FCFA")
print(f"Remise fidélité  : {remise_fidelite} FCFA")
print(f"À payer          : {a_payer} FCFA")
print("=" * 30)

