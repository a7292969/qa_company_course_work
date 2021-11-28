from django.db import models


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=500)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.comment + " - " + self.user

    def natural_key(self):
        return {
            'comment': self.comment,
            'user': self.user,
        }


class Vacancy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=500)
    salary = models.IntegerField()

    def __str__(self):
        return self.name + " - " + str(self.salary)

    def natural_key(self):
        return {
            'name': self.name,
            'summary': self.summary,
            'salary': self.salary,
        }
