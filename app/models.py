from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import safe


class TimeStamped(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)


class BaseAddress(models.Model):
    class Meta:
        abstract = True

    cep = models.CharField(max_length=15, default="Nao Informado")
    state = models.CharField(max_length=20, default="Nao Informado")
    city = models.CharField(max_length=100, default="Nao Informado")
    district = models.CharField(max_length=100, default="Nao Informado")
    address = models.CharField(max_length=100, default="Nao Informado")
    number = models.CharField(max_length=5, default="Nao Informado")
    complement = models.CharField(max_length=200, blank=True)


class Institute(TimeStamped, BaseAddress):
    class Meta:
        verbose_name = "Instituicao"
        verbose_name_plural = "Instituicoes"

    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    photo = models.URLField(blank=True)
    cnpj = models.CharField(max_length=100, default="Nao Informado")
    description = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=30, default="Nao Informado")

    def __str__(self):
        return self.user.first_name

    def __unicode__(self):
        return u'%s' % (self.user.first_name)


class CommonUser(TimeStamped):
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=100, default="Nao Informado")
    phone = models.CharField(max_length=30, default="Nao Informado")
    anonymous = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % (self.user.first_name)

    def __str__(self):
        return self.user.first_name


class Item(TimeStamped):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    name_item = models.CharField(max_length=100)
    photo = models.URLField()

    def __unicode__(self):
        return u'%s' % (self.name_item)

    def __str__(self):
        return self.name_item


object_type = (
    ('Eletronicos', 'Eletronicos'),
    ('Vestimentas', 'Vestimentas'),
    ('Alimentos', 'Alimentos'),
    ('Higiene', 'Higiene'),
    ('Mobilia', 'Mobilia'),
    ('Brinquedos', 'Brinquedos'),
    ('Papelaria', 'Papelaria'),
    ('Outros', 'Outros'),
)


class Object(TimeStamped):
    class Meta:
        verbose_name = "Objeto"
        verbose_name_plural = "Objetos"

    item = models.ForeignKey(Item, on_delete=models.CASCADE, unique=True)
    type = models.CharField(max_length=50, choices=object_type)

    def __unicode__(self):
        return u'%s' % (self.item.name_item)

    def __str__(self):
        return self.item.name_item


class Service(TimeStamped):
    class Meta:
        verbose_name = "Servico"
        verbose_name_plural = "Servicos"

    item = models.ForeignKey(Item, on_delete=models.CASCADE, unique=True)

    def __unicode__(self):
        return u'%s' % (self.item.name_item)

    def __str__(self):
        return self.item.name_item


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

    @permalink
    def get_absolute_url(self):
        return ('view_post', None, {'slug': self.slug})


class ImagePost(TimeStamped):
    class Meta:
        verbose_name = "ImagePost"
        verbose_name_plural = "ImagePosts"

    image = CloudinaryField('image')
    model = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    label = models.CharField(max_length=100, blank=True, null=True)
    is_visible = models.BooleanField(default=True)


class Message(models.Model):
    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"

    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.email)
