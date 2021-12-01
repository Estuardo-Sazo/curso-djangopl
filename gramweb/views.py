from django.http import HttpResponse
from datetime import datetime

def hello(request):
    now = datetime.now().strftime('%b %d, %Y - %H:%M hrs')
    return HttpResponse('La fecha del servidor {now}' .format(now=now))



