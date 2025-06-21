from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def about(request):
    return render(request, 'users/about.html')

def projects(request):
    return render(request, 'users/projects.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # You can add logic to store or email this data
        messages.success(request, "Your message has been sent successfully!")
        return redirect('home')  # ✅ Redirect to home after message
    return render(request, 'users/contact.html')  

def about(request):
    frontend_skills = [
        ('HTML', 95, 'bg-blue-600'),
        ('CSS', 90, 'bg-blue-500'),
        ('JavaScript', 70, 'bg-yellow-500'),
        ('Bootstrap', 75, 'bg-purple-600'),
        ('Tailwind CSS', 75, 'bg-cyan-500'),
        ('Flutter', 70, 'bg-indigo-500')
    ]

    backend_skills = [
        ('Python', 95, 'bg-green-600'),
        ('Django', 80, 'bg-green-400'),
        ('Node.js', 75, 'bg-lime-500'),
        ('VB.NET', 70, 'bg-red-500')
    ]

    db_skills = [
        ('SQL', 90, 'bg-pink-500'),
        ('MySQL', 90, 'bg-pink-400')
    ]

    tools = [
        'Git & GitHub',
        'Visual Studio & VS Code',
        'Postman',
        'REST APIs',
        'JSON'
    ]

    projects = [
        ('2025', 'Portfolio Website', 'Built a modern responsive portfolio site using Django, Tailwind CSS, and MySQL with dynamic backend integration and animation support.'),
        ('2024', 'Flutter Auth App', 'Developed a full-stack mobile login/signup app using Flutter, Node.js, and MySQL featuring OTP-based authentication.'),
        ('2023', 'VB.NET ERP Module', 'Designed and implemented modules in VB.NET for enterprise resource planning software with SQL database integration.')
    ]

    return render(request, 'users/about.html', {
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills,
        'db_skills': db_skills,
        'tools': tools,
        'projects': projects,
    })

