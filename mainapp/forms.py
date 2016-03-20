from django import forms
from django.forms.forms import BaseForm
from models import Article, Person


class AuthorsChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.short_name


class ArticleForm(forms.Form):
    def __init__(self, data=None, name=None, description=None, publication_date=None):
        super(ArticleForm, self).__init__(data)
        self.name = forms.CharField(max_length=255, initial=name)
        self.description = forms.Textarea()
        self.authors = AuthorsChoiceField(queryset=Person.objects.all(), required=False)
        self.publication_date = forms.DateField(initial=publication_date)
