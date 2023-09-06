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
