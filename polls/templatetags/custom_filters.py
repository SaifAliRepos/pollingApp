from django import template
from django.utils import timezone
import datetime

register = template.Library()


@register.filter
def time_difference(pub_date):
    now = timezone.now()
    duration = datetime.timedelta(days=14)
    time_diff = pub_date - (now - duration)

    days = time_diff.days
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    time_diff_formatted = f"{days} days, {hours}:{minutes:02} mins"
    return time_diff_formatted
