from django.shortcuts import render
from django.utils import timezone
from .models import News

def index(request):
    news = News.objects.filter(posted_date__lte=timezone.now()).order_by('posted_date')
    return render(request, 'news/index.html', {'news': news})



