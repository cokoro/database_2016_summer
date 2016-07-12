# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from dataapp.models import StudentInfo, CourseInfo, TeacherInfo, StudentCourse, TeacherCourse
from django.db.models import Count, Max, Avg


# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def login_action(request):
    username = ""
    password = ""
    login_type = ""

    if request.POST.get("username"):
        username = request.POST["username"]

    if request.POST.get("password"):
        password = request.POST["password"]

    if request.POST.get("login_type"):
        login_type = request.POST["login_type"]

    mention = "用户名或密码不正确"
    if login_type == '0':  # 学生
        try:
            stu = StudentInfo.objects.get(student_id = username)
        except StudentInfo.DoesNotExist:
            return render(request, 'login.html', {'mention': mention})

        if stu.password == password:
            return render(request, 'student.html', {'stu': stu})
        else:
            return render(request, 'login.html', {'mention': mention})

    elif login_type == '1':  # 老师
        try:
            tea = TeacherInfo.objects.get(teacher_id = username)
        except TeacherInfo.DoesNotExist:
            return render(request, 'login.html', {'mention': mention})

        if tea.password == password:
            return render(request, 'teacher.html', {'tea': tea})

        else:
            return render(request, 'login.html', {'mention': mention})
    else:
        mention = "请选择用户类型"
        return render(request, 'login.html', {'mention': mention})


def get_student_info(request, stu_id):
    stu = StudentInfo.objects.get(student_id = stu_id)
    return render(request, 'student_info.html', {"stu": stu})


def get_grade(request, stu_id):
    student = None
    try:
        student = StudentInfo.objects.get(student_id = stu_id)
    except:
        return None, None
    course_set = StudentCourse.objects.filter(student_id = stu_id)
    for cs in course_set:  # 获取课程
        course = CourseInfo.objects.get(course_id = cs.course_id.course_id)
        cs.course_name = course.course_name
        cs.course_credit = course.credit

    return course_set, student


def get_student_grade(request, stu_id):
    course_set, student = get_grade(request, stu_id)
    return render(request, 'student_grade.html', {'courseSet': course_set, 'student': student})


def get_teacher_info(request, teacher_id):
    tea = TeacherInfo.objects.get(teacher_id = teacher_id)
    return render(request, 'teacher_info.html', {'tea': tea})


def input_student_id(request, teacher_id):
    return render(request, 'input_student_id.html', {'teacher_id': teacher_id})


def get_student_grade_by_teacher(request, teacher_id):
    student_id = None
    if request.POST.get("student_id"):
        student_id = request.POST["student_id"]
    print(student_id)
    if (student_id):
        try:
            exist = StudentInfo.objects.get(student_id = student_id)
        except:
            mention = "该学生不存在！"
            return render(request, 'input_student_id.html', {'teacher_id': teacher_id, 'mention': mention})
        course_set = None
        course_set, student = get_grade(request, student_id)
        if (course_set):
            return render(request, 'student_grade_by_teacher.html', {'stu': student, 'courseSet': course_set})
        else:
            mention = "该学生成绩未录入！"
            return render(request, 'input_student_id.html', {'teacher_id': teacher_id, 'mention': mention})
    else:
        mention = "学生学号不能为空"
        return render(request, 'input_student_id.html', {'teacher_id': teacher_id, 'mention': mention})


def get_all_grades_by_teacher(request, teacher_id):
    students = StudentInfo.objects.all().order_by('student_id')
    result = []
    for student in students:
        print(student)
        if StudentCourse.objects.filter(student_id = student.student_id):
            result.append(StudentCourse.objects.filter(student_id = student.student_id))
            print(result)
            course = CourseInfo.objects.get(course_id = result[-1][0].course_id.course_id)
    print(result)
    #print(course)
    return render(request, 'all_grades_by_teacher.html', {'grades': result})


def input_student_new_password(request,stu_id):
    return render(request,'input_student_new_password.html',{"stu_id":stu_id})


def modify_password_student(request, stu_id):
    old_pass=None
    new_pass=None
    confrim_pass=None

    if request.POST.get("old_pass"):
        old_pass = request.POST["old_pass"]
    if request.POST.get("new_pass"):
        new_pass = request.POST["new_pass"]
    if request.POST.get("confrim_pass"):
        confrim_pass = request.POST["confrim_pass"]

    student = StudentInfo.objects.get(student_id = stu_id)
    if (student.password != old_pass):
        mention = "原密码错误"
        return render(request, "input_student_new_password.html", {"stu_id": stu_id, "mention": mention})

    if (new_pass != confrim_pass):
        mention = "两次输入的密码不一致"
        return render(request, "input_student_new_password.html", {"stu_id": stu_id, "mention": mention})

    student.password = new_pass
    student.save()
    mention = "修改成功"
    return render(request, "input_student_new_password.html", {"stu_id": stu_id, "mention": mention})


def student_home(request,stu_id):
    stu=StudentInfo.objects.get(student_id=stu_id)
    return render(request, 'student.html', {'stu': stu})


def input_new_password(request,teacher_id):
    return render(request,'input_new_password.html',{"teacher_id":teacher_id})


