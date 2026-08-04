from django.db import models


class Student(models.Model):

    PREFIX_NAME = [
        ('นาย', 'นาย'),
        ('นางสาว', 'นางสาว'),
        ('นาง', 'นาง'),
    ]

    prefix_name = models.CharField(
        max_length=10,
        choices=PREFIX_NAME
    )

    st_id = models.CharField(max_length=20)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prefix_name}{self.fname} {self.lname}"