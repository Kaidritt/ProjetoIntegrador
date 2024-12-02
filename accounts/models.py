from django.db import models

# Create your models here.
#class Subscription(models.Model):
#    email = models.EmailField(unique=True)
#
#    def __str__(self):
#        return self.email

class Residuo(models.Model):
    tipoResiduo = models.CharField(max_length=100)
    descricao = models.TextField()
    diretrizes = models.TextField()
    imagem = models.ImageField(upload_to='residuos_images/', null=True, blank=True)

    def __str__(self):
        return self.tipoResiduo

class PontoColeta(models.Model):
    endereco = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    tipo_residuo = models.ForeignKey(Residuo, on_delete=models.CASCADE)
    horario = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.endereco} - {self.tipo_residuo.tipoResiduo}"