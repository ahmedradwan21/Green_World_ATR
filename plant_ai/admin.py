from django.contrib import admin
from .models import Inquiry
# Register your models here.
@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']