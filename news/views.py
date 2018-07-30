from django.utils import timezone
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from .models import News

#def index(request):
#    news = News.objects.filter(posted_date__lte=timezone.now()).order_by('posted_date')
#    return render(request, 'news/index.html', {'news': news})


def index(request):
    posts= News.objects.all()
    paginator = Paginator(posts, 1)
    page = request.GET.get('page')

    posts = paginator.get_page(page)
    return render(request, 'news/list.html', {'posts': posts})