from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    html = '''
    <div>
        <h1>Резюме(Главная)</h1>
        <h2> Пупкин Павел Петрович</h2>
        <p>Описание(о себе):</p>
        <ul>
            <li>Дата рождения: 20.03.1998</li>
            <li>Образование: Высшее </li>
            <li>Профессия: Профессиональное обучения</li>
            <li>Опыт работы: 12 лет </li>
        </ul>
        <br>
        <footer>
            <div>
                <p>Контакты: +375454644845</p>
            </div>
        </footer>
        
    </div>
    '''

    return HttpResponse(html)
    # return HttpResponse('<h1> ФИО: Пупкин Павел Петрович</h1>'
    #                         '<h2> Дата рождения: 20.02.1995</h2>'
    #                         '<h3> Образование: Высшее, педагогическое'
    #                         '<h4> Опыт работы: 13 лет'
    #                         '<h5> Личные качества: Умение работать в колективе, многозадачность, готов к обучению </h5>')

