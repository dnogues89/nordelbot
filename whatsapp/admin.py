from django.contrib import admin
from .models import *

# Model Classes
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'contacts')
    search_fields = ('name', 'phone', 'email')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('client', 'date', 'msg_recibed')
    search_fields = ('client',)
    date_hierarchy = 'date'



# Register your models here.

admin.site.register(Client, ClientAdmin)
admin.site.register(CarModel)
admin.site.register(ClientChatStatus)
admin.site.register(Message, MessageAdmin)
admin.site.register(ChatFlow)
admin.site.register(Credentials)