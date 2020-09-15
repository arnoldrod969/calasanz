from django.db import models
from django.contrib.auth.models import User


class Nature(models.Model):
    CHOICES = [
        ('Constitution', 'Constitution'),
        ('Loi', 'Loi'),
        ('Décret', 'Décret'),
        ('Programme/plan', 'Programme/plan')
    ]
    type = models.CharField(max_length=15, choices=CHOICES,
                            default='Constitution', verbose_name='Type de document')

    def __str__(self):
        return self.type


class Region(models.Model):
    CHOICES = [
        ('AF', 'Afrique'),
        ('AC', 'Amerique latine et Caraibes'),
        ('AP', 'Asie et Pacifique'),
        ('EA', 'Etats arabes'),
        ('EU', 'Europe'),
        ('AM', 'Amerique du Nord'),
    ]
    region = models.CharField(max_length=255, choices=CHOICES, default='AF')

    def __str__(self):
        return self.region


class Document(models.Model):
    LANGUAGES_CHOICES = [
        ('FR', 'Français'),
        ('EN', 'Anglais'),
        ('SP', 'Espagnol'),
        ('PE', 'Portugais'),
        ('AL', 'Allemand'),
        ('CH', 'Chinois'),
        ('AR', 'Arabe'),
        ('RU', 'Russe'),
        ('IT', 'Italien'),
        ('AU', 'Autre')
    ]
    titre = models.CharField(max_length=255, verbose_name='Nom du document')
    auteur = models.CharField(max_length=255)
    langue = models.CharField(max_length=100, choices=LANGUAGES_CHOICES, default='FR')
    source = models.FileField(upload_to="documents/", blank=True, null=True, max_length=255)
    date_pub = models.DateField(auto_now=False)
    reference = models.CharField(blank=True, null=True, max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nature = models.ForeignKey(Nature, on_delete=models.CASCADE)

    class Meta:
        ordering = ['titre']

    def __str__(self):
        return self.titre


class Pays(models.Model):
    pays = models.CharField(max_length=255)
    continent = models.ForeignKey(Region, on_delete=models.CASCADE)
    documents = models.ManyToManyField(Document)

    def __str__(self):
        return self.pays
