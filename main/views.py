from django.shortcuts import render
from django.http import HttpResponse

# 1. Басты бет
def home(request):
    return render(request, 'home.html')

# 2. About
def about(request):
    return render(request, 'about.html')

# 3. Dynamic project
def project_detail(request, project_id):
    if project_id == 1:
        title = "Жоба 1"
        description = "Бұл бірінші жоба туралы ақпарат"
    elif project_id == 2:
        title = "Жоба 2"
        description = "Бұл екінші жоба туралы ақпарат"
    else:
        title = f"Жоба {project_id}"
        description = "Белгісіз жоба"

    return render(request, 'project.html', {
    'title': title,
    'description': description,
    'id': project_id
})

# 4. Info page
def info(request):
    ip = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT')

    return HttpResponse(f"""
    <h2>Пайдаланушы туралы ақпарат</h2>
    <p><b>IP:</b> {ip}</p>
    <p><b>Browser:</b> {user_agent}</p>
    """)