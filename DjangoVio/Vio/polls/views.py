from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question,Choice,OverTimeWork

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
			pub_date__lte=timezone.now()
		).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list,
    }
    return HttpResponse(template.render(context,request))

def SCindex(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'question':question})

def SCdetail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def WOT(request):
    return render(request,'workovertime.html')
def OTW(request):
    messages = request.POST.get("OTW")
    # messages = "杨过 xwx12315 神雕 小龙女 侠侣 郭靖 抗金守卫战 2020/7/4 8:30 2020/7/4 18:00\n 杨过 xwx12315 神雕 小龙女 侠侣 郭靖 抗金守卫战 2020/7/4 8:30 2020/7/4 18:00"
    msg = messages.split("\n")
    for line in msg:
        tmo = line.split()
        if len(tmo) == 11:
            data = {'name' : tmo[0],
        'jobid' : tmo[1],
        'corporate_firm' :tmo[2],
        'group_leader' : tmo[3],
        'project_team' : tmo[4],	
        'project_manager' : tmo[5],
        'reason' : tmo[6],
        'begindate' :" ".join(tmo[7:9]),
        'begindate'  " ".join(tmo[9:11]}
            OverTimeWork.objects.create(**data)
        else:
            return HttpResponse("<p>熊羊羊 xwx236085 易宝 倪巾钧 融合计费 孙建兵 版本基线调试 2020/7/4 8:30 2020/7/4 18:00</p><br><p> 熊羊羊 xwx236085 易宝 倪巾钧 融合计费 孙建兵 版本基线调试 2020/7/4 8:30 2020/7/4 18:00</p>")
    