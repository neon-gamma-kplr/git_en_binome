class CompteBancaire:
    def __init__(self, numero_compte, solde=0):
        self.numero_compte = numero_compte
        self.solde = solde
    
    def deposer(self, montant):
        self.solde += montant
    
    def retirer(self, montant):
        if self.solde >= montant:
            self.solde -= montant
        else:
            print("Solde insuffisant.")
    
    def transferer(self, compte_destinataire, montant):
        if self.solde >= montant:
            self.solde -= montant
            compte_destinataire.deposer(montant)
        else:
            print("Solde insuffisant.")

def gestion_compte_bancaire():
    compte1 = CompteBancaire("123456", 5000)
    compte2 = CompteBancaire("789012", 3000)

    print("Bienvenue dans le système de gestion des comptes bancaires.")

    while True:
        print("\nQue souhaitez-vous faire ?")
        print("1. Déposer de l'argent")
        print("2. Retirer de l'argent")
        print("3. Transférer de l'argent")
        print("4. Quitter")

        choix = input("Votre choix (1-4) : ")

        if choix == "1":
            montant = float(input("Montant à déposer : "))
            numero_compte = input("Numéro de compte bancaire : ")

            if numero_compte == compte1.numero_compte:
                compte1.deposer(montant)
                print(f"{montant}€ ont été déposés sur le compte {compte1.numero_compte}.")
            elif numero_compte == compte2.numero_compte:
                compte2.deposer(montant)
                print(f"{montant}€ ont été déposés sur le compte {compte2.numero_compte}.")
            else:
                print("Numéro de compte invalide.")

        elif choix == "2":
            montant = float(input("Montant à retirer : "))
            numero_compte = input("Numéro de compte bancaire : ")

            if numero_compte == compte1.numero_compte:
                compte1.retirer(montant)
                print(f"{montant}€ ont été retirés du compte {compte1.numero_compte}.")
            elif numero_compte == compte2.numero_compte:
                compte2.retirer(montant)
                print(f"{montant}€ ont été retirés du compte {compte2.numero_compte}.")
            else:
                print("Numéro de compte invalide.")

        elif choix == "3":
            montant = float(input("Montant à transférer : "))
            numero_compte_source = input("Numéro de compte bancaire source : ")
            numero_compte_destinataire = input("Numéro de compte bancaire destinataire : ")

            if numero_compte_source == compte1.numero_compte and numero_compte_destinataire == compte2.numero_compte:
                compte1.transferer(compte2, montant)
                print(f"{montant}€ ont été transférés du compte {compte1.numero_compte} au compte {compte2.numero_compte}.")
            elif numero_compte_source == compte2.numero_compte and numero_compte_destinataire == compte1.numero_compte:
                compte2.transferer(compte1, montant)
                print(f"{montant}€ ont été transférés du compte {compte2.numero_compte} au compte {compte1.numero_compte}.")
            else:
                print("Numéros de compte invalides.")

        elif choix == "4":
            print("Merci d'avoir utilisé notre système de gestion des comptes bancaires. Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")


if __name__ == "__main__":
    gestion_compte_bancaire()
