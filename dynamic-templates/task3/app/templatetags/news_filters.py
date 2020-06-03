from django import template
import datetime


register = template.Library()

@register.filter
def format_date(value):
    # Ваш код
    cur_time = datetime.datetime.now()
    reddit_time = datetime.datetime.fromtimestamp(value)

    if (cur_time - reddit_time) <= datetime.timedelta(minutes=10):
        return 'только что'

    if (cur_time - reddit_time) <= datetime.timedelta(hours=24):
        hours = (cur_time - reddit_time).seconds // 3600
        return f'{hours} часов назад'

    return reddit_time.strftime('%Y-%m-%d')


# необходимо добавить фильтр для поля `score`
@register.filter
def format_score(value):
    if (value < -5):
        return 'все плохо'
    elif (value <= 5):
        return 'нейтрально'
    else:
        return 'хорошо'


@register.filter
def format_num_comments(value):
    # Ваш код
    if (value == 0):
        return 'Оставьте комментарий'
    elif (value <= 50):
        return f'{value} комментариев'
    else:
        return '50+'


@register.filter
def format_selftext(value, count=5):
    reddit_list = value.split()
    length = len(reddit_list)

    return ' '.join(reddit_list[:count]) + ' ... ' + ' '.join(reddit_list[length-count:])
