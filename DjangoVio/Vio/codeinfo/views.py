from django.shortcuts import render,HttpResponse
from datetime import datetime
from .models import CodeInfo,CodeInfoSpe
# Create your views here.
def index(request):
	return render(request,"codeinfo/index.html")

def codeadd(request):
	return render(request,"codeinfo/add.html")
def codesave(request):
	# for spe
	module = request.POST.get('模块',max_length=20,null=False)
	source = request.POST.get('源文件名',max_length=20,null=False)
	errcode = request.POST.get('告警错误码',max_length=20,null=False)
	errattr = request.POST.get('告警属性',max_length=50,null=False)
	errpara = request.POST.get('告警参数',max_length=50,null=False)
	syseffect = request.POST.get('系统影响',max_length=512,null=True)
	sysproc = request.POST.get('系统处理过程')
	cause = request.POST.get('原因',max_length=512,null=True)
	procstep = request.POST.get('处理步骤', max_length=256, null=True)
	upgradedate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	model = CodeInfo(module=module, source=source, errcode=errcode, errattr=errattr, errpara=errpara,
					 syseffect=syseffect, sysproc=sysproc, cause=cause,procstep=procstep,upgradedate=upgradedate)
	model.save()

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


def codesearch(request):
	q = request.GET.get('q')
	error_msg = ''
	if not q:
		error_msg = '请输入关键词'
		return HttpResponse(f"{error_msg}")
	# 设计对所有字段进行检索
	context = CodeInfo.objects.filter(code__icontains=q)
	return render(request,'codeinfo/results.html',context=context)
