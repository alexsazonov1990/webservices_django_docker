from django.shortcuts import render
from .models import ApplicationForDevelopmentCard
from .forms import PostForm
from .forms import AttachForm
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import requests
import json
from django.core.mail import EmailMessage  # не то передевал


# Create your views here.

def create_request(request):
    if request.method == 'POST' or request.FILES.get('upload'):
        form = PostForm(request.POST, request.FILES)
        form_attach = AttachForm(request.POST, request.FILES)
        if form.is_valid():  # Пометить какие поля не обязательны для заполнения
            post = form.save(commit=False)
            post.save()  # сохранили
            cd = form.cleaned_data  # получили данные с формы
            # отправка на почту в отдел разработки
            subject = "Задача на разработку: " + cd['topic']
            message = "-----------------------------------------------------------------\n" + "Что разрабатываем - " \
                                                                                              "дорабатываем: \n\n" + \
                      cd['topic'] + \
                      "\n---------------------------------------------------------------" + "\n\nЧто должно " \
                                                                                            "получиться в готовом " \
                                                                                            "варианте:\n\n" + \
                      cd['purpose'] + \
                      "\n---------------------------------------------------------------" + "\n\nКакую проблему " \
                                                                                            "решает доработка?К чему " \
                                                                                            "мы хотим прийти в " \
                                                                                            "итоге:\n\n" + \
                      cd['why_necessary'] + \
                      "\n---------------------------------------------------------------" + "\n\nКто будет " \
                                                                                            "использовать?\n\n" + \
                      cd['why_use_it'] + \
                      "\n---------------------------------------------------------------" + "\n\nГде будут " \
                                                                                            "использовать?\n\n" + \
                      cd['where_used'] + \
                      "\n---------------------------------------------------------------" + "\n\nФИО заказчика:\n\n" + \
                      cd['full_name_customer'] + \
                      "\n---------------------------------------------------------------" + "\n\nEmail: \n\n" + cd[
                          'email']

            try:
                attach12 = request.FILES.get('upload')
                print("Имя вложения:" + str(attach12.name))
                # handle_uploaded_file(request.FILES['upload'])
                fs = FileSystemStorage()
                print("ФС:" + str(fs))
                attach1 = fs.save(attach12.name, attach12)
                print(fs.path)
                uploaded_file_url = fs.url(attach1)
                print(uploaded_file_url)
                email = EmailMessage(subject, message, '', ['','',''])
                email.attach_file('media/' + attach12.name)
                email.send(fail_silently=False)
            except Exception:
                email = EmailMessage(subject, message, '', ['','',''])  # '
            # email.attach(attach12.name, attach12.read(), attach12.content_type)
                email.send(fail_silently=False)

            # Глюк найден, приходит пустое вложение.
            # ----Добавим карточку в трело----

            url = "https://api.trello.com/1/cards"
            query = {
            #    'key':  
            #    'token': ,
            #    'idList':,
            #    'name': subject,
            #    'desc': message,
                # 'file': attach12.read()
            }
            print('idCardSource')
            response = requests.request(
                "POST",
                url,
                params=query
            )
            print(response.status_code)
            print('Создали задачу на согласование в службу разработки')
            form = PostForm()  # очистим форму после отправки
            return render(request, 'appfordev/create_taskdev.html',
                          {'form': form, 'form_attach': form_attach, 'alert_flag': True})#'uploaded_file_url': uploaded_file_url}

    else:
        form = PostForm()
        form_attach = AttachForm()

    return render(request, 'appfordev/create_taskdev.html',
                  {'form': form, 'form_attach': form_attach})  # 'form': form ,'sent':sent


'''
# загрузка файла
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'appfordev/file_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'appfordev/file_upload.html')'' 
'''
