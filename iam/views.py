from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1> ФИО: Пупкин Павел Петрович</h1>'
                        '<h2> Дата рождения: 20.02.1995</h2>'
                        '<h3> Образование: Высшее, педагогическое'
                        '<h4> Опыт работы: 13 лет'
                        '<h5> Личные качества: Умение работать в колективе, многозадачность, готов к обучению </h5>')

