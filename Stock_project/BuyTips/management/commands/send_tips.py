from django.core.management.base import BaseCommand
from BuyTips.models import Tips, UserEmail
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        tips_obj = Tips.objects.all()

        template= get_template('email.html')

        context = Context({'tips_data': tips_obj})

        content = template.render(context.flatten())
        
        message = EmailMessage('smit', content, 'smitgol007@gmail.com', [user.email for user in UserEmail.objects.all()])
        message.content_subtype = 'html' 
        message.send()
        
