from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse

# def send_test_email(request):
#     subject = 'Welcome to my blog'
#     message = 'This is a test email sent from Django.'
#     from_email = 'zaroonjunaidaslam@gmail.com'
#     recipient_list = ['junaid.edu27@gmail.com']
#     send_mail(subject, message, from_email, recipient_list)
#     return HttpResponse('Email sent successfully!')

def send_test_email(request):
    subject = 'Welcome to my blog'
    message = render_to_string('email/welcome_email.html', {'name': 'junaid','course': 'Django'})

    email = EmailMessage(
        subject,
        message,
        "zaroonjunaidaslam@gmail.com",
        ['junaid.edu27@gmail.com']
    )
    email.content_subtype = 'html'  # Set the content type to HTML
    email.send()
    return HttpResponse('Email sent successfully!')