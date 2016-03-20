from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    birth_date = models.DateField(null=True)
    description = models.TextField()

    class Meta:
        db_table = 'person'

    def __str__(self):
        return ' '.join([self.name, self.surname])

    def __eq__(self, other):
        return isinstance(other, Person) and other.id == self.id

    def short_name(self):
        return "{0} {1}.".format(self.surname, self.name[0])


class File(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'file'


class Article(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    file = models.ForeignKey(File, on_delete=models.SET_NULL, null=True)
    journal = models.CharField(max_length=255)
    publication_date = models.DateField(null=True
                                        # , input_formats=['%Y', '%d/%m/%Y', '%m/%Y', '%d-%m-%Y', '%m-%Y']
                                        )
    authors = models.ManyToManyField(Person, db_table='author_to_article', related_name='articles')

    class Meta:
        db_table = 'article'


class AuthorToArticle(models.Model):
    author = models.ForeignKey(Person, db_column='author_id')
    article = models.ForeignKey(Article, db_column='article_id')

    class Meta:
        db_table = 'author_to_article'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comment'
        ordering = ('-date',)
