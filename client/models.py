from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.


class Profile(models.Model):
    GENDER_CHOICES = (
        (1, 'Мужчина'),
        (2, 'Женщина'),
        (3, 'Иначе'),
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Номер телефона должен быть в формате '+999999999'")

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                unique=True, primary_key=True, blank=False, related_name='profile')
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    address = models.CharField(max_length=300)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, default=3)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        app_label = 'auth'
