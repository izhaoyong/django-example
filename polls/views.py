from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import BookInfo
import json
import logging


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

	template = loader.get_template('polls/vote.html')
	context = {
		'question_id':  question_id
	}

	return render(request, 'polls/vote.html', context)


logger = logging.getLogger(__name__)
@csrf_exempt
def post_message(request):


	bookInfo = BookInfo(source_id='35463546', author='hao', info='{"name": "hello"}')

	# import pdb
	# pdb.set_trace()

	bookInfo.save()
	print(bookInfo)

	response = {
		'status': 200
	}
	return HttpResponse(json.dumps(response), content_type='application/json')


@csrf_exempt
def upload_file(request):

	print(request.method)
	file = request.FILES.get('file')
	print(file.name)
	file_content = file.read()
	print(file_content)

	# import pdb
	# pdb.set_trace()

	fileObject = open('./test.json', 'wb')
	for chunk in file.chunks():
		fileObject.write(chunk)
	fileObject.close()

	response = {
		'status': 200
	}
	return HttpResponse(json.dumps(response), content_type='application/json')
