from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer

from .models import Profile
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Create':'/task-create/',
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Profile.objects.all().order_by('-id')
	serializer = ProfileSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):

	
	serializer = ProfileSerializer(data=request.data)
	

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)
