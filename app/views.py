from django.shortcuts import render

# Create your views here.

def If_condition(request):
    d={'a':50,'b':30}
    return render(request,'if-condition.html',d)

def If_else_condition(request):
    d={'a':50,'b':90}
    return render(request,'if-else_condition.html',context=d)

def If_elif_condition(request):
    d={'a':50,'b':90,'c':100}
    return render(request,'if-elif_condition.html',context=d)

def Nested_condition(request):
    d={'a':50,'b':90,'c':100}
    return render(request,'nested-condition.html',context=d)


def for_loop(request):
    d={'name':'CHANDANA!'}
    return render(request,'loop.html',context=d)

