from django.contrib import admin
from server.models import TrashStats, TrashPlace, Campus

# Register your models here.
admin.site.register(TrashPlace)
admin.site.register(TrashStats)
admin.site.register(Campus)
