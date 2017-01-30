from django.db import models


class DatabaseObject(models.Model):
    '''Represents a database object containing a name and an id (inherited)'''
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
