from django.core.mail import send_mail
from config.celery import app
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import get_template 
from datetime import datetime
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from decouple import config

@app.task
def send_activation_code(email, code, first_name, last_name, phone, company,usdot,number_employees ):
    context = {
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "company": company,
        "usdot": usdot,
        "number_employees": number_employees,
        "code": f"{config('LINK')}{code}/",
        "year": 2024,
    }

    template_name = "email_template.html"
    convert_to_html_content = render_to_string(template_name, context)
    plain_message = strip_tags(convert_to_html_content)

    email_sent = send_mail(
        subject="Receiver information from a form",
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email, ],
        html_message=convert_to_html_content,
        fail_silently=False  # Или False, если хотите получать уведомления об ошибках
    )

    return email_sent


@app.task
def send_create_company(email, name, phone, home_terminal_address,
                                  home_terminal_timezone, company_address, last_name, first_name, code):
    context = {

        "email": email,
        "name": name,
        "phone": phone,
        "home_terminal_address": home_terminal_address,
        "home_terminal_timezone": home_terminal_timezone,
        "company_address": company_address,
        "year": 2024,
        "last_name": last_name,
        "first_name": first_name,
        "code": f"{config('LINK_COMPANY')}{code}/",

    }

    template_name = "email_company.html"
    convert_to_html_content = render_to_string(template_name, context)
    plain_message = strip_tags(convert_to_html_content)

    email_sent = send_mail(
        subject="Receiver information from a form",
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email, ],
        html_message=convert_to_html_content,
        fail_silently=False
    )


    return email_sent


@app.task
def send_delete_company(company_name, email, code, first_name, last_name):
    context = {
        "first_name": first_name,
        "last_name": last_name,
        "company_name": company_name,
        "email": email,
        "code": f"{config('LINK_DELETE_COMPANY')}{code}/",

    }

    template_name = "email_delete_company.html"
    convert_to_html_content = render_to_string(template_name, context)
    plain_message = strip_tags(convert_to_html_content)

    email_sent = send_mail(
        subject="Receiver information from a form",
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email, ],
        html_message=convert_to_html_content,
        fail_silently=False
    )


    return email_sent


