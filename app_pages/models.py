from django.db import models

# 1. Consultation Request Model
class ConsultationRequest(models.Model):
    SERVICE_CHOICES = [
        ('cloud', 'Cloud Infrastructure'),
        ('dev', 'Custom Development'),
        ('cyber', 'Cybersecurity'),
        ('disaster', 'Disaster Recovery'),
    ]
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.service}"

# 2. Blog/Insights Model
class BlogArticle(models.Model):
    category = models.CharField(max_length=50, default="Tech")
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField()
    comment_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

# 3. FAQ Model
class FAQ(models.Model):
    number = models.CharField(max_length=5)
    question = models.CharField(max_length=250)
    answer = models.TextField()

    def __str__(self):
        return self.question