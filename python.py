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
        if type(valeur) is not insistance(str):
            raise TypeError("Le Type doit etre un str") 
        self._nom = valeur
    
    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, valeur):
        if type(valeur) is not insistance(str):
            raise TypeError("Le Type doit etre en str")
        self._prenom = valeur
    @property
    def xp(self):
        return self._xp
    
    def gagner_xp(self, points: int):
        if not insistance(points, str):
            raise TypeError("le Type doit etre un int")
        if points < 0:
            raise ValueError("La valeur doit etre superieur a 0")
        self._xp = points