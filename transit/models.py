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
    name = models.CharField(max_length=40, null=True)
    street = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=2, null=True)
    zip = models.IntegerField(null=True)
    code = models.CharField(max_length=3, unique=True, null=True)
    line = models.ForeignKey(Line, on_delete=models.CASCADE, related_name='primary_line')
    longitude = models.DecimalField(decimal_places=6, max_digits=9, null=True)
    latitude = models.DecimalField(decimal_places=6, max_digits=9, null=True)
    line2 = models.ForeignKey(Line, on_delete=models.CASCADE, null=True, blank=True, related_name='secondary_line')
    line3 = models.ForeignKey(Line, on_delete=models.CASCADE, null=True, blank=True, related_name='tertiary_line')
    code2 = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.code