from django.shortcuts import render, redirect
from django.contrib import messages

from .models import ContactMessage, Project, Certificate


def home(request):

    # Contact Form
    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save message to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Success message
        messages.success(
            request,
            "Your message has been sent successfully!"
        )

        return redirect("home")

    # Get projects from database
    projects = Project.objects.all().order_by("-created_at")

    # Get certificates from database
    certificates = Certificate.objects.all().order_by("-id")

    context = {
        "projects": projects,
        "certificates": certificates,
    }

    return render(request, "main/home.html", context)