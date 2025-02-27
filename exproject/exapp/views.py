from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def demo(request):
#     return HttpResponse('new project')

# def demo(request):
#     return render(request,'form.html')


def demo(request):
    output=''
    if request.method=='POST':
        num1=eval(request.POST.get('fn'))
        num2=eval(request.POST.get('sn'))
        main=request.POST.get('opr')
        if main=='+':
            output=num1+num2
        elif main=='-':
            output=num1-num2
        elif main=='*':
            output=num1*num2
        elif main=='/':
            output=num1/num2
    return render(request,'form.html',{'o':output})