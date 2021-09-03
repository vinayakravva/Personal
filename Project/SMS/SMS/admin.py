from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Staffs)
admin.site.register(CustomUser)
# admin.site.register(AdminHOD)
admin.site.register(SessionYearModel)
admin.site.register(Staffs)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Students)
admin.site.register(AttendanceReport)
# admin.site.register(LeaveReportStaff)
admin.site.register(LeaveReportStudent)
# admin.site.register(FeedBackStaffs)
# admin.site.register(FeedBackStudent)
admin.site.register(StudentResult)
admin.site.register(NotificationStudent)





