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
        

class GroupeTP():
    def __init__(self, prof, participants):
        self._prof = prof
        self._participants = participants
    
    @property
    def prof(self):
        return self._prof

    @prof.setter
    def prof(self, nouveau_prof):
        if not isinstance(nouveau_prof, Prof):
            raise TypeError("La valeur doit etre un prof")
        self._prof = nouveau_prof

    @property
    def participants(self):
        return self._participants

    @participants.setter
    def participants(self, nouveau_participants):
        if not isinstance(nouveau_participants, list):
            raise TypeError("Le participants doit etre une list")
        if len (nouveau_participants) < 2:
            raise ValueError("La liste doit contenir au moins 2 personnes")
        for participants in nouveau_participants:
            if not isinstance(participants, Personne):
                raise TypeError("Le participants doit etre un Personne")
        self._participants = nouveau_participants

        def expliquer_la_prof(self):
            for participants in self.participants:
                self.prof.expliquer_la_poo(participants)
            
        def pause_cafe(self) -> None:
            for i in range(5):
                p1, p2 = random.sample(self.participants, 2)
                if isinstance(p1, Etudiant) and isinstance(p2, Etudiant):
                    p1.entraide(p2)
            
        def faire_une_seance(self) -> None:
            self.expliquer_la_prof()
            self.pause_cafe()
            self.expliquer_la_prof()

        def niveau_minimum(self) -> int:
            minimum = self.participants[0]._xp
            for participants in self.participants:
                if participants._xp < self.participants:
                    minimum = participants._xp
            return minimum

        def bourriner(self, objectif: int):
            while self.niveau_minimum < objectif:
                self.faire_une_seance