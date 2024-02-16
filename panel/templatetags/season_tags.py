from django import template
from datetime import datetime
from panel.models import BackGround

register = template.Library()


@register.simple_tag
def seasonal_background_color():
    now = datetime.now()
    season = get_current_season(now.month)  # Передаем месяц в функцию get_current_season()

    try:
        background = BackGround.objects.get(**{season: True})
        if background.image:
            return f"url('{background.image.url}') center/cover repeat;"
        elif background.standart:
            return "#fb3;"  # Стандартный цвет фона
    except BackGround.DoesNotExist:
        pass

    return ''  # В случае отсутствия фона или ошибки, возвращаем пустую строку


def get_current_season(month):
    if month in range(6, 9):
        return 'summer'
    elif month in range(9, 12):
        return 'standart'
    elif month in range(3, 6):
        return 'standart'
    else:
        return 'winter'

