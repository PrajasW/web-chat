from django.shortcuts import render, redirect
from .models import Message
from django.shortcuts import HttpResponse
from datetime import date, datetime


# Create your views here.
def home(request):
    queryset = Message.objects.all()
    params = {
        "messages":queryset,
    }
    return render(request,'chats.html',params)

def addMessage(request):
    sender = request.POST.get('sender','not found')
    reciver = request.POST.get('reciver','not found')
    message = request.POST.get('message','not found')
    if sender == 'not found' or reciver == 'not found' or message == 'not found':
        return render(request,'home.html')
    now = datetime.now()
    datee = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M")
    print(sender+" "+reciver+ " "+message+" "+datee + " "+time)
    msg = Message(sender = sender,reciver = reciver,message = message,date = datee,time = time)
    msg.save()
    return redirect('/')