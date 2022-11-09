from django.shortcuts import render,redirect
from django.db.models import Q
# Create your views here.
from .models import Experience
from django.contrib.auth.decorators import login_required
# from django.core.mail import EmailMessgae
from django.conf import settings
from django.template.loader import render_to_string 

def index(request):
    return render(request, 'base/index.html')

@login_required
def create_experience(request):
    user = request.user
    if request.method == 'POST':
        user = user
        post= request.POST['post']
        company = request.POST['company']
        content = request.POST['content']
        dur = request.POST['dur']
        experience = Experience.objects.create(user=user, post=post,company=company, content= content, duration=dur, is_approved = False)
        
        template = render_to_string('base/email.html' , {'experience':experience})
    #     email = EmailMessage(
    #     'Confirm experience',
    #     template,
    #     settings.EMAIL_HOST_USER,
    #     ['vedu8051@gmail.com'],
    # )

    # email.fail.silently = False
    # email.send()
        experience.save()
        return redirect('experiences')
    
    context={


    }
    return render(request, 'base/create-experience.html',context)
    # 
@login_required
def experiences(request):
    
    experiences = Experience.objects.all()
    companies = Experience.objects.values_list('company', flat=True ).distinct().order_by()
    posts = Experience.objects.values_list('post', flat=True ).distinct().order_by()
    durations = Experience.objects.values_list('duration', flat=True).distinct().order_by() 
    
   
   
    if request.method=='POST':
       
        company = request.POST['company'] if request.POST['company'] != 'All' else ''
        post = request.POST['post'] if request.POST['post'] != 'All' else ''
        duration = request.POST['duration'] if request.POST['duration'] != 'All' else ''
        experiences = Experience.objects.filter(Q(company__icontains = company) & Q(post__icontains= post) & Q(duration__icontains = duration))

        
    else:
        q=request.GET.get('q') if request.GET.get('q') != None else ''
        experiences = Experience.objects.filter(
            Q(company__icontains = q ) |
            Q(content__icontains = q)  |
            Q(duration__icontains = q) |
            Q(post__icontains = q)  
            )
    

    context = {
        'experiences' : experiences,
        'companies': companies,
        'posts':posts,
        'durations': durations,

    }

    
    return render (request, 'base/experiences.html', context)

def experienceDetail(request, pk):
    experience = Experience.objects.get(pk =pk)
    context ={
        'experience':experience

    }
    return render(request, 'base/detail.html', context)


    

    






