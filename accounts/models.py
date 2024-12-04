from django.db import models
from geopy.geocoders import Nominatim

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
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    tipos_residuo = models.ManyToManyField(Residuo, related_name='pontos_coleta')

    def __str__(self):
        return f"{self.endereco}"

    def save(self, *args, **kwargs):
        if self.endereco and (self.latitude is None or self.longitude is None):
            # Geocode the address
            geolocator = Nominatim(user_agent="myApp")
            location = geolocator.geocode(self.endereco)
            if location:
                self.latitude = location.latitude
                self.longitude = location.longitude
        super(PontoColeta, self).save(*args, **kwargs)