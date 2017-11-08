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


class Instituicao(TimeStamped):
    class Meta:
        verbose_name = "Instituicao"
        verbose_name_plural = "Instituicoes"

    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    photo = models.URLField(blank=True)
    cnpj = models.CharField(max_length=100, default="Nao Informado")
    senha = models.CharField(max_length=20, default="12345678")
    name = models.CharField(max_length=100, default="Nao Informado")
    cep = models.CharField(max_length=8, default="Nao Informado")
    estado = models.CharField(max_length=20, default="Nao Informado")
    cidade = models.CharField(max_length=100, default="Nao Informado")
    bairro = models.CharField(max_length=100, default="Nao Informado")
    rua = models.CharField(max_length=100, default="Nao Informado")
    numero = models.CharField(max_length=5, default="Nao Informado")
    complemento = models.CharField(max_length=200, default="Nao Informado")
    descricao = models.CharField(max_length=100, default="Nao Informado")
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=30, default="Nao Informado")

    def __str__(self):
        return self.user.first_name

    def __unicode__(self):
        return u'%s' % (self.user.first_name)


class Usuario(TimeStamped):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    photo = CloudinaryField()
    nome = models.CharField(max_length=150, default="Nao Informado")
    dataNascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=100, default="Nao Informado")
    email = models.EmailField(blank=True)
    endereco = models.CharField(max_length=100, default="Nao Informado")
    numero = models.CharField(max_length=10, default="Nao Informado")
    bairro = models.CharField(max_length=100, default="Nao Informado")
    cep = models.CharField(max_length=8, default="Nao informado")
    complemento = models.CharField(max_length=100, default="Nao Informado")
    cidade = models.CharField(max_length=100, default="Nao Informado")
    estado = models.CharField(max_length=20, default="Nao Informado")
    telefone = models.CharField(max_length=30, default="Nao Informado")
    login = models.CharField(max_length=15 , default="Nao Informado")
    senha = models.CharField(max_length=25, default="Nao Informado")

    def __unicode__(self):
        return u'%s' % (self.user.first_name)

    def __str__(self):
        return self.user.first_name


class Item(TimeStamped):
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=300)
    nome_item = models.CharField(max_length=100)
    photo = models.URLField()

    def __unicode__(self):
        return u'%s' % (self.nome_item)

    def __str__(self):
        return self.nome_item


tipo_objeto = (
    ('Eletronicos', 'Eletronicos'),
    ('Calcados', 'Calcados'),
    ('Pereciveis', 'Pereciveis'),
)


class Objeto(TimeStamped):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, unique=True)
    tipo = models.CharField(max_length=50, choices=tipo_objeto)

    def __unicode__(self):
        return u'%s' % (self.item.nome_item)

    def __str__(self):
        return self.item.nome_item


class Servico(TimeStamped):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, unique=True)

    def __unicode__(self):
        return u'%s' % (self.item.nome_item)

    def __str__(self):
        return self.item.nome_item


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


class Mensagem(models.Model):
    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"

    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.email)