def modify_password_teacher(request, teacher_id):
    old_pass=None
    new_pass=None
    confrim_pass=None

    if request.POST.get("old_pass"):
        old_pass = request.POST["old_pass"]
    if request.POST.get("new_pass"):
        new_pass = request.POST["new_pass"]
    if request.POST.get("confrim_pass"):
        confrim_pass = request.POST["confrim_pass"]
    teacher = TeacherInfo.objects.get(teacher_id = teacher_id)

    if (teacher.password != old_pass):
        mention="原密码错误"
        return render(request,"input_new_password.html",{"teacher_id":teacher_id,"mention":mention})

    if (new_pass != confrim_pass):
        mention = "两次输入的密码不一致"
        return render(request, "input_new_password.html", {"teacher_id": teacher_id, "mention": mention})

    teacher.password = new_pass
    teacher.save()
    mention = "修改成功"
    return render(request, "input_new_password.html", {"teacher_id": teacher_id, "mention": mention})


def teacher_home(request,teacher_id):
    tea=TeacherInfo.objects.get(teacher_id=teacher_id)
    return render(request, 'teacher.html', {'tea': tea})


def insert_grade_front(request,teacher_id):
    student_set=StudentInfo.objects.all()
    course_set=CourseInfo.objects.all()
    return render(request,"insert_grade_front.html",{"teacher_id" : teacher_id,"student_set":student_set,"course_set":course_set})

def insert_grade(request, teacher_id):
    print(teacher_id)
    student_id=None
    course_name=None
    grade=None
    if request.POST.get("student_id"):
        student_id=request.POST["student_id"]
        print(student_id)
    if request.POST.get("course_name"):
        course_name=request.POST["course_name"]
        print(course_name)
    if request.POST.get("grade"):
        grade = request.POST["grade"]
    print(grade)
    if (student_id == None):
        return HttpResponse('学号不能为空')
    if (course_name == None):
        return HttpResponse('课程名不能为空')
    if (grade == None):
        return HttpResponse("成绩不能为空")

    student = StudentInfo.objects.get(student_id = student_id)
    course = CourseInfo.objects.get(course_name = course_name)
    teacher=TeacherInfo.objects.get(teacher_id=teacher_id)
    #print(course.course_id,course_name)
    #print(student)
    info = TeacherCourse.objects.get(course_id = course.course_id)
    #print(info.teacher_id)
    #print(teacher_id)
    if (student == None):
        return HttpResponse('该学生不存在')
    if (str(teacher_id) != str(info.teacher_id)):
        return HttpResponse('您无此权限')

    try:
        grade = int(grade)
    except ValueError:
        return HttpResponse('输入的成绩不合法')

    try:
        #print(student)
        record = StudentCourse.objects.get(student_id = student, course_id = course)
        #print(record)
        record.grade = grade
        record.save()
        return HttpResponse('更新成功')
    except:
        record = StudentCourse(student_id = student, course_id = course, teacher_id = teacher,
                               grade = grade, credit = course.credit)
        record.save()
        return HttpResponse('插入成功')


def find_average_by_courseName(request,teacher_id):
    result={}#最后未使用到
    courses = CourseInfo.objects.all()
    for course in courses:
        result[course.course_name] = StudentCourse.objects.filter(course_id = course.course_id).aggregate(Avg('grade'))
        course.average=StudentCourse.objects.filter(course_id = course.course_id).aggregate(Avg('grade'))['grade__avg']
        #print(course.average)
        #print(result[course.course_name]['grade__avg'])
    #print(courses)
    return render(request,"find_average_by_courseName.html",{"result":result,"teacher_id":teacher_id,"courses":courses})



def find_grade_distribution(request,teacher_id):
    cour_name = None
    if request.POST.get("cour_name"):
        cour_name = request.POST["cour_name"]

    course = CourseInfo.objects.get(course_name = cour_name)
    grades = StudentCourse.objects.filter(course_id = course.course_id)
    result = {}  #未使用，在html中使用字典额方法未掌握
    result['less_60_'] = grades.filter(grade__lt = 60).count()
    course.less_60_=grades.filter(grade__lt = 60).count()
    result['from_60_to_70_'] = grades.filter(grade__gt = 60, grade__lt = 70).count()
    course.from_60_to_70_=grades.filter(grade__gt = 60, grade__lt = 70).count()
    result['from_70_to_80_'] = grades.filter(grade__gt = 70, grade__lt = 80).count()
    course.from_70_to_80_=grades.filter(grade__gt = 70, grade__lt = 80).count()
    result['from_80_to_90_'] = grades.filter(grade__gt = 80, grade__lt = 90).count()
    course.from_80_to_90_=grades.filter(grade__gt = 80, grade__lt = 90).count()
    result['more_90_'] = grades.filter(grade__gt = 90).count()
    course.more_90_=grades.filter(grade__gt = 90).count()
    #print(result)
    #print(course.from_60_to_70_)
    return render(request,"show_course_distribute_graph.html",{"result":result,"course":course,"teacher_id":teacher_id})


def choose_course(request,teacher_id):
    course_set=CourseInfo.objects.all()
    return render(request,"choose_class_to_get_graph.html",{"teacher_id":teacher_id,"course_set":course_set})


