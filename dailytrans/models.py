from django.db import models


# Create your models here.


class MasterCategory(models.Model):
    masterid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class PaymentMode(models.Model):
    modeid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Details(models.Model):
    detailsid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Daily(models.Model):
    transid = models.AutoField(primary_key=True)
    transdate = models.DateField()
    transdetails = models.ForeignKey(Details, on_delete=models.CASCADE)
    transcategory = models.ForeignKey(MasterCategory, on_delete=models.CASCADE)
    transmode = models.ForeignKey(PaymentMode, on_delete=models.CASCADE)
    transsubdetails = models.CharField(max_length=100, blank=False, null=False)
    transamount = models.DecimalField(max_digits=7, decimal_places=2)
    objects = models.Manager()

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (
            self.transid,
            self.transdate,
            self.transdetails,
            self.transcategory,
            self.transmode,
            self.transsubdetails,
            self.transamount)