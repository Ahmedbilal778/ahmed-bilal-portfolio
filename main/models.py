from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Project(models.Model):
    name = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=300)

    github_link = models.URLField(blank=True)
    live_demo_link = models.URLField(blank=True)

    image = models.ImageField(upload_to="projects/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    issue_date = models.CharField(max_length=50, blank=True)
    image = models.ImageField(
        upload_to="certificates/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title   