from django.shortcuts import render
from .models import Topic as TopicModel
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm as TopicFormModel
def index(request):
	return render(request, 'learning_logs/index.html')
def topics(request):
	#Внимание эта хуета работает только если топик импортировать как топикМодель!!!
	topics = TopicModel.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html',context)
def topic(request,topic_id):
	topic = TopicModel.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topics':topic,'entries':entries}
	return render(request, 'learning_logs/topic.html',context)
def new_topic(request):
	if request.method != 'POST':
		form = TopicFormModel()
	else:
		form = TopicFormModel(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))
	context = {'form':form}
	return render(request,'learning_logs/new_topic.html', context)
	