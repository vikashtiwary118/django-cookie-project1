from django.shortcuts import render

# Create your views here.

def count_view(request):
	count=int(request.COOKIES.get('count',0))
	newcount=count+1
	response= render(request,'testapp/count.html',{'count':newcount})
	response.set_cookie('count',newcount)
	return response

###permanent cookies
def per_count_view(request):
	count=int(request.COOKIES.get('count',0))
	newcount=count+1
	response= render(request,'testapp/count.html',{'count':newcount})
	response.set_cookie('count',newcount,max_age=1)
	return response

