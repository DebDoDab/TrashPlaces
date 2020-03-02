from django.contrib import admin
from server.models import TrashStats, TrashPlace, Campus, OwnPermission, CampusStats


admin.site.register(TrashPlace)
admin.site.register(TrashStats)
admin.site.register(OwnPermission)
admin.site.register(CampusStats)
admin.site.register(Campus)
