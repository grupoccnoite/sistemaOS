from django.contrib import admin
from itens.models import Itens      

# Register your models here.

class ItensAdmin(admin.ModelAdmin):
        model = Itens      
        list_display = ['descricao', 'valor']
        search_fields = ['descricao']
	list_filter = ['descricao',]

admin.site.register(Itens, ItensAdmin)


