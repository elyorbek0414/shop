from django.db import models


class Mahsulot(models.Model):
    nomi = models.CharField(max_length=100)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    miqdori = models.IntegerField()
    chegirma_foizi = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    chegirma_muddati = models.DateField(null=True, blank=True)

    @property
    def chegirma(self):
        if self.chegirma_foizi is not None and self.chegirma_muddati is not None:
            return f"{self.chegirma_foizi}% chegirma {self.chegirma_muddati}gacha"
        else:
            return "Chegirma mavjud emas"


class Chegirma(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    chegirma_foizi = models.DecimalField(max_digits=5, decimal_places=2)
    chegirma_muddati = models.DateField()


class Buyurtma(models.Model):
    buyurtma_id = models.AutoField(primary_key=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdori = models.IntegerField()
    chegirma_foizi = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    chegirma_muddati = models.DateField(blank=True)
    summa = models.DecimalField(max_digits=10, decimal_places=2)
    qabul_sana = models.DateField()


