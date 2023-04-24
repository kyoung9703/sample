from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random
# 같은 위치의 models.py 불러오기 + emp 클래스 불러오기
# from .models import emp
from .models import emp, night_pharmacy, accident as acc

# 무조건 함수
def index(request):
    return HttpResponse(
        '''<h1 style="color:red;">Hello</h1>'''
    )

def main(request):
    num = random.randint(1, 45)
    emp_list = emp.objects.all()
    print(emp_list)
    return render(request, 'bookmark.html', {'num': num, 'emp_list': emp_list})


    return HttpResponse(
        'main %s' %num
        # '''<h1 style="color:blue;">Main</h1>'''
    )



def night(request):
    night_list = night_pharmacy.objects.all()
    print(night_list)
    return render(request, 'night.html', {'night_list': night_list})


def accident(request):
    acc_list = acc.objects.all()
    print(acc_list)
    return render(request, 'accident.html', {'acc_list': acc_list})
