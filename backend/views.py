from django.http import HttpResponse, JsonResponse

# Create your views here.
from backend.utils.fib import helper_fib


def hello_world(request):
	return HttpResponse("Hello World")


def test_api(request):
	return JsonResponse({"hi": 3}, status=202)


def create_fib(request):  # how to parse data from url
	val = [1]
	values = helper_fib(1, 100, val)
	return JsonResponse(dict(zip(values, values)), status=200)
