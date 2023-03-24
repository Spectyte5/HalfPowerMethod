from django.db import models

class Input(models.Model):
    transfer = models.CharField(max_length=100)
    function = models.CharField(max_length=100)
    time = models.IntegerField()

    def __str__(self):
        return f"Transfer:{self.transfer}, Function:{self.function}, Time:{self.time}"