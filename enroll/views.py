from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User,comment,commentForm
from django.contrib import messages





def add_comment(request):
   if request.method == 'POST':
        NAME=request.POST['1']
        COMMENT = request.POST['2']
        RATE = request.POST['rate']
        print(RATE)
        c= comment(subject=NAME, comment1=COMMENT ,rate=RATE)
        c.save()
        d = comment.objects.all()
        
        return render(request,'enroll/addandshow.html',{'com':d})
   else:
        d = comment.objects.all()
        
        return render(request,'enroll/addandshow.html',{'com':d}) 