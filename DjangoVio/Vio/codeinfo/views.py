from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.db.utils import IntegrityError
from django.db.models import Q
from datetime import datetime,timedelta
from django.core.exceptions import ObjectDoesNotExist
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
		return HttpResponseRedirect('codeinfo/results', context=context)
def deleteid(request):
	id = request.GET['id']
	result=CodeInfo.objects.get(pk=id)
	if result.upgradedate+timedelta(minutes=10)<=datetime.now():
		result.delete()
		# 这里回复ok会有searchresults.html的js校验，别乱改
		return HttpResponse('ok')
	else:
		return HttpResponse('<script type="text/javascript"> alert("10分钟以上数据不允许删除，请联系管理员");window.location.href="/codeinfo/delete"</script>')


def deleteconfirm(request):
	module = request.POST.get('module')
	source = request.POST.get('source')
	errcode = request.POST.get('errcode')
	try:
		result=''
		if module and source and errcode:
			result=CodeInfo.objects.get(Q(module__exact=module)&Q(source__exact=source)&Q(errcode__exact=errcode))
		elif module and source :
			result=CodeInfo.objects.get(Q(module__exact=module)&Q(source__exact=source))
		elif source and errcode :
			result=CodeInfo.objects.get(Q(source__exact=source)&Q(errcode__exact=errcode))
		elif module:
			return HttpResponse('<script type="text/javascript">alert("不允许仅按模块删除");</script>')
		elif source:
			return HttpResponse('<script type="text/javascript">alert("不允许仅按源文件删除");</script>')
		elif errcode:
			result=CodeInfo.objects.get(errcode__exact=errcode)
		if result.upgradedate + timedelta(minutes=10) <= datetime.now():
			result.delete()
			# msg = "from module:{module} errcode:{errcode} delete success."
			return HttpResponse('<script type="text/javascript">alert("删除成功");</script>')
		else:
			return HttpResponse(
				'<script type="text/javascript"> alert("10分钟以上数据不允许删除，请联系管理员");window.location.href="/codeinfo/delete"</script>')

	except ObjectDoesNotExist as e:
		return HttpResponse('<script type="text/javascript">alert("数据不存在，删除失败");</script>')

def codesave(request):
	# for spe
	module = request.POST.get('module')
	source = request.POST.get('source')
	errcode = request.POST.get('errcode')
	err_msg = ''
	errattr = request.POST.get('errattr')
	if len(errattr) > 50:
		err_msg = "<p>告警属性超过50字符</p>"
	errpara = request.POST.get('errpara')
	if len(errpara) > 50:
		err_msg = err_msg + "<p>告警参数超过50字符</p>"
	syseffect = request.POST.get('syseffect')
	if len(syseffect) > 512:
		err_msg = err_msg + "<p>系统影响超过512字符</p>"
	sysproc = request.POST.get('sysproc')
	if len(sysproc) > 512:
		err_msg = err_msg + "<p>系统处理过程超过512字符</p>"
	cause = request.POST.get('cause')
	if len(cause) > 512:
		err_msg = err_msg + "<p>可能原因超过512字符</p>"
	procstep = request.POST.get('procstep')
	if len(procstep) > 256:
		err_msg = err_msg + "<p>处理步骤超过256字符</p>"
	if len(err_msg)>0:
		err_msg = '<h1>报错信息如下</h1>' + err_msg
		return HttpResponse(err_msg)
	upgradedate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	model = CodeInfo(module=module, source=source, errcode=errcode, errattr=errattr, errpara=errpara,
					 syseffect=syseffect, sysproc=sysproc, cause=cause,procstep=procstep,upgradedate=upgradedate)
	try:
		model.save()
		id = model.id
		# return HttpResponse(f'Code Info add successfully.From module:{module},code:{errcode}')
		msg = f'<script type="text/javascript">alert("提交成功");window.location.href="/codeinfo/detail/{id}";</script>'
		return HttpResponse(msg)
	except IntegrityError as e:
		msg = f'<p>{e}</p><script type="text/javascript">alert("提交失败");</script>'
		return HttpResponse(msg)

