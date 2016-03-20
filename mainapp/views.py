from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Person, Article, File
from django.core.urlresolvers import reverse
from datetime import datetime
import time
from django.conf import settings


def index(request):
    return render(request, 'mainapp/index.html')


def get_person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(request, 'mainapp/person.html', {'person': person})


def get_persons(request):
    return render(request, 'mainapp/persons.html', {'persons': Person.objects.all()})


def get_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'mainapp/article.html', {'article': article})


def get_articles(request):
    return render(request, 'mainapp/articles.html', {'articles': Article.objects.all()})


def edit_person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(request, 'mainapp/edit_person.html', {'person': person})


def create_article(request):
    article = Article()
    return create_edit_article(request, article, 'Create article', 'Create', reverse('mainapp:create_article'))


def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return create_edit_article(request, article, 'Edit article', 'Update',
                               reverse('mainapp:edit_article', args=(article.id,)))


def create_edit_article(request, article, title, action, action_url):
    if request.method == 'GET':
        context = {
            'article': article,
            'title': title,
            'action': action,
            'action_url': action_url,
            'all_authors': Person.objects.all(),
        }
        return render(request, 'mainapp/edit_article.html', context)
    else:
        article.name = request.POST['name']
        article.description = request.POST['description']
        article.publication_date = datetime.strptime(request.POST['publication_date'], '%d/%m/%Y')
        if not article.id:
            article.save()
        article.authors = Person.objects.filter(id__in=[int(a) for a in request.POST.getlist('authors')])
        article.save()

        return HttpResponseRedirect(reverse('mainapp:get_article', args=(article.id,)))


def create_article_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    text = request.POST['text']
    article.comment_set.create(text=text)
    return HttpResponseRedirect(reverse('mainapp:get_article', args=(article.id,)))


def create_person_comment(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    text = request.POST['text']
    person.comment_set.create(text=text)
    return HttpResponseRedirect(reverse('mainapp:get_person', args=(person_id,)))


def create_person(request):
    person = Person()
    if request.method == 'GET':
        context = {
            'person': person,
            'title': 'Add person',
            'action': 'Create',
            'action_url': reverse('mainapp:create_person'),
        }
        return render(request, 'mainapp/edit_person.html', context)
    else:
        person.name = request.POST['name']
        person.surname = request.POST['surname']
        person.description = request.POST['description']
        if request.POST['birth_date']:
            person.birth_date = datetime.strptime(request.POST['birth_date'], '%d/%m/%Y')
        person.save()
        return HttpResponseRedirect(reverse('mainapp:create_person'))


def get_tasks(request):
    return HttpResponse('Tasks list stub')


def upload_article_file(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    file_data = request.FILES['file']
    extension = '.' + file_data.name.split('.')[-1]
    filepath = settings.FILE_REPO + str(int(time.mktime(datetime.now().timetuple()))) + extension
    name = file_data.name
    with open(filepath, 'wb+') as destination:
        for chunk in file_data.chunks():
            destination.write(chunk)
        file = File(name=name, path=filepath)
        file.save()
        file.article_set.add(article)

    return HttpResponseRedirect(reverse('mainapp:get_article', args=(article_id,)))
