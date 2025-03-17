import os
import pytz
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
import subprocess

def htop(request):
    full_name = "Vangala Rajendhar Reddy"
    username = os.getenv("USER") or os.getenv("USERNAME")
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Changed 'top' to 'tasklist' for Windows compatibility
        top_output = subprocess.check_output("tasklist", shell=True).decode('utf-8')
    except Exception as e:
        top_output = str(e)
        
    response = f"""
    Name: {full_name}<br>
    Username: {username}<br>
    Server Time (IST): {ist_time}<br>
    <pre>{top_output}</pre>
    """
    
    return HttpResponse(response)