def coderesults(request):
	if request.method == "GET":
		searchtext = CodeInfo.objects.order_by('upgradedate').reverse()[:100]
		count = searchtext.count()
		context = {'messages':searchtext,
				   'resultscount':count}
		return render(request,'codeinfo/searchresults.html',context=context)

def coderesultpagin(request,page):
	if request.method == "GET":
		searchtext = CodeInfo.objects.order_by('upgradedate').reverse()
		count = searchtext.count()
		messages = searchtext[5*(page-1):5*page]
		context = {'messages':messages,
				   'resultscount':count,
				   'page':page}
		return render(request,'codeinfo/searchresults.html',context=context)

def codesearch(request):
	q = request.GET.get('q')
	error_msg = ''
	if not q:
		error_msg = '<script type="text/javascript">alert("这！...-_-!");alert("不会说话，难道还不能打个字吗？");alert("回去再谈");window.location.href="/";</script>'
		return HttpResponse(f"{error_msg}")
	# 设计对所有字段进行检索
	searchtext = CodeInfo.objects.filter(errcode__icontains=q)
	count = searchtext.count()
	context = {'messages':searchtext,
			   'resultscount':count}
	return render(request,'codeinfo/searchresults.html',context=context)

def codemodify(request):
	return render(request,"codeinfo/modify.html")

def codemodifyid(request,id):
	message = CodeInfo.objects.get(id=id)
	context = {'message': message }
	return render(request,"codeinfo/modify.html",context=context)

def modifyconfirm(request):
	module = request.POST.get('module')
	source = request.POST.get('source')
	errcode = request.POST.get('errcode')
	model = CodeInfo.objects.filter(Q(module__exact=module)&Q(source__exact=source)&Q(errcode__exact=errcode))
	err_msg = ''
	errattr = request.POST.get('errattr')
	if len(errattr) > 50:
		err_msg = "<p>告警属性超过50字符</p>"
	errpara = request.POST.get('errpara')
	if len(errpara) > 50:
		err_msg = err_msg + "<p>告警参数超过50字符</p>"
	syseffect = request.POST.get('syseffect')
	if len(syseffect) > 512:
		err_msg = err_msg + "<p>系统影响超过512字符</p>"
	sysproc = request.POST.get('sysproc')
	if len(sysproc) > 512:
		err_msg = err_msg + "<p>系统处理过程超过512字符</p>"
	cause = request.POST.get('cause')
	if len(cause) > 512:
		err_msg = err_msg + "<p>可能原因超过512字符</p>"
	procstep = request.POST.get('procstep')
	if len(procstep) > 256:
		err_msg = err_msg + "<p>处理步骤超过256字符</p>"
	if len(err_msg)>0:
		err_msg = '<h1>报错信息如下</h1>' + err_msg
		return HttpResponse(err_msg)
	mdict = {}
	if errattr and errattr!=model[0].errattr:
		mdict.update({'errattr':errattr})
		# model.update(errattr=errattr)
	if errpara and errpara!=model[0].errpara:
		mdict.update({'errpara':errpara})
		# model.update(errpara=errpara)
	if syseffect and syseffect!=model[0].syseffect:
		mdict.update({'syseffect': syseffect})
		# model.update(syseffect=syseffect)
	if sysproc and sysproc!=model[0].sysproc:
		mdict.update({'sysproc': sysproc})
		# model.update(sysproc=sysproc)
	if cause and cause!=model[0].cause:
		mdict.update({'cause': cause})
		# model.update(cause=cause)
	if procstep and procstep!=model[0].procstep:
		mdict.update({'procstep': procstep})
		# model.update(procstep=procstep)
	if len(mdict)==0:
		return HttpResponse(f'<script type="text/javascript">alert("无改动");</script>')
	upgradedate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	mdict.update({'upgradedate': upgradedate})
	model.update(**mdict)
	id = model[0].id
	msg = f'<script type="text/javascript">alert("修改成功");window.location.href="/codeinfo/detail/{id}";</script>'
	return HttpResponse(msg)

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

def codedetail(request,id):
	message = CodeInfo.objects.get(id=id)
	context = {'message': message }
	return render(request,'codeinfo/detail.html',context=context)