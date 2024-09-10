from django.shortcuts import render, redirect,get_object_or_404
from home.models import Add_Contact
# Create your views here.
def index(request):
    contacts = Add_Contact.objects.all()
    return render(request,'index.html',{'contacts':contacts})

def addContact(request):
    if request.method == "POST":
        name = request.POST.get("name").capitalize()
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        newContact = Add_Contact(name=name, email=email, phone=phone)
        newContact.save()
    
    return render(request,'addContact.html')

def searchContact(request):
    query = request.GET.get('query','')
    cap_query = query.capitalize()
    result = Add_Contact.objects.filter(name = cap_query)
    return render(request,'searchContact.html',{'result':result})


def updateContact(request, contact_id):
    contact = get_object_or_404(Add_Contact, id=contact_id)
    if request.method == "POST":

        contact.name = request.POST.get("name")
        contact.email = request.POST.get("email")
        contact.phone = request.POST.get("phone")
        contact.save()
        # for going to back index page aftr updating
        return redirect('index')
    
    return render(request, 'updateContact.html', {'contact': contact})

def deleteContact(request, contact_id):
    contact = get_object_or_404(Add_Contact, id=contact_id)
    contact.delete()
    return redirect('index')
