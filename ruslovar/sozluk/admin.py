from django.contrib import admin
from .models import Sozcukler, Diller, Sesler

class VeriYonetim(admin.ModelAdmin):
    list_display = ("sozcuk","koken","anlam","karsilik",)
    list_editable = ("anlam",)
    search_fields = ("sozcuk",)
    list_filter = ("dil", "ses",)
    readonly_fields = ("slug",)

admin.site.register(Sozcukler, VeriYonetim)
admin.site.register(Diller)
admin.site.register(Sesler)