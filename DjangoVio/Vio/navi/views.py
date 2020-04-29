from django.shortcuts import render,HttpResponse
from django.http import JsonResponse,HttpResponseRedirect
from django.views.decorators.clickjacking import xframe_options_exempt
from .models import MsgBoard,VisitorInfo
from datetime import datetime
import requests

# Create your views here.
def index(request):
	if request.method == 'GET':
		if request.META.get('HTTP_X_FORWARDED_FOR'):
			ip = request.META['HTTP_X_FORWARDED_FOR']
		else:
			ip = request.META['REMOTE_ADDR']
		vis = VisitorInfo(visitor=ip,visdate=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		vis.save()
		msg = MsgBoard.objects.order_by('msgdate').reverse()[:5]
		context = {"messages":msg,"ip":ip}
		return render(request,"navi/index.html",context=context)

@xframe_options_exempt
def msgb(request):
	if request.method == 'GET':
		msg = MsgBoard.objects.all()
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
		model = MsgBoard(visitor=visitor, msgdate=msgdate, email=email, message=message)
		model.save()
		# return HttpResponse(f'MsgBoard<visitor = {visitor},msgdate = {msgdate},email = {email}\n {message}')
		return HttpResponseRedirect("/")
def wttr(request):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
			   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
	req = requests.get('http://wttr.in/Guangzhou?1_lang=zh-cn', headers=headers,timeout=20)
	# 需要解决远端网站的css调用
	text = req.text.replace(r"/files/style.css",r"http://wttr.in/files/style.css")
	return HttpResponse(text)

def viscount(request):
	"""
	:param request:
	:return: json格式的访问统计index页统计
	"""
	vistoday = VisitorInfo.objects.filter(visdate__gte=datetime.now().strftime("%Y-%m-%d")).count()
	vishisday = VisitorInfo.objects.count()
	return JsonResponse({"today":vistoday,
						 "history":vishisday})
