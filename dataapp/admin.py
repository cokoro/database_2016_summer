from django.contrib import admin

# Register your models here.
from dataapp.models import StudentInfo, CourseInfo, TeacherInfo, StudentCourse,TeacherCourse,DdepartmentInfo,ClassInfo

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_id','department_name',)


class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_id','department_id')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'student_name', 'class_id', 'sex', 'major',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'teacher_name', 'sex', 'profession', 'telephone','department_id',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name', 'total_perior', 'credit',)



class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'course_id', 'grade','credit','teacher_id',)

class TeacherCourseAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'course_id',)

admin.site.register(StudentInfo, StudentAdmin)
admin.site.register(TeacherInfo, TeacherAdmin)
admin.site.register(CourseInfo, CourseAdmin)
admin.site.register(TeacherCourse, TeacherCourseAdmin)
admin.site.register(StudentCourse, StudentCourseAdmin)
admin.site.register(DdepartmentInfo,DepartmentAdmin)
admin.site.register(ClassInfo,ClassAdmin)
