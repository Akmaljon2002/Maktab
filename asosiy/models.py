from django.contrib.auth.models import User
from django.db import models

class Fanlar(models.Model):
    nom = models.CharField(max_length=50)
    def __str__(self):
        return self.nom

class Oqituvchi(models.Model):
    fish = models.CharField(max_length=60)
    fan = models.ManyToManyField(Fanlar)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.fish

class Sinf(models.Model):
    id_sinf = models.PositiveSmallIntegerField(null=True, blank=True)
    bosqich = models.PositiveSmallIntegerField()
    rang = models.CharField(max_length=20)
    kurator = models.ForeignKey(Oqituvchi, on_delete=models.CASCADE)
    fan = models.ManyToManyField(Fanlar)
    def __str__(self):
        return f"{self.bosqich}-{self.rang}"

class Oquvchi(models.Model):
    fish = models.CharField(max_length=60)
    sinf = models.ForeignKey(Sinf, on_delete=models.CASCADE)

    def __str__(self):
        return self.fish

class Reyting_daftar(models.Model):
    oquvchi = models.ForeignKey(Oquvchi, on_delete=models.CASCADE)
    chorak_1 = models.PositiveSmallIntegerField()
    chorak_2 = models.PositiveSmallIntegerField()
    chorak_3 = models.PositiveSmallIntegerField()
    chorak_4 = models.PositiveSmallIntegerField()
    yillik  =models.PositiveSmallIntegerField()
    imtihon = models.PositiveSmallIntegerField()
    natija = models.CharField(max_length=50)
    oquv_yili = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.oquvchi}({self.oquv_yili})"


class Yangiliklar(models.Model):
    sarlavha = models.CharField(max_length=60)
    matn = models.TextField()
    rasm = models.FileField()
    sana = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.sarlavha

class Malumot(models.Model):
    sarlavha = models.CharField(max_length=60)
    bepul = models.BooleanField(default=False)
    rasm = models.FileField()

class MaktabMedia(models.Model):
    rasm = models.FileField()
    sarlavha = models.CharField(max_length=60)
    def __str__(self):
        return self.sarlavha

class Murojat(models.Model):
    ism = models.CharField(max_length=50)
    email = models.EmailField()
    tel = models.CharField(max_length=15)
    sarlavha = models.CharField(max_length=60)
    xabar = models.TextField()
    def __str__(self):
        return f"{self.ism}({self.email})"

