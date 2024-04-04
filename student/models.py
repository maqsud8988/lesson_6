from django.db import models

class Address(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Role(models.TextChoices):
    b = ("b", "B")
    m = ("m", "M")
    p = ("ph", "PH")

class Student(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Role.choices, default=Role.b)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

