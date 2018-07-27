from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from .models import News

#def index(request):
#    news = News.objects.filter(posted_date__lte=timezone.now()).order_by('posted_date')
#    return render(request, 'news/index.html', {'news': news})


def index(request):
    contact_list = News.objects.all()
    paginator = Paginator(contact_list, 1)  # Show 25 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'news/list.html', {'contacts': contacts})