from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def app(request):
    return HttpResponse("app!")

def poetry(request):
    context={}
    context['title'] = '送别'
    context['content'] = '长亭外，古道边，芳草碧连天'
    return render(request,'poetry.html',context)
def poetry1(request):
    title = '静夜思'
    content = '床前明月光，疑是地上霜！'
    return render(request,'poetry.html',{'title':title,'content':content})
def poetry2(request):
    title='李白的诗歌'
    array=['静夜思','月下独酌','蜀道难']
    return render(request,'poetry2.html',{'title':title,'array':array})
def dictionary(request):
    person={
        'name':'xiongdu',
        'age':'23',
        'phone':'15236447077',
    }
    return render(request,'dictionary.html',{'person':person})