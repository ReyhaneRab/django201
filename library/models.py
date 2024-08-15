from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateTimeField()
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name, self.last_name

    class Meta:
        verbose_name = 'author'
        ordering = ['first_name']


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'category'
        ordering = ['category_name']


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_book')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_book')
    publication_date = models.DateTimeField()
    isbn = models.CharField(max_length=100, unique=True)
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'book'
        ordering = ['-publication_date']
