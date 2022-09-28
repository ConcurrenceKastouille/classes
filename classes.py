# Création d'une classe (commence toujours par une majuscule)

class Client:
    pass  #permet de passer la ligne sans donner d'instructions

# Création d'objets faisant parti de la classe

MrX = Client()
MmeY = Client()

# Création d'une classe avec 3 attributs

class Client2:
    def __init__(self):  #fonction "constructeur"
        self.nom = "Jean"
        self.prenom = "Michel"
        self.date = "03/05/1969 "

MrV = Client2()
MmeP = Client2()

    # Tout le monde a : nom -> Jean / prenom -> Michel / date -> 03/05/1969

# Création d'une classe avec 3 attributs personnalisables pour chaque objet

class Client3:
    def __init__(self,sonnom,sonprenom,sadate):
        self.nom = sonnom
        self.prenom = sonprenom
        self.date = sadate

MrA = Client3("Kroaba","Raoul","26/03/1985")
MrB = Client3("Karol","Edward","05/06/2001")

    # Testez ! Tappez par exemple "MrA.nom" dans la console
    # Attention ! On peut modifier les valeurs de MrA ou MrB avec "MrA.nom = "Mok"
    # Pour remédier à cela il faut rendre les attributs "privées"

# Création d'une classe avec 3 attributs personnalisables privés pour chaque objet

class Client4:
    def __init__(self,sonnom,sonprenom,sadate):
        self.__nom = sonnom
        self.__prenom = sonprenom
        self.__date = sadate

MrN = Client4("Kroaba","Raoul","26/03/1985")
MrM = Client4("Karol","Edward","05/06/2001")

    # Le problème est qu'il est désormais impossible de lire ces attributs privés
    # Pour remédier à ce problème nous allons devoir créer des "méthodes"

# Création

class Client5:
    def __init__(self,sonnom,sonprenom,sadate):
        self.__nom = sonnom
        self.__prenom = sonprenom
        self.__date = sadate

    def Getnom(self):       #Méthode accesseur (permet de voir l'attribut)
        return self.__nom

    def Getprenom(self):
        return self.__prenom

    def Getdate(self):
        return self.__date

    def Setnom(self,modif):    #Méthode mutateur (permet de modifier l'attribut)
        self.__nom = modif

    def Setprenom(self,modif):
        self.__prenom = modif

    def Setdate(self,modif):
        self.__date = modif

Mr1 = Client5("Kroaba","Raoul","26/03/1985")
Mr2 = Client5("Karol","Edward","05/06/2001")

    # Il existe énormément de méthodes qui permettent de faire pleins de
    # choses différentes, à vous de vous documenter !
    # Amusez vous bien :)


