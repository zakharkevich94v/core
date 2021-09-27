from django.db import models


class Profile(models.Model):
    profile_pic = models.ImageField('Ваша фотография', blank=True, upload_to='images/profile/')
    first_name = models.CharField('Имя', max_length=25)
    last_name = models.CharField('Фамилия', max_length=25)
    middle_name = models.CharField('Отчество', max_length=25)
    email_address = models.EmailField('Адрес электронной почты', blank=True)
    date_of_birth = models.DateField('Дата рождения', max_length=10)
    country = models.CharField('Страна проживания', max_length=25)
    city = models.CharField('Город проживания', max_length=25)

    def __str__(self):
        return self.first_name