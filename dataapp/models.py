from django.db import models

# Create your models here.
class Upload(models.Model):
    car = models.CharField(max_length=60)
    mpg = models.DecimalField(max_digits=5, decimal_places=1)
    cyl = models.IntegerField()
    cyl_disp = models.DecimalField(max_digits=5, decimal_places=1)
    horsep = models.DecimalField(max_digits=5, decimal_places=1)
    weight = models.DecimalField(max_digits=6, decimal_places=1)
    accel = models.DecimalField(max_digits=4, decimal_places=1)
    model = models.IntegerField()
    COUNTRIES = (
        (0, 'US'),
        (1, 'Europe'),
        (2, 'Japan'),
    )
    origin = models.IntegerField(choices=COUNTRIES)
