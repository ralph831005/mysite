import base64

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Pyro5.api import Proxy

from .forms import UserForm
from .models import Photo, Receipt, Item


def index(request):
    return render(request, 'scanner/index.html')


def login_view(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            data = userform.cleaned_data
            # print(f'logging attempt: {data["usernmae"]}, {data["password"]}')
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next', '/'))  # Replace with your desired redirect
        messages.error(request, "Invalid username or password.")
    else:
        userform = UserForm()
    return render(request, 'scanner/login.html', {'form': userform})


@login_required(login_url='/scanner/login')
def scanner(request):

    if request.method == "POST":
        # Check if this is a base64-encoded image (camera capture)
        if 'photo' in request.POST:
            image_data = request.POST['photo']
            format_, imgstr = image_data.split(';base64,')
            ext = format_.split('/')[-1]
            photo = ContentFile(base64.b64decode(imgstr), name=f"capture.{ext}")
        else:
            # File upload (photo from input)
            photo = request.FILES['photo']

        # Save photo to the database
        photo_instance = Photo.objects.create(image=photo)


        p = Proxy('PYRONAME:mysite.receipt_recognizer')
        receipt_detail = p.parse(photo_instance.image.path)
        # receipt_detail = mock(photo_instance.image.path)

        receipt_attr = ['store', 'total_price', 'tax', 'tax_rate', 'purchase_date']
        receipt_instance = Receipt.objects.create(
            **{name: value for name, value in receipt_detail.items()
               if name in receipt_attr and value is not None})

        for item in receipt_detail['items']:
            Item.objects.create(receipt_id=receipt_instance.id, **item)

        return render(
            request,
            'scanner/scanner.html',
            {
                'photo_url': photo_instance.image.url,
                'receipt': receipt_detail,
            },
        )
    return render(request, 'scanner/scanner.html')


def mock(path):
    return {
        'store': 'Test',
        'total_price': 100.00,
        'tax': 10,
        'tax_rate': 11.1,
        'purchase_date': '2024-10-11',
        'items': [{'item': 'Apple', 'price': 10}, {'item': 'Orange', 'price': 90}],
    }
