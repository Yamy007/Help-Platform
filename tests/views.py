from django.shortcuts import render
from .models import *
from math import *
# Create your views here.


def index(request, id):
    test = Question.objects.filter(test_id=id)
    return render(request, "test/index.html", {"test": test, "id": id})


def result(request, id):
    questions = Question.objects.filter(test_id=id).count()
    result_count = Result.objects.filter(test_id=id).count()
    list_key = []
    answer = 0
    if request.method == "POST":
        for i in request.POST:
            list_key.append(i)
        for i in range(len(request.POST)):
            if request.POST.get(list_key[i]) == "1":
                answer += 1
        for i in range(len(request.POST)):
            if request.POST.get(list_key[i]) == "2":
                answer += 0.5
        for i in range(len(request.POST)):
            if request.POST.get(list_key[i]) == "3":
                answer += 0.75

        lvl = ceil(answer/questions*10)
        if lvl == 0:
            lvl = 1 
        result = Result.objects.filter(test_id=id, lvl=lvl)
        print(lvl)
        
        if len(result) == 0 and lvl >=5:
            while lvl > 0:
                if len(Result.objects.filter(test_id=id, lvl=lvl)) != 0:
                    break
                else:
                    lvl -= 1

            result = Result.objects.filter(test_id=id, lvl=lvl)
            return render(request, "test/result.html", {"result": result})
        elif len(result) == 0 and lvl < 5:
            while lvl > 0:
                if len(Result.objects.filter(test_id=id, lvl=lvl)) != 0:
                    break
                else:
                    lvl += 1

            result = Result.objects.filter(test_id=id, lvl=lvl)
            return render(request, "test/result.html", {"result": result})
        else:
            return render(request, "test/result.html", {"result": result})


def about(request):
    return render(request, "test/about.html")


def choose(request):
    choose_test = Test.objects.all()
    return render(request, "test/choose_test.html", {"tests": choose_test})
