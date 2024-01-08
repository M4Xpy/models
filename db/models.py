from django.db import models


# class Band(models.Model):
#     name = models.CharField(max_length=63, )
#     country = models.CharField(max_length=63, null=True, )

class Band(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63, blank=True, null=True)


class Album(models.Model):
    title = models.CharField(max_length=63)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True, null=True, )


class Concert(models.Model):
    name = models.CharField(max_length=63)
    audience = models.IntegerField(default=100, )


class Person(models.Model):
    name = models.CharField(max_length=63)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.name} is {self.age}"


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    MARKET_SEGMENT_CHOICES = (
        ("A", "mini car"),
        ("B", "small car"),
        ("C", "medium car"),
        ("D", "large car"),
        ("F", "luxury car"),
        ("S", "sport car"),
    )

    brand = models.CharField(max_length=255)
    horsepower = models.IntegerField()
    creation_date = models.DateField(null=True)
    description = models.TextField(default="Default description")
    market_segment = models.CharField(
        max_length=1,
        choices=MARKET_SEGMENT_CHOICES,
        default="C"
    )

    def __str__(self):
        return f"{self.id}: {self.brand} (power: {self.horsepower})"


class Message(models.Model):
    content = models.TextField()
    datetime_sent = models.DateTimeField(auto_now=True)
