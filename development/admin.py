from django.contrib import admin

from .models import *


admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Developer)
admin.site.register(Subscription)
admin.site.register(Stage)
admin.site.register(SubStage)
admin.site.register(StageUpdate)
