from django.shortcuts import render
from django.http import JsonResponse
import uuid
from django.contrib import messages
import qrcode
from io import BytesIO
import base64

def home(request):
    return render(request, 'core/base.html')

def qrGenerator(request):
    data = request.GET.get('text')
    is_api_request = (
        request.path == '/apiEnd/' or 
        request.headers.get('Content-Type') == 'application/json' or
        'application/json' in request.headers.get('Accept', '')
    )
    
    if data:
        qr = qrcode.QRCode()
        qr.add_data(data)
        img = qr.make_image()
        buffer = BytesIO()
        img.save(buffer, format='png')
        buffer.seek(0)
        img_url = base64.b64encode(buffer.getvalue()).decode()
        if is_api_request:
            return JsonResponse({'status':200, 'img_url':img_url, 'data':data})
        else:
            return JsonResponse({'status':200, "img_url":img_url})
    
    return JsonResponse({'status':400, 'failer': 'no data found'})