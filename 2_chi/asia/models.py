from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Country(models.Model):
    category = models.ForeignKey(to = 'Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    population = models.ImageField()
    body = models.TextField()
    money = models.CharField(max_length=20)
    image = models.ImageField(upload_to='country/', blank=True, null=True)
    class Meta:
        db_table = 'country'

    def __str__(self):
        return f"{self.category.name} {self.population}"