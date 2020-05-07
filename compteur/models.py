from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Couleur(models.Model):
    nom = models.CharField(max_length=8,verbose_name="couleur")

    def __str__(self):
        return self.nom

class Contrat(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom du contrat")
    points = models.IntegerField(verbose_name="Points à réaliser par l'attaque")
    coefficient = models.IntegerField(verbose_name="Coefficient multiplicateur")

    def __str__(self):
        return self.nom

class Poignée(models.Model):
    nom = models.CharField(max_length=20)
    points = models.IntegerField()

    def __str__(self):
        return self.nom

class TarotPlayer(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()
    prises_totales = models.IntegerField()
    prise_petite = models.IntegerField()
    prise_garde = models.IntegerField()
    prise_garde_sans = models.IntegerField()
    prise_garde_contre = models.IntegerField()
    nombre_de_fois_appelé = models.IntegerField()

    def __str__(self):
        return self.player.username

class TarotGame(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(default=False)
    players = models.ManyToManyField(TarotPlayer)
    tours = models.IntegerField()

    def __str__(self):
        return self.date


class TarotTurn(models.Model):
    partie = models.ForeignKey(TarotGame,on_delete=models.CASCADE)
    position = models.IntegerField(verbose_name="Numéro du tour")
    joueur_preneur = models.OneToOneField(TarotPlayer,related_name="nom_preneur", on_delete=models.CASCADE,verbose_name="Nom du preneur")
    contrat = models.OneToOneField(Contrat, on_delete=models.CASCADE)
    joueur_appelé = models.OneToOneField(TarotPlayer,related_name="nom_appelé", on_delete=models.CASCADE,verbose_name="Nom du joueur appelé")
    défense = models.ManyToManyField(TarotPlayer,verbose_name="Liste des défenseurs")
    couleur_appelée = models.OneToOneField(Couleur,on_delete=models.CASCADE)
    petit = models.BooleanField(default=False, verbose_name="Petit au bout")
    poignée = models.OneToOneField(Poignée,on_delete=models.CASCADE)

    def __str__(self):
        return self.position


