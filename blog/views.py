from django.shortcuts import render
from blog.models import GeneralPageInformation, Vacancy 


def home(request):
    company_information = GeneralPageInformation.objects.all()
    context = {'company_information': company_information}
    return render(request, 'blog/home_page.html', context)


def all_vacancy(request):
    vacancy = Vacancy.objects.all()
    context = {'vacancy': vacancy}
    return render(request, 'blog/all_vacancy.html', context)


def description_one_vacancy(request, vacancy_id):
    one_vacancy = Vacancy.objects.get(pk=vacancy_id)
    context = {'one_vacancy': one_vacancy}
    return render(request, 'blog/about_one_vacancy.html', context)