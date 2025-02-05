from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


SCHOOLS = [
    ('ENSPD','Ecole Nationale Supéreure Polytecnique Douala'),
    ('ENSPM','Ecole Nationale Supéreure Polytecnique Maroua'),
    ('ENSPY','Ecole Nationale Supéreure Polytecnique Yaoundé'),
    ('ENSPB','Ecole Nationale Supéreure Polytecnique Bamenda'),
]

class MyUser(AbstractUser):
    school = models.CharField(max_length=50, choices=SCHOOLS, default='ENSPM', blank=False)
    department = models.CharField( max_length=100, validators=[RegexValidator(r'^[A-Za-zÀ-ÿ\s-]+$')])
    email_verification_token = models.CharField(max_length=255, default='')
    is_verified = models.BooleanField(default=False)  # Par défaut, l'utilisateur n'est pas vérifié
