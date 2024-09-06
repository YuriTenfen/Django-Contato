from django.contrib import admin

from .models import Grupo, Contato
# Register your models here.

admin.site.site_header = "Django Contatos"
admin.site.site_title = "Django Contatos"
admin.site.index_title = "Seja Bem-Vindo a nossa página"

admin.site.register(Grupo)
admin.site.register(Contato)

