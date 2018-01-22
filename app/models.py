# coding=utf-8
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
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

    cep = models.CharField(max_length=15, blank=True)
    state = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    number = models.CharField(max_length=5, blank=True, null=True)
    complement = models.CharField(max_length=200, blank=True)


class Institute(TimeStamped, BaseAddress):
    class Meta:
        verbose_name = "Instituicao"
        verbose_name_plural = "Instituicoes"

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    photo = models.URLField(blank=True)
    cnpj = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    site = models.CharField(max_length=100)
    social = models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name

    def __unicode__(self):
        return u'%s' % self.user.first_name


class CommonUser(TimeStamped, BaseAddress):
    class Meta:
        verbose_name = "Doador"
        verbose_name_plural = "Doadores"

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    anonymous = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.user.first_name

    def __str__(self):
        return self.user.first_name


class Auditor(TimeStamped, BaseAddress):
    class Meta:
        verbose_name = "Auditor"
        verbose_name_plural = "Auditores"

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    phone = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return u'%s' % self.user.first_name

    def __str__(self):
        return self.user.first_name


class Item(TimeStamped):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    name_item = models.CharField(max_length=100)
    photo = models.URLField()
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' % self.name_item

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
        return u'%s' % self.item.name_item

    def __str__(self):
        return self.item.name_item


class Service(TimeStamped):
    class Meta:
        verbose_name = "Servico"
        verbose_name_plural = "Servicos"

    item = models.ForeignKey(Item, on_delete=models.CASCADE, unique=True)

    def __unicode__(self):
        return u'%s' % self.item.name_item

    def __str__(self):
        return self.item.name_item


class Post(TimeStamped):
    title = models.CharField(max_length=150)
    text = RichTextField()
    is_visible = models.BooleanField(default=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return u'%s' % self.title

    def get_description(self):
        return safe(self.text[:200])

    @permalink
    def get_absolute_url(self):
        return ('view_post', None, {'slug': self.slug})


class ImagePost(TimeStamped):
    class Meta:
        verbose_name = "ImagePost"
        verbose_name_plural = "ImagePosts"

    image = models.URLField()
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


class Requirement(TimeStamped):
    class Meta:
        verbose_name = "Necessidade"
        verbose_name_plural = "Necessidades"

    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=50, choices=object_type)
    status = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=300)

    # photo = models.URLField()

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return u'%s' % self.name


class Match(TimeStamped):
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s : %s - %s' % (self.requirement.name,
                                  self.requirement.type,
                                  self.requirement.owner)

    def __str__(self):
        return u'%s : %s - %s' % (self.requirement.name,
                                  self.requirement.type,
                                  self.requirement.owner)


accepted_type = (
    ('ACEITO', 'ACEITO'),
    ('EM ANÁLISE', 'EM ANÁLISE'),
    ('RECUSADO', 'RECUSADO')
)


class Notification(TimeStamped):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    status = models.CharField(choices=accepted_type, max_length=100, default='EM ANÁLISE')
    is_accepted = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s - Match: %s' % (self.user.first_name, self.match)

    def __str__(self):
        return u'%s - Match: %s' % (self.user.first_name, self.match)


deferred_type = (
    ('DEFERIDO', 'DEFERIDO'),
    ('EM ANÁLISE', 'EM ANÁLISE'),
    ('INDEFERIDO', 'INDEFERIDO')
)


class Audit(TimeStamped):
    new_owner = models.ForeignKey(User, related_name='new_owner', on_delete=models.CASCADE, )
    donor = models.ForeignKey(User, related_name='donor', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    is_deferred = models.CharField(choices=deferred_type, max_length=100, default='EM ANÁLISE')
    match = models.OneToOneField(Match, on_delete=models.CASCADE, blank=True, null=True)

    def __unicode__(self):
        return u'%s - %s' % (self.new_owner.first_name, self.item)

    def __str__(self):
        return u'%s - %s' % (self.new_owner.first_name, self.item)


class Step(TimeStamped):
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE)
    note = models.TextField()

    def __unicode__(self):
        return u'Step to Audit: %s' % (self.audit)

    def __str__(self):
        return u'Step to Audit: %s' % (self.audit)


class ItemCollect(TimeStamped):
    audit = models.OneToOneField(Audit, on_delete=models.CASCADE)

class Donation(TimeStamped):
    donator = models.ForeignKey(User, related_name='donator', on_delete=models.CASCADE)
    institute = models.ForeignKey(User, related_name='reciver', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    data = models.DateField()
    is_completed = models.BooleanField(default=False)