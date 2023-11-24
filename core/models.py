from django.db import models


class SignupModel(models.Model):

    name: str = models.CharField(max_length=254)
    email: str =  models.EmailField(max_length=254)

    def __str__(self) -> str:
        return self.name