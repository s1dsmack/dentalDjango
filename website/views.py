from django.shortcuts import render
from django.core.mail import send_mail
from django.template.defaultfilters import linebreaks
from django.template.defaultfilters import linebreaksbr

def home(request):
	'''return render(request, 'home.html', {})'''

	if request.method == "POST":
		#do stuff
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_time = request.POST['your-time']
		your_message = request.POST['your-message']
		

		# Send email
		send_mail(
			'Message From: ' + your_name, # subject			
			'Phone: ' + your_phone + ' | Address: '+ your_address + ' | Time (Mon-Wed): ' + your_schedule + ' | Time (Thu-Fri): ' + your_time + ' | Message: ' + your_message, # message
			your_email, # from email
			#your_phone, # from phone number
			#your_address, # from address
			#your_schedule, # schedule selected
			#your_time, # time selected
			['info.garfieldyoungdds@gmail.com'], # to email
			fail_silently=False,
			)

		return render(request, 'home.html', {'your_name':your_name})

	else:
		# return the page
		return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		#do stuff
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message'] 
		

		# Send email
		send_mail(
			'Message From: ' + message_name, # subject
			message, # message
			message_email, # from email
			['info.garfieldyoungdds@gmail.com'], # to email
			fail_silently=False,
			)

		return render(request, 'contact.html', {'message_name':message_name})

	else:
		# return the page
		return render(request, 'contact.html', {})

''' Keep syntax for later
def appointment(request):
	if request.method == "POST":
		#do stuff
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_time = request.POST['your-time']
		your_message = request.POST['your-message'] 
		

		# Send email
		send_mail(
			'Message From: ' + your_name, # subject
			your_message, # message
			your_phone, # from phone number
			your_email, # from email
			your_address, # from address
			your_schedule, # schedule selected
			your_time, # time selected
			['info.garfieldyoungdds@gmail.com'], # to email
			fail_silently=False,
			)

		return render(request, 'home.html', {'your_name':your_name})

	else:
		# return the page
		return render(request, 'home.html', {})
'''

def about(request):
	return render(request, 'about.html', {})

def service(request):
	return render(request, 'service.html', {})

def cleaning(request):
	return render(request, 'cleaning.html', {})

def missing(request):
	return render(request, 'missing.html', {})

def whitening(request):
	return render(request, 'whitening.html', {})

def cosmetic(request):
	return render(request, 'cosmetic.html', {})

def tpain(request):
	return render(request, 'tpain.html', {})	

def surgery(request):
	return render(request, 'surgery.html', {})

def credit(request):
	return render(request, 'credit.html', {})

def lending(request):
	return render(request, 'lending.html', {})

def insurance(request):
	return render(request, 'insurance.html', {})

def policy(request):
	return render(request, 'policy.html', {})

def faqs(request):
	return render(request, 'faqs.html', {})

def privacy(request):
	return render(request, 'privacy.html', {})

def gallery(request):
	return render(request, 'gallery.html', {})

