from django.shortcuts import render
import requests
from datetime import date, datetime
from panel.models import Header


def get_events():
    url = 'https://obs-balashiha.ru/api/v1/event_list/'  # Замените на URL вашего API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        filtered_data = []

        for item in data:
            if (
                item.get('library') == 'Информационно-культурный центр' and
                item.get('date') >= str(date.today())
            ):
                filtered_data.append(item)

        return filtered_data
    else:
        # Обработка ошибки запроса к API
        return []


def get_movies():
    url = 'https://obs-balashiha.ru/api/v1/cinema-week/'  # Замените на URL вашего API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        filtered_data = []

        for item in data:
            if (
                item.get('date') >= str(date.today())
            ):
                filtered_data.append(item)

        return filtered_data
    else:
        # Обработка ошибки запроса к API
        return []


def get_current_season():
    now = datetime.now()
    if now.month in range(6, 9):
        return 'summer'
    elif now.month in range(9, 12):
        return 'autumn'
    elif now.month in range(3, 6):
        return 'spring'
    else:
        return 'winter'

def get_visible_header():
    current_season = get_current_season()
    if current_season == 'summer':
        return Header.objects.filter(summer=True).first()
    elif current_season == 'winter':
        return Header.objects.filter(winter=True).first()
    else:
        return Header.objects.filter(standart=True).first()


def index(request):
    events_data = get_events()
    movies_data = get_movies()
    header = get_visible_header()
    return render(request, 'index.html', {'events_data': events_data, 'movies_data': movies_data,
                                          'header': header})

# API SECTION

def get_news():
    url = 'https://obs-balashiha.ru/api/v1/news_list/'  # Замените на URL вашего API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        filtered_data = []

        for item in data:
            if (
                item.get('library') == 'Детская библиотека (ш. Энтузиастов 33)' and
                item.get('date') >= str(date.today())
            ):
                filtered_data.append(item)

        return filtered_data
    else:
        # Обработка ошибки запроса к API
        return []

