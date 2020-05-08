from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Couleur(models.Model):
    nom = models.CharField(max_length=8, verbose_name="couleur")

    def __str__(self):
        return self.nom

class Contrat(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom du contrat")
    coefficient = models.IntegerField(verbose_name="Coefficient multiplicateur")

    def __str__(self):
        return self.nom


class PointsAFaire(models.Model):
    nombre_bouts = models.IntegerField()
    points = models.IntegerField()

class Poignée(models.Model):
    nom = models.CharField(max_length=20)
    points = models.IntegerField()

    def __str__(self):
        return self.nom

class TarotPlayer(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    prises_totales = models.IntegerField(default=0)
    prise_petite = models.IntegerField(default=0)
    prise_garde = models.IntegerField(default=0)
    prise_garde_sans = models.IntegerField(default=0)
    prise_garde_contre = models.IntegerField(default=0)
    nombre_de_fois_appelé = models.IntegerField(default=0)

    def __str__(self):
        return self.player.username

class TarotGame(models.Model):
    name = models.CharField(max_length=200,verbose_name="Nom de la partie")
    date = models.DateField(default=timezone.now())
    player1 = models.ForeignKey(TarotPlayer, related_name="joueur1",on_delete=models.CASCADE, verbose_name="Joueur 1",default=False)
    player2 = models.ForeignKey(TarotPlayer, related_name="joueur2", on_delete=models.CASCADE, verbose_name="Joueur 2",default=False)
    player3 = models.ForeignKey(TarotPlayer, related_name="joueur3",  on_delete=models.CASCADE, verbose_name="Joueur 3",default=False)
    player4 = models.ForeignKey(TarotPlayer, related_name="joueur4", on_delete=models.CASCADE, verbose_name="Joueur 4",default=False)
    player5 = models.ForeignKey(TarotPlayer, related_name="joueur5", on_delete=models.CASCADE, verbose_name="Joueur 5",default=False)
    tours = models.IntegerField(default=0)

    def __str__(self):
        return "Partie du {0}".format(self.date)


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
    point_a_faire = models.OneToOneField(PointsAFaire,on_delete=models.CASCADE)

    def __str__(self):
        return self.position


