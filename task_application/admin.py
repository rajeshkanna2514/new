from django.contrib import admin
from .models import User,TaskModel
# Register your models here.
class UserAdmin(admin.ModelAdmin):

    list_display = ('id','username','email','password')

admin.site.register(User)

class TaskAdmin(admin.ModelAdmin):

        list_display = ['task_assigned','taskname','username' ,'description', 'taskstatus', 'createdon', 'updatedon','deadline',"completed_on",'priority']
admin.site.register(TaskModel,TaskAdmin)    


