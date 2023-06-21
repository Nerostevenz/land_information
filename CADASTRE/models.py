from django.db import models

class Plan(models.Model):
    plannumber = models.CharField(db_column='PlanNumber', primary_key=True, max_length=50)  # Field name made lowercase.
    area = models.FloatField(db_column='Area', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    surveyor = models.CharField(db_column='Surveyor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coordinatesystem = models.CharField(db_column='CoordinateSystem', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plan'
    def __str__(self):
        return self.plannumber


from django.core.validators import MinValueValidator, RegexValidator

class Coordinate(models.Model):
    id = models.BigAutoField(primary_key=True)
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE, blank=True, null=True)
    pillarnumber = models.CharField(max_length=50, blank=False, validators=[
        RegexValidator(r'^[a-zA-Z0-9]+$', message='Pillar number must be alphanumeric')
    ])
    eastings = models.FloatField(null=False, validators=[
        MinValueValidator(0, message='Eastings must be a positive number')
    ])
    northings = models.FloatField(null=False, validators=[
        MinValueValidator(0, message='Northings must be a positive number')
    ])

    class Meta:
        managed = False
        db_table = 'coordinate'
    def __str__(self):
        return self.pillarnumber