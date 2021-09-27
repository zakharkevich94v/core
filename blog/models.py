from django.db import models


class GeneralPageInformation(models.Model):
    company_name = models.CharField('Название компании', max_length=20)
    company_icon = models.ImageField('Логотип компании', blank=True, upload_to='images/company/logo/')
    company_description = models.TextField('Описание компании', blank=True)
    company_address_ofice = models.CharField('Адрес компании', max_length=225)
    company_phone_number_1 = models.CharField('Контактный телефон 1', max_length=20)
    company_phone_number_2 = models.CharField('Контактный телефон 2', max_length=20)

    def __str__(self):
        return self.company_name


class Vacancy(models.Model):
    job_title = models.CharField('Название Вкансии', max_length=255)
    location_where_work = models.CharField('Город/Страна где работать', max_length=30, null=True)
    job_description = models.TextField('Описание вакансии', blank=True)
    candidate_requirement = models.TextField('Какой кандидат нам подходит', blank=True)
    date_pub = models.DateTimeField('Дата публикации вакансии',  auto_now_add=True)
    other_information_vacancy = models.TextField('Соц пакет', blank=True) 

    def __str__(self):
        return self.job_title
