from django.shortcuts import render,redirect
from django.db.models import Q
# Create your views here.
from .models import Experience
from django.contrib.auth.decorators import login_required


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
        experience = Experience.objects.create(user=user, post=post,company=company, content= content, duration=dur)
        
        experience.save()
        return redirect('experiences')
    
    context={
        

    }
    return render(request, 'base/create-experience.html',context)

@login_required
def experiences(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    experiences = Experience.objects.filter(
        Q(company__icontains = q ) |
        Q(content__icontains = q) |
        Q(duration__icontains = q) |
        Q(post__icontains = q)
        )

    # companies = Experience.objects.only('company')
    context = {
        'experiences' : experiences,
        # 'companies': companies,
    }
    
    return render (request, 'base/experiences.html', context)






