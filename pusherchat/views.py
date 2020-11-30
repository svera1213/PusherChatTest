#render library for returning views to the browser
from django.shortcuts import render
#decorator to make a function only accessible to registered users
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#import the user library
#replace the xxx with your app_id, key and secret respectively
#instantate the pusher class
# Create your views here.
#login required to access this page. will redirect to admin login page.
@login_required(login_url='/admin/login/')
def chat(request):
    return render(request, "pusherchat/chat.html")

@login_required(login_url='/admin/login/')
def chat_applozic(request):
    return render(request, "pusherchat/chat_applozic.html")

@csrf_exempt
def broadcast(request):

    return HttpResponse("done")
