from django.shortcuts import render,HttpResponse
from .models import msgboard
from django.views.decorators.clickjacking import xframe_options_exempt
from datetime import datetime
import requests

# Create your views here.
def hi(request):
	if request.method == 'GET':
		msg = msgboard.objects.order_by('msgdate').reverse()[:5]
		context = {"messages":msg}
		return render(request,"navi/index.html",context=context)

@xframe_options_exempt
def msgb(request):
	if request.method == 'GET':
		msg = msgboard.objects.all()
		context = {"messages":msg}
		return render(request,"navi/messageboard.html",context=context)

def msgsave(request):
	visitor = request.POST.get("visitor")
	email = request.POST.get("email")
	message = request.POST.get("message")
	if message.strip() == "":
		return HttpResponse("naughty you are.lol ")
	else:
		msgdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		model = msgboard(visitor=visitor,msgdate=msgdate,email=email,message=message)
		model.save()
		return HttpResponse(f'msgboard<visitor = {visitor},msgdate = {msgdate},email = {email}\n {message}')

def wttr(request):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
			   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
	req = requests.get('http://wttr.in/Guangzhou?1_lang=zh-cn', headers=headers,timeout=20)
	# 需要解决远端网站的css调用
	text = req.text.replace(r"/files/style.css",r"http://wttr.in/files/style.css")
	return HttpResponse(text)