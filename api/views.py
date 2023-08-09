from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import requests

from .serializer import MessageSerializer
from whatsapp.models import *

class Bot():
    def __init__(self, data):
        self.data = data
        self.get_client()
        self.get_message()
        self.get_client_chat_flow()
        self.get_answer()
        
        
        
    def get_client(self):
        client_phone = self.data['entry'][0]['changes'][0]['value']['messages'][0]['from']
        if Client.objects.filter(phone=client_phone).count()==0:
            #Create it
            self.client = Client.objects.create(phone = client_phone)
            self.client.save()
        else:
            self.client = Client.objects.get(phone=client_phone)
        
        
    def get_message(self):
        # Check if ui know the message
        id_wap = self.data['entry'][0]['changes'][0]['value']['messages'][0]['id']
        if Message.objects.filter(id_wap = id_wap).count()==0:
            type = self.data['entry'][0]['changes'][0]['value']['messages'][0]['type']
            # check if the msg its an audio
            if type != 'text':
                message = 'Audio'
            else:
                message = self.data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            
            timestamp = self.data['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']
            
            self.wap = Message.objects.create(id_wap=id_wap, client=self.client, type=type, timestamp=timestamp,msg_recibed=message)
            self.wap.save()
    
    def get_client_chat_flow(self):
        if ClientChatStatus.objects.filter(client = self.client).count() == 0:
            self.chat_status = ClientChatStatus.objects.create(client = self.client, status = 0)
            self.chat_status.save()
        else:
            self.chat_status=ClientChatStatus.objects.get(client=self.client)
    
    def get_answer(self):
        flow = ChatFlow.objects.get(status=self.chat_status.status)
        if flow.params == "":
            self.answer = flow.ok_message
        else:
            if flow.params:
                self.answer = flow.ok_message
            else:
                self.answer = flow.nook_message
    
        print(self.answer)
            
    def send_message(self):
        pass 
    
    

@api_view(['GET','POST'])
def webhook(request):
    if request.method == "GET":
        if request.args.get('hub.verify_token') == "nordelban_wap_bot":
            #ESCRIBIMOS EN EL NAVEGADOR EL VALOR DEL RETO RECIBIDO DESDE FACEBOOK
            return request.args.get('hub.challenge')
        else:
            #SI NO SON IGUALES RETORNAMOS UN MENSAJE DE ERROR
          return "Error de autentificacion."
    data = request.data
    print(data)
    Bot(data)
    
    return JsonResponse(data)