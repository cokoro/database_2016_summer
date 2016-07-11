"""database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from dataapp import views

urlpatterns = [
    url(r'^admin/',admin.site.urls, name='admin'),
    url(r'^login/$', views.login, name='login'),  # 将主url与应用中的url关联起来
    url(r'^login/ActionLogin/', views.login_action, name='login_action'),  # 跳转到指定界面界面

    url(r'^studentHome/(?P<stu_id>[0-9]+)/$',views.student_home,name="student_home"), #返回老师首页
    url(r'^studentInfo/(?P<stu_id>[0-9]+)/$',views.get_student_info,name='get_student_info'), #学生信息显示
    url(r'^studentGrade/(?P<stu_id>[0-9]+)/$',views.get_student_grade,name='get_student_grade'), #学生自己的成绩显示
    url(r'^studentInsertAction/(?P<stu_id>[0-9]+)/$',views.modify_password_student,name="modify_password_student"),#处理密码修改请求
    url(r'^insertStudentNewPassword/(?P<stu_id>[0-9]+)/$',views.input_student_new_password,name="input_student_new_password"), #学生修改密码

    #url(r'^teacherChooseSearchType/(?P<stu_id>[0-9]+)/$',views.teacher_choose_grade_search_type,name = 'teacher_choose_grade_search_type'), #选择查询方式
    url(r'^teacherHome/(?P<teacher_id>[0-9]+)/$',views.teacher_home,name="teacher_home"), #返回老师首页
    url(r'^teacherInfo/(?P<teacher_id>[0-9]+)/$', views.get_teacher_info, name = 'get_teacher_info'),  # 显示教师基本信息
    url(r'^inputStudentId/(?P<teacher_id>[0-9]+)/$',views.input_student_id,name="input_student_id"),#输入学生学号信息查找学生成绩
    url(r'^gradeByTeacher/(?P<teacher_id>[0-9]+)/$', views.get_student_grade_by_teacher, name = 'get_student_grade_by_teacher'),#显示学生成绩
    url(r'^allGradesByTeacher/(?P<teacher_id>[0-9]+)/$', views.get_all_grades_by_teacher, name = 'get_all_grades_by_teacher'),#显示所有学生成绩
    url(r'^insertOrmodifyGrade/(?P<teacher_id>[0-9]+)/$',views.insert_grade_front,name="insert_grade_front"), #录入学生成绩
    url(r'^insertOrmodifyGradeaction/(?P<teacher_id>[0-9]+)/$',views.insert_grade,name="insert_grade_action"), #录入学生成绩
    url(r'^insertNewPassword/(?P<teacher_id>[0-9]+)/$',views.input_new_password,name="input_new_password"),#老师输入修改密码
    url(r'^insertAction/(?P<teacher_id>[0-9]+)/$',views.modify_password_teacher,name="modify_password_teacher"),#处理密码修改请求
    url(r'^chooseClassToGetGradeGraph/(?P<teacher_id>[0-9]+)/$',views.choose_course,name="choose_class"),#选择课程编号获得课程统计图
    url(r'^getGradeGraph/(?P<teacher_id>[0-9]+)/$',views.find_grade_distribution,name="find_grade_distribution"),#生成各科统计图
    url(r'^find_average_by_courseName/(?P<teacher_id>[0-9]+)/$',views.find_average_by_courseName,name="find_average_by_courseName"),#各科平均成绩比较

    #url(r'^teaCheckGrade/')
    url(r'^$', views.home, name='home'),  # 选择登陆或进行后台管理


]
