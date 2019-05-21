from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
def index(request):
	return HttpResponse('Hello world! This is a polls app')

def test(request):
	return HttpResponse('test route')


def template(request):
	latest_question_list = [
		{
			'id': 1,
			'question_text': "hahah"
		},
		{
			'id': 2,
			'question_text': "ahahah"
		},
	]
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list
	}
	return HttpResponse(template.render(context, request))


def vote(request, question_id):
	queryDict = request.GET;
	param = queryDict.get('param')
	print(int(param))

	template = loader.get_template('polls/vote.html')
	context = {
		'question_id':  question_id
	}

	return render(request, 'polls/vote.html', context)

@csrf_exempt
def post_message(request):
	# import pdb
	# pdb.set_trace()

	print(request.method)
	response = {
		'status': 200
	}

	return HttpResponse(json.dumps(response), content_type='application/json')
