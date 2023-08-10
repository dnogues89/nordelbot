from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=70, blank=True, null=True)
    email = models.EmailField(blank=True,null=True)
    phone = models.IntegerField(blank=True, null=True)
    contacts = models.IntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f'Nombre: {self.name} | Telefono: {self.phone}'
    
    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
        
class CarModel(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    active = models.BooleanField(auto_created=True)

    def __str__(self) -> str:
        return f'Modelo: {self.name}'   

    class Meta:
        verbose_name = 'model'
        verbose_name_plural = 'models'
        
          
class ClientChatStatus(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now=True)
    coment = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        if self.model != None:
            return f'{self.client} | Modelo: {self.model}'
        else:
            return f'{self.client}'

    class Meta:
        verbose_name = 'estatus'
        verbose_name_plural = 'estatus'
    


class Message(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    msg_recibed = models.TextField(max_length=1000)
    msg_sended = models.TextField(max_length=1000, blank=True, null=True)
    id_wap = models.CharField(max_length=50, primary_key=True)
    timestamp = models.IntegerField()
    fecha = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=15)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'

    
    
class ChatFlow(models.Model):
    flow_name = models.CharField(max_length=50)
    status = models.IntegerField(null=True)
    option = models.IntegerField(null=True)
    params = models.TextField(max_length=1000, null=True, blank=True)
    ok_message = models.TextField(max_length=1000,blank=True, null=True)
    nook_message = models.TextField(max_length=1000,blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.flow_name}'

    class Meta:
        verbose_name = 'flow'
        verbose_name_plural = 'flow'
        
class Credentials(models.Model):
    token_wa = models.CharField(max_length=500)
    whatsapp_url = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Credenciales'
        verbose_name_plural = 'Credenciales'