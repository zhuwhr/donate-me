# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

@login_required
def checkout(request):
	publishKey = settings.STRIPE_PUBLISHABLE_KEY
	if request.method == 'POST':
		token = request.POST.get('stripeToken', False)
		# Create a charge: this will charge the user's card
		try:
		  charge = stripe.Charge.create(
		      amount=1000, # Amount in cents
		      currency="usd",
		      source=token,
		      description="Example charge"
		  )
		except stripe.error.CardError as e:
		  # The card has been declined
		  pass
	context = {'publishKey': publishKey}
	template = 'checkout.html'
	return render(request,template,context)