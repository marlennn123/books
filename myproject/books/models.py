from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateTimeField(null=True, blank=True)
    pages = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    have = models.BooleanField(default=True)

    def __str__(self):
        return self.title