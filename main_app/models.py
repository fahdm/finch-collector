from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L','Lunch'),
    ('D','Dinner'),
)



# Create your models here.

class Cage(models.Model):
    name = models.CharField(max_length=12, default='')
    material = models.CharField(max_length=30)
    color = models.CharField(max_length=40)
    size = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('cages_detail', kwargs={'pk': self.id})
    


class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    count = models.IntegerField()
    cages = models.ManyToManyField(Cage)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )

    # create a finch_id FK

    finch = models.ForeignKey(
        Finch,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']




