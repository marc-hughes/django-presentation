from demoapp.models import InterestingPerson
from django.contrib import admin

class InterestingPersonAdmin(admin.ModelAdmin):
    fields = ( ('name','twitter_username'),'follow_count','picture_url')
    list_display = ( 'name','twitter_username','follow_count')
    search_fields = ( 'name','twitter_username')
    
    
admin.site.register(InterestingPerson, InterestingPersonAdmin)
