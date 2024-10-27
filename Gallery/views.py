from django.shortcuts import render , redirect
from django.contrib import messages
from core.forms import FormComment

def Gallery(request):
    Form = FormComment()


    if request.method == "POST":
        Form = FormComment(data = request.POST)
        if Form.is_valid():
            Form.save()
            messages.add_message(request,messages.SUCCESS,"Your form is accepted.")
            return redirect("Gallary:Gallary_Page")
        else:
            messages.add_message(request,messages.ERROR,"Your form isn't accepted")
        
        
    context = {
        "Form":Form,
    }

    return render(request,"Gallary.html",context = context)

