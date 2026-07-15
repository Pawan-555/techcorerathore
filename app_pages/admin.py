from django.contrib import admin

# Register your models here.
from .models import ContactInquiry

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'created_at')  # Admin dashboard पर जो कॉलम्स आपको दिखने चाहिए
    search_fields = ('full_name', 'email')