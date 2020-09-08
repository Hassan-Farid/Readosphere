from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=255)
    author_info = models.TextField(blank=True, null=True)
    profile = models.FileField(upload_to='author/')    
    
    def __str__(self):
        return self.author_name

    class Meta:
        db_table = 'authors'

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=255)
    publisher_loc = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.publisher_name
    
    class Meta:
        db_table = 'publishers'

class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=45)
    isbn = models.IntegerField()
    language = models.CharField(max_length=45, blank=True, null=True)
    edition = models.CharField(max_length=45, blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    cover = models.FileField(upload_to='cover/')    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'books'
