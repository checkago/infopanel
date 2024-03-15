import locale
from datetime import datetime, date
import requests
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
    locale.setlocale(locale.LC_TIME, 'ru_RU')
    url = "https://obs-balashiha.ru/api/v1/cinema-week/"
    movies_data = []

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for week_data in data:
            for cinema_day in week_data["cinemadays"]:
                movies = cinema_day["movies"]
                if movies:  # Проверяем, есть ли фильмы на этот день
                    movies_info = []
                    for movie in movies:
                        movie_info = {
                            "movie_name": movie["name"],
                            "start_time": datetime.strptime(movie["start_time"], '%H:%M:%S').strftime('%H:%M'),  # Форматируем время
                        }
                        movies_info.append(movie_info)

                    day_info = {
                        "day_name": cinema_day["name"],
                        "date": datetime.strptime(cinema_day["date"], '%Y-%m-%d').strftime('%d.%m'),  # Форматируем дату
                        "movies": movies_info
                    }
                    movies_data.append(day_info)

    return movies_data


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


def get_news():
    url = 'https://obs-balashiha.ru/api/v1/news_list/'  # Замените на URL вашего API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        filtered_data = []

        for item in data:
            if (
                item.get('date') <= str(date.today())
            ):
                filtered_data.append(item)

        return filtered_data
    else:
        # Обработка ошибки запроса к API
        return []

