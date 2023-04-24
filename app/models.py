from django.db import models

# Create your models here.

class emp(models.Model):
    EMPNO = models.IntegerField(primary_key=True)
    ENAME = models.CharField(max_length=10)

    class Meta:
        db_table = 'emp'


class night_pharmacy(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    tel = models.CharField(max_length=10)

    class Meta:
        db_table = 'night_pharmacy'


class accident(models.Model):
    ID = models.IntegerField(primary_key=True)
    YEAR = models.CharField(max_length=10)
    AMPM = models.CharField(max_length=10)
    WEEK = models.CharField(max_length=10)
    DIE = models.IntegerField()
    AREA1 = models.CharField(max_length=10)
    AREA2 = models.CharField(max_length=10)
    KIND = models.CharField(max_length=10)

    class Meta:
        db_table = 'accident'