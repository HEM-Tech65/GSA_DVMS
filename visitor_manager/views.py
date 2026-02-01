from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import VisitorLog
from .firebase_config import save_visitor_to_cloud
from django.utils import timezone

def visitor_checkin(request):
    if request.method == "POST":
        name = request.POST.get('visitor_name').strip()
        host = request.POST.get('host_name').strip()
        
        # 1. Validation and Sanitization (Cyber Security Step) 
        if not name or not host:
            return render(request, 'checkin.html', {'error': 'Required fields missing'})

        # 2. Local Database Save
        log = VisitorLog.objects.create(visitor_name=name, host_name=host)

        # 3. Cloud Database Sync (Firestore) 
        save_visitor_to_cloud({
            "name": name,
            "host": host,
            "time_in": str(timezone.now()),
            "status": "signed_in"
        })

        return render(request, 'success.html', {'name': name})
    
    return render(request, 'checkin.html')