import random


class Personne :
    def __init__(self, nom, prenom):
        self._prenom = prenom
        self._nom = nom
        self._xp = 0
    def __str__(self):
        return f"nom: {self._nom}, Prenom : {self._prenom}, xp: {self._xp}"

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, valeur):
        if not isinstance(valeur, str):
            raise TypeError("Le Type doit etre un str") 
        self._nom = valeur
    
    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, valeur):
        if not isinstance(valeur, str):
            raise TypeError("Le Type doit etre en str")
        self._prenom = valeur
    @property
    def xp(self):
        return self._xp
    
    def gagner_xp(self, points: int):
        if not isinstance(points, int):
            raise TypeError("le Type doit etre un int")
        if points < 0:
            raise ValueError("La valeur doit etre superieur a 0")
        self._xp += points



class Etudiant(Personne):
    def __init__(self, nom, prenom, annee):
        super().__init__(nom, prenom)
        if not isinstance(annee, int):
            raise TypeError("Le Type doit etre un str")
        if not 1 <= annee <= 3:
        #if annee < 1 or annee > 3:
            raise ValueError("La valeur doit etre compris entre 1 et 3")
        self._annee = annee


    def __str__(self):
        return f"nom: {self._nom}, Prenom : {self._prenom}, annee: {self._annee} "

    def gagner_xp(self, points: int):
        super().gagner_xp(points * (self._annee + 1))


    def entraide(self, autre_etu: Etudiant):
        if self._xp > autre_etu._xp:
            self.gagner_xp(1)
            autre_etu.gagner_xp(random.randint(1, 3))

        elif self._xp < autre_etu._xp:
            autre_etu.gagner_xp(1)
            self.gagner_xp(random.randint(1, 3))


class Prof(Personne):
    def __init__(self,nom, prenom):
        super().__init__(nom, prenom)
        self._xp = 10000
    
    def expliquer_la_poo(self, p: Personne):
        if not isinstance(p, Personne):
            raise TypeError("P doit etre une personne")
        self.gagner_xp(1)
        p.gagner_xp(random.randint(8, 12))
        