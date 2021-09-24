from django.contrib import admin

# Register your models here.
from api.models import Person, Office, Company, Partnership, Skill, Language, JobPlace

admin.site.register(Person)
admin.site.register(Office)
admin.site.register(Company)
admin.site.register(Partnership)
admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(JobPlace)
