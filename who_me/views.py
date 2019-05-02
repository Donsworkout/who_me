from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from pandas.io.json import json_normalize
import os
import sys
import requests
import json

def index(request):
    return render(request, 'index.html', {})


def face_recognition(request):
    if request.is_ajax():
        client_id = get_secret('CLIENT_ID') 
        client_secret = get_secret('CLIENT_SECRET')
        # url = "https://openapi.naver.com/v1/vision/face"  얼굴감지
        url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식
        files = {'image': request.FILES['image'] }
        headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
        response = requests.post(url,  files=files, headers=headers)
        rescode = response.status_code
        if(rescode==200):
            print (response.text)
        else:
            print(json.loads(response.text))      
    return render(request, 'index.html', {})


# 아래는 secret_key 로딩 
BASE_DIR = settings.BASE_DIR
secret_file = os.path.join(BASE_DIR, 'secret.json')

with open(secret_file, 'r') as f:
    secret = json.loads(f.read())

def get_secret(setting, secret=secret):
    try:
        return secret[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)