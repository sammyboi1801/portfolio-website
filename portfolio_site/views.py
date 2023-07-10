from django.shortcuts import render, redirect
from .utils import send_email_from_client, send_email_to_client
from email_validator import validate_email, EmailNotValidError

def check(email):
    try:
      # validate and get info
        v = validate_email(email)
        # replace with normalized form
        email = v["email"]
        return True
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        return str(e)

# Create your views here.
def home(request):
    rmsg1 = ""
    rmsg2 = ""
    if request.method == 'POST':
        if 'emailcv' in request.POST:
            email = request.POST['emailcv']
            echeck = check(str(email))
            if echeck!=True:
                rmsg1 = echeck
            else:
                send_email_to_client(str(email))
                rmsg1 = "Message sent:)"
        elif 'email' in request.POST:
            mail = request.POST['email']
            message = request.POST['message']
            echeck = check(str(mail))
            if echeck != True:
                rmsg2 = echeck
            else:
                rmsg2 = "Message sent:)"
                send_email_from_client(mail,message)

    # request.POST =None
    # render function takes argument - request
    # and return HTML as response
    return render(request, "home.html",{'rmsg1' : rmsg1, 'rmsg2' : rmsg2})
