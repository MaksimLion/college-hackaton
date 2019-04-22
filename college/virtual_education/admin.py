from django.contrib import admin
from .models import Report, Lab

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_filter = ('user', 'group', 'subject')


@admin.register(Lab)
class LabAdmin(admin.ModelAdmin):
    list_filter = ('subject',)

