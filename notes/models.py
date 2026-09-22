from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    task = models.CharField(max_length=200)
    text_task = models.TextField(blank=True)

    def __str__(self):
        return self.task

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title