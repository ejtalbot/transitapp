from django.db import models

LINE_COLORS = (
    ('GR', 'Green'),
    ('BL', 'Blue'),
    ('SV', 'Silver'),
    ('RD', 'Red'),
    ('OR', 'Orange'),
    ('YL', 'Yellow')
)

class Line(models.Model):
    name = models.CharField(max_length=2, unique=True, choices=LINE_COLORS)
    color = models.CharField(max_length=6, null=True)
    start_station = models.CharField
    end_station = models.CharField

    def __str__(self):
        return self.color

class Station(models.Model):
    name = models.CharField
    city = models.CharField
    state = models.CharField
    zip = models.IntegerField
    code = models.CharField(max_length=3, unique=True, null=True)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)