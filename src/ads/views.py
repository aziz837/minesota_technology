from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse

def ads(request):
	products = Product.objects.all()
	partners = Partners.objects.all()
	contacts = Contact.objects.get(pk=1)
	carts = Cart.objects.all()
	info = Info.objects.get(pk=1)
	context= {
		'products':products,
		'partners':partners,
		'contacts':contacts,
		'info': info,
		'carts':carts
		}
	return render(request, 'main/index.html', context )