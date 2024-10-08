import json
from datetime import datetime

import requests
from django.shortcuts import render, get_object_or_404
from panel.api import get_events, get_movies, get_visible_header, get_news
from panel.models import Section, Pravila, PushkinCard, Reglament, Qr


def index(request):
    events_data = get_events()
    movies_data = get_movies()
    header = get_visible_header()
    return render(request, 'index.html', {'events_data': events_data, 'movies_data': movies_data,
                                          'header': header})


def news_list(request):
    news_data = get_news()
    return render(request, 'news.html', {'news_data': news_data})


def news_detail(request, news_id):
    news_list = get_news()
    news_item = None

    for news in news_list:
        if news.get('id') == news_id:
            news_item = news
            break

    return render(request, 'news_detail.html', {'news_item': news_item})



def events_list(request):
    events_data = get_events()
    return render(request, 'events.html', {'events_data': events_data})


def krujki_list(request):
    krujki_data = Section.objects.all()
    return render(request, 'krujki.html', {'krujki_data': krujki_data})


def krujok_detail(request, pk):
    krujok = get_object_or_404(Section, pk=pk)
    return render(request, 'krujok_detail.html', {'krujok': krujok})


def pravila(request):
    pravila = Pravila.objects.all()
    return render(request, 'pravila.html', {'pravila': pravila})


def pushkin(request):
    pushkin = PushkinCard.objects.all()
    return render(request, 'pushkin.html', {'pushkin': pushkin})


def reglament_list(request):
    reglament_list = Reglament.objects.all()
    return render(request, 'reglament_list.html', {'reglament_list': reglament_list})


def reglament_detail(request, pk):
    reglament = get_object_or_404(Reglament, pk=pk)
    return render(request, 'reglament.html', {'reglament': reglament})


def qr(request):
    qr_list = Qr.objects.all()
    return render(request, 'qr_list.html', {'qr_list': qr_list})


def services_list(request):
    api_url = 'http://obs-balashiha.ru/api/v1/services_list/'
    response = requests.get(api_url)
    services = response.json()

    return render(request, 'services_list.html', {'services': services})


def shedule_list(request):
    url = "http://obs-balashiha.ru/api/v1/active-weeks/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        week_data = data[0]  # Предполагаем, что у вас есть только одна неделя в данных

        days = week_data["data"][0]["days"]  # Получаем список дней

        for day in days:
            for event in day["events"]:
                event["start_time"] = datetime.strptime(event["start_time"], "%H:%M:%S").strftime("%H:%M")
                event["end_time"] = datetime.strptime(event["end_time"], "%H:%M:%S").strftime("%H:%M")

        context = {
            "days": days
        }

        return render(request, 'shedule_list.html', context)
    else:
        # Обработка случая, если не удалось получить данные
        return render(request, 'error_template.html')


def balashiha(request):
    return render(request, 'balashiha_site.html')