from django.shortcuts import render, redirect
from django.http import HttpResponse

from stories.froms import ContactForm
from stories.models import Story, Subcribe, Contact, Category
from django.core.mail import EmailMessage
from django.db.models import Q
import re


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def Masterbase(request, id):
    list_category = Category.objects.all()
    return render(request, 'stories/Masterbase.html', context={
        'list_category': list_category,
    })

def index(request):
    list_story = Story.objects.all()[:4]
    list_story_dex_1 = Story.objects.filter(id=11)[:1]
    nha_dat_ban = Story.objects.filter(category_id=1)
    nha_dat_thue = Story.objects.filter(category_id=2)
    tin_tuc = Story.objects.filter(category_id=3)

    return render(request, 'stories/index.html', context={
        'list_story': list_story,
        'nha_dat_ban': nha_dat_ban,
        'nha_dat_thue': nha_dat_thue,
        'tin_tuc': tin_tuc,
        'list_story_dex_1': list_story_dex_1,
    })

def blogs(request):
    list_story = Story.objects.filter(category_id=1)
    paginator = Paginator(list_story, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'stories/blog.html', context={
        'List_story': list_story,
        'page_obj': page_obj,
    })

def contact(request):
    forms = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form['subject'].value()
            message = form['message'].value()
            notifier = f'Name:\t{form["name"].value()}\nmessage:\t{form["message"].value()}\nemail:\t{form["email"].value()}'
            form.save()
            email = EmailMessage(subject, notifier, to=['huynhdonggiang@gmail.com'])
            email.send()
            return redirect('stories:contact_ok')
        else:
            form = ContactForm()
    return render(request, 'stories/contact_us.html', {'form': forms})

def contact_ok(request):
    
    return render(request, 'stories/contact_ok.html')

def news(request):
    return render(request, 'stories/news.html')

def single(request):
    list_story = Story.objects.filter(category_id=2)
    paginator = Paginator(list_story, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'stories/single.html', context={
        'List_story': list_story,
        'page_obj': page_obj,
    })

def news(request):
    list_story = Story.objects.filter(category_id=3)
    paginator = Paginator(list_story, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'stories/news.html', context={
        'List_story': list_story,
        'page_obj': page_obj,
    })
def detail_single(request, id):
    list_story = Story.objects.filter(id=id)
    return render(request, 'stories/detail_single.html', {
        'List_story': list_story,
    })

def search(request):
    stories_search = []
    tu_khoa = ' '

    if request.GET.get('keyword'):

        tu_khoa = request.GET.get('keyword')
        # stories_search = Story.objects.filter(Q(name=tu_khoa)|Q(content__contains=tu_khoa)).order_by('-public_day')
        stories = Story.objects.all().values()
        lst_story = list(stories)
        id_list = []
        for story in lst_story:
            story['content'] = re.sub('<[^<]+?>','',story['content'])
            if tu_khoa.lower() in story['name'].lower() or tu_khoa.lower() in story['content'].lower():
                id_list.append(story['id'])
        stories_search = Story.objects.filter(id__in=id_list).order_by('-public_day')

    return render(request, 'stories/search.html', {
        'stories_search': stories_search,
        'keyword': tu_khoa,
    })
