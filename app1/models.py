from django.db import models


class Major(models.Model):
    mj_name = models.CharField(max_length=100, blank=False)

    class Meta:
        verbose_name = "major"
        verbose_name_plural = "majors"

    def __str__(self):
        return self.mj_name


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

    st_id = models.BigIntegerField(unique=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.prefix_name}{self.fname} {self.lname}"