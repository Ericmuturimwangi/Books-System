from django.db import models


# defining a book model with fields for the title, author and pub date, and isbn number

class Book(models.Model):
    title = models.CharField(max_length= 100)
    author = models.CharField(max_length= 100)
    published_date = models.DateField ()
    isbn_number = models.CharField(max_length=13)

# returning self.title 
    def __str__(self):
        return self.title
 