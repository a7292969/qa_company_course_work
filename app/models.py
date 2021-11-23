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
