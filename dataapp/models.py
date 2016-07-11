from django.db import models


# Create your models here.
class DdepartmentInfo(models.Model):
    department_id=models.CharField(primary_key = True,max_length = 30)
    department_name=models.CharField(max_length = 30)

    def __str__(self):
        return self.department_name


class ClassInfo(models.Model):
    class_id=models.CharField(primary_key = True,max_length = 30)
    department_id=models.ForeignKey(DdepartmentInfo)

    def __str__(self):
        return self.class_id


class StudentInfo(models.Model):
    student_id = models.CharField(primary_key = True, max_length = 30)
    student_name = models.CharField(max_length = 30)
    class_id = models.ForeignKey(ClassInfo)
    sex = models.CharField(max_length = 10)
    major = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30, default = 0)

    def __str__(self):
        return self.student_id


class TeacherInfo(models.Model):
    teacher_id = models.CharField(primary_key = True, max_length = 30)
    teacher_name = models.CharField(max_length = 30)
    department_id=models.ForeignKey(DdepartmentInfo)
    sex = models.CharField(max_length = 10)
    profession = models.CharField(max_length = 30)
    telephone = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30, default = 0)

    def __str__(self):
        return self.teacher_id


class CourseInfo(models.Model):
    course_id = models.CharField(primary_key = True, max_length = 30)  # 课程编号
    course_name = models.CharField(max_length = 30)  # 课程名称
    total_perior = models.IntegerField()  # 学时
    credit = models.IntegerField()  # 学分

    def __str__(self):
        return self.course_name


class StudentCourse(models.Model):
    course_id = models.ForeignKey(CourseInfo)
    student_id = models.ForeignKey(StudentInfo)
    teacher_id = models.ForeignKey(TeacherInfo)
    grade = models.IntegerField()
    credit = models.IntegerField()

    def __str__(self):
        return self.student_id.student_id


class TeacherCourse(models.Model):
    teacher_id = models.ForeignKey(TeacherInfo)
    course_id = models.ForeignKey(CourseInfo)
