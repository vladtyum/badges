from django.contrib import admin
from . models import Student, School, Topic, Skill, Badge,  Achievement, Evidence

# Register your models here.
admin.site.register(School)
admin.site.register(Topic)
admin.site.register(Skill)

class BadgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'skill', 'topic', 'school')

    def topic(self, obj):
        return obj.skill.topic

    def school(self, obj):
        return obj.skill.topic.school

class EvidenceInLine(admin.TabularInline):
    model = Evidence
    extra = 1

class AchvAdmin(admin.ModelAdmin):
    inlines = (EvidenceInLine,)
    list_display = ('id', 'student', 'badge',  'date', )


class AchvInLine(admin.TabularInline):
    model = Achievement
    extra = 1


class StudentAdmin(admin.ModelAdmin):
    inlines = (AchvInLine,)

admin.site.register(Badge, BadgeAdmin)
admin.site.register(Achievement, AchvAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Evidence)

