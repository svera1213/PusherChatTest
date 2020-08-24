#render library for returning views to the browser
from django.shortcuts import render
#decorator to make a function only accessible to registered users
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#import the user library
from pusher import Pusher
#replace the xxx with your app_id, key and secret respectively
#instantate the pusher class
pusher = Pusher(app_id=u'', key=u'', 
    secret=u'',
    cluster='us2',
    ssl=True)
# Create your views here.
#login required to access this page. will redirect to admin login page.
@login_required(login_url='/admin/login/')
def chat(request):
    return render(request,"pusherchat/chat.html")

@csrf_exempt
def broadcast(request):
    pusher.trigger(u'a_channel', u'an_event', {u'name': request.user.username, u'message': request.POST['message']})
    return HttpResponse("done")
