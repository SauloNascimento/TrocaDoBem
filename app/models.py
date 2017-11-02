from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import safe


class TimeStamped(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)


class Instituicao(TimeStamped):
    class Meta:
        verbose_name = "Instituicao"
        verbose_name_plural = "Instituicoes"

    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    photo = models.URLField()
    cnpj = models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name

    def __unicode__(self):
        return u'%s' % (self.user.first_name)


class Usuario(TimeStamped):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    photo = CloudinaryField()

    def __unicode__(self):
        return u'%s' % (self.user.first_name)

    def __str__(self):
        return self.user.first_name


tipo_objeto = (
    ('Eletronicos', 'Eletronicos'),
    ('Calcados', 'Calcados'),
    ('Pereciveis', 'Pereciveis'),
)


class Objeto(TimeStamped):
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=tipo_objeto)
    nome_objeto = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.nome_objeto)

    def __str__(self):
        return self.nome_objeto


class Servico(TimeStamped):
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_atividade = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.nome_atividade)

    def __str__(self):
        return self.nome_atividade


class Post(TimeStamped):
    title = models.CharField(max_length=150)
    text = RichTextField()
    is_visible = models.BooleanField(default=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return u'%s' % (self.title)

    def get_description(self):
        return safe(self.text[:200])

        # @permalink
        # def get_absolute_url(self):
        #     return ('view_post', None, {'slug': self.slug})


class ImagePost(TimeStamped):
    class Meta:
        verbose_name = "ImagePost"
        verbose_name_plural = "ImagePosts"

    image = CloudinaryField('image')
    model = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    label = models.CharField(max_length=100, blank=True, null=True)
    is_visible = models.BooleanField(default=True)


class Message(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.email)
