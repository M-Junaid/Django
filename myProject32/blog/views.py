from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.template.loader import render_to_string

# def bulk_email(request):
#     messages1 = ('welcome user1, welcome to our platform,', 'Hello user1, welcome to our platform!', 'zaroonjunaidaslam@gmail.com', ['junaid.edu27@gmail.com'])

#     send_mass_mail((messages1,), fail_silently=False)
#     return HttpResponse("Bulk email sent successfully.")

def send_bulk_email(request):
    subject = 'Welcome to Our Platform'
    from_email = 'zaroonjunaidaslam@gmail.com'
    recipients_list = ['junaid.edu27@gmail.com']

    html_content = render_to_string('welcome_email.html', {'user': 'Junaid'})

    msg = EmailMultiAlternatives(subject, 'welcome to our platform!', from_email, recipients_list)
    msg.attach_alternative(html_content, "text/html")
    # msg.attach_file('path/to/attachment.pdf', 'application/pdf')  # Attach a file if needed
    msg.send()

    return HttpResponse("Bulk email sent successfully.")


def bulk_email(request):
    return send_bulk_email(request)
