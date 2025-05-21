from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import comment,CustomUser,classes,subject,publication,unit,unit1,exam1,exam,type12,major12

@admin.register(comment) 
class usercomment(admin.ModelAdmin):  
    list_display = ['name','email', 'message','uploaded']

@admin.register(CustomUser) 
class usercustomuser(admin.ModelAdmin):  
    list_display = [field.name for field in CustomUser._meta.get_fields() if not field.many_to_many and not field.is_relation]

@admin.register(unit) 
class unit(admin.ModelAdmin):
    list_display = ['class1','sub', 'pub','major','unit_num','unit_pdf']

@admin.register(classes) 
class classes(admin.ModelAdmin):
    list_display = ['num','type']

@admin.register(subject) 
class subject(admin.ModelAdmin):
    list_display = ['sub_name','type','class1','sub_full','major']

@admin.register(publication) 
class publication(admin.ModelAdmin):
    list_display = ['pub_name','type','major']

@admin.register(unit1) 
class unit1(admin.ModelAdmin):
    list_display = ['name']

@admin.register(exam1) 
class exam1(admin.ModelAdmin):
    list_display = ['term']

@admin.register(exam) 
class exam(admin.ModelAdmin):
    list_display = ['ter','class1','sub','major','pdf','scl']

@admin.register(type12) 
class type123(admin.ModelAdmin):
    list_display = ['num']

@admin.register(major12) 
class major12(admin.ModelAdmin):
    list_display = ['sub','type']



