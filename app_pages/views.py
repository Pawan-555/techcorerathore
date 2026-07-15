from django.shortcuts import render,redirect
from django.contrib import messages
from app_pages.models import ContactInquiry

def home_view(request):
    context = {
        'articles': [
            {'category': 'Cloud', 'comment_count': 5, 'title': "Exceptional Engineering",'paragraph':"They transformed our outdated legacy system into a sleek, cloud-ready software application. Our team's efficiency increased by 40% within the first month of launch. \n\n Sarah M ., CEO of NexaCorp", 'published_date': 'June 11, 2026'},
            {'category': 'AI', 'comment_count': 12, 'title': 'Phenomenal Automation','paragraph':"Integrating their generative AI models completely transformed our deployment pipeline. What used to take our DevOps team hours is now fully automated and error-free. \n\n David L.Head of DevOps at CloudStream", 'published_date': 'June 10, 2026'},
        ],
        'faqs': [
            {'number': 1, 'question': 'What core architectural and development services do you provide?', 'answer': 'We specialize in cloud infrastructure engineering, custom enterprise software development, and end-to-end digital transformation consulting designed to scale your business.'},
            {'number': 2, 'question': 'How can we initiate a project discovery or schedule a consultation?', 'answer': 'You can connect directly with our engineering team by filling out the brief briefing form below, and we will get back to you within one business day to map out your solution.'},
        ]
    }
    return render(request, 'home.html', context)

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        project_details = request.POST.get('details')

        ContactInquiry.objects.create(
            full_name=name,
            email=email,
            project_briefing=project_details
        )
        
        print("--- New Lead Received ---")
        print(f"Name/Company: {name}")
        print(f"Email: {email}")
        print(f"Project Scope: {project_details}")
        print("-------------------------")

        messages.success(request, "Your briefing details have been sent successfully!")
        return redirect('contact_page')  # या जहां भी आप रीडायरेक्ट करना चाहें
        return redirect('home') 
    
        
    return render(request, 'contact.html')