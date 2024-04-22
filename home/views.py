from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from django.core.paginator import Paginator
from home.forms import ContactForm
from home.models import Events, Products, FAQ, newsBlog
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request,'landing_pages/index.html',{})

def aboutus(request):
    return render(request,'landing_pages/about.html',{})

def contactus(request):
    faqdata = FAQ.objects.all()  

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            message_phone_number = form.cleaned_data['contact_Number']
            message_email = form.cleaned_data['email']
            message_message = form.cleaned_data['message']
            
            try:
                send_mail(
                f"Message from: {name}",
                f"{message_message}\nPhone number: {message_phone_number}\nEmail: {message_email}",
                message_email,
                ['grgjeny619@gmail.com'],
                fail_silently=False)
                return JsonResponse({'success': True})

                
            except Exception as e:
                # Handle the exception if the email fails to send
                print(f"Error sending email: {e}")
                return JsonResponse({'success': False, 'errors':e})

        else:
            print(f"Error sending email: {form.errors}")

            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ContactForm()
        
    return render(request, 'landing_pages/contact.html', {'form': form, 'faqs': faqdata})


def events(request):
    today = timezone.now().date()
    eventsdata = Events.objects.filter(Event_End_Date__gte=today)
    return render(request, 'events/event.html', {'data': eventsdata})


def eventsdetails(request,Events_id):
    eventsdata=get_object_or_404(Events,pk=Events_id)
    return render(request,"events/event-details.html",{'event':eventsdata})


def explore(request):
    p=Paginator(Products.objects.all(),6)
    page=request.GET.get('page')
    Products_List=p.get_page(page)
    nums='a'*Products_List.paginator.num_pages
    return render(request,'explore/explore.html',{'Products_List':Products_List,'nums':nums})

def items(request,Items_id):
    item=get_object_or_404(Products,pk=Items_id)
    return render(request,'explore/details.html',{'item':item})
def blog(request):
    blogsdata=newsBlog.objects.all()
    return render(request,"landing_pages/blog.html",{'data':blogsdata})
def posts(request,Blog_id):
    blogdata= get_object_or_404(newsBlog, pk=Blog_id)
    return render (request,"landing_pages/posts.html",{"posts":blogdata}) 

def login(request):
    return render(request,'login.html',{})




