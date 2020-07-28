from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from app.models import *
import json
from django.views.decorators.csrf import csrf_exempt
from hashlib import sha1
from cryptography.fernet import Fernet

import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = "PasswordKepper"
password = password_provided.encode()
salt = b'salt_'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once

@csrf_exempt
def registerUser(request):
    if request.method == 'POST':
        user = json.loads(request.body)
        print(user)
        try:
            User.create(user['username'],sha1(user['password'].encode('utf-8')).hexdigest()).save()
            status = {'status': 'account created'}
        except:
            status = {'status' : 'cannot create the account'}
        return JsonResponse(status)

@csrf_exempt
def authUser(request):
    if request.method == 'POST':
        user = json.loads(request.body)
        print(user)
        try:
            encPassword = sha1(user['password'].encode('utf-8')).hexdigest()
            obj = get_object_or_404(User, username = user['username'], password = encPassword)
            status = {'status': 'success','userId': obj.id}
        except:
            status = {'status' : 'failed to login'}
        return JsonResponse(status)

@csrf_exempt
def getWebsites(request):
    if request.method == 'GET':
        try:
            userId = request.GET.get('user')
            print(userId)
            websites = Websites.objects.all().filter(userId=userId)
            print(websites)
            websiteData = []
            for website in websites:
                name = website.websiteName
                password = website.websitePassword
                username  = website.websiteUsername
                data = {'name' : name,'username':username, 'password':password}
                websiteData.append(data)
            status = {'websites':websiteData}
        except:
            status = {'status' : 'failed to show the list'}
        return JsonResponse(status)

@csrf_exempt
def addWebsite(request):
    if request.method == 'POST':
        try:
            global key

            userId = request.GET.get('user')
            print(userId)
            websiteData = json.loads(request.body)
            print(websiteData)
            #encPassword = sha1(websiteData['password'].encode('utf-8')).hexdigest()
            password = websiteData['password'].encode()
            f = Fernet(key)
            encPassword = f.encrypt(password).decode("utf-8")
            newWebsite = Websites.create(websiteName = websiteData['website'], websiteUsername = websiteData['username'], websitePassword = encPassword)
            print(newWebsite)
            newWebsite.save()
            try:
                newWebsite.userId.add(get_object_or_404(User,id=userId))
                status = {'status': 'success'}
                print('Decryppted Password = ' + f.decrypt(encPassword.encode('utf-8')).decode('utf-8'))
            except:
                Websites.objects.latest('id').delete()
                status = {'status': 'no such user exists'}
        except Exception as e:
            status = {'status' : 'failed to add the website'}
        return JsonResponse(status)