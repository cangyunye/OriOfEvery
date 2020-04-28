from django.shortcuts import render,HttpResponse
from django.db.utils import IntegrityError
from django.db.models import Q
from datetime import datetime,timedelta
from .models import CodeInfo,CodeInfoSpe
# Create your views here.
def index(request):
	countlastday = CodeInfo.objects.filter(upgradedate__day=(datetime.today()-timedelta(days=1)).day).count()
	countall = CodeInfo.objects.count()
	context = {'countlastday':countlastday,
			   'countall':countall}
	return render(request,"codeinfo/index.html",context=context)

def codeadd(request):
	return render(request,"codeinfo/add.html")

def codedelete(request):
	return render(request,"codeinfo/delete.html")

def deletesearch(request):
	module = request.POST.get('module')
	source = request.POST.get('source')
	errcode = request.POST.get('errcode')
	if request.method == "GET":
		searchresult = CodeInfo.objects.filter(Q(module__exact=module)|Q(source__startswith=source)|Q(errcode__exact=errcode))
		context = {'messages':searchresult}
		return render(request,'codeinfo/searchresults.html',context=context)

def delete(request):
	module = request.POST.get('module')
	source = request.POST.get('source')
	errcode = request.POST.get('errcode')
	if module and source and errcode:
		CodeInfo.objects.get(Q(module__exact=module)&Q(source__exact=source)&Q(errcode__exact=errcode)).delete()
	elif module and source :
		CodeInfo.objects.get(Q(module__exact=module)&Q(source__exact=source)).delete()
	elif source and errcode :
		CodeInfo.objects.get(Q(source__exact=source)&Q(errcode__exact=errcode)).delete()
	elif module:
		CodeInfo.objects.get(module__exact=module).delete()
	elif source:
		CodeInfo.objects.get(source__exact=source).delete()
	elif errcode:
		CodeInfo.objects.get(errcode__exact=errcode).delete()
	return HttpResponse(f'{errcode} delete success.')

def codesave(request):
	# for spe
	module = request.POST.get('module')
	source = request.POST.get('source')
	errcode = request.POST.get('errcode')
	errattr = request.POST.get('errattr')
	errpara = request.POST.get('errpara')
	syseffect = request.POST.get('syseffect')
	sysproc = request.POST.get('sysproc')
	cause = request.POST.get('cause')
	procstep = request.POST.get('procstep')
	upgradedate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	model = CodeInfo(module=module, source=source, errcode=errcode, errattr=errattr, errpara=errpara,
					 syseffect=syseffect, sysproc=sysproc, cause=cause,procstep=procstep,upgradedate=upgradedate)
	try:
		model.save()
		return HttpResponse(f'code info add successfully.from module:{module},code:{errcode}')
	except IntegrityError as e:
		return HttpResponse(f'{e}')

def coderesults(request):
	if request.method == "GET":
		searchtext = CodeInfo.objects.all()
		context = {'messages':searchtext}
		return render(request,'codeinfo/searchresults.html',context=context)

def codesearch(request):
	q = request.GET.get('q')
	error_msg = ''
	if not q:
		error_msg = '请输入关键词'
		return HttpResponse(f"{error_msg}")
	# 设计对所有字段进行检索
	context = CodeInfo.objects.filter(code__icontains=q)
	return render(request,'codeinfo/results.html',context=context)

def codespesave(request):
	module =  request.POST.get('module')
	codefile = request.POST.get('codefile')
	code = request.POST.get('code')
	codesummary = request.POST.get('codesummary')
	solution = request.POST.get('solution')
	codeclip = request.POST.get('codeclip')
	docinfo = request.POST.get('docinfo')
	upgradedate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	model = CodeInfoSpe(module=module, codefile=codefile, code=code, codesummary=codesummary, solution=solution,
					 codeclip=codeclip, docinfo=docinfo, upgradedate=upgradedate)
	model.save()
	return HttpResponse(f'codeinfo:module = {module},codefile = {codefile},code = {code}')

def codesperesult(request):
	if request.method == "GET":
		searchtext = CodeInfo.objects.all()
		context = {'messages':searchtext}
		return render(request,'codeinfo/results.html',context=context)


def codeload(request):
	if request.method == "GET":
		return render(request,'codeinfo/upload.html')


def codespesearch(request):
	q = request.GET.get('q')
	error_msg = ''
	if not q:
		error_msg = '请输入关键词'
		return HttpResponse(f"{error_msg}")
	# 设计对所有字段进行检索
	context = CodeInfo.objects.filter(code__icontains=q)
	return render(request,'codeinfo/results.html',context=context)
