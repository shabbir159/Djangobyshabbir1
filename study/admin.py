from django.contrib import admin
from .models import chapter
from .models import topic
from .models import sub_topic

# Register your models here.
admin.site.register(chapter)
admin.site.register(topic)
admin.site.register(sub_topic)