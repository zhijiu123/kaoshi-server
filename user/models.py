from django.contrib.auth.models import AbstractUser, User
from django.db import models


class College(models.Model):
    college_name = models.CharField("学院名称", max_length=20)

    class Meta:
        ordering = ['id']
        verbose_name = "学院管理"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.college_name
    
class Major(models.Model):
    college_name = models.ForeignKey(College, verbose_name="所属学院", on_delete=models.CASCADE)
    major_name = models.CharField("专业名称", max_length=20)

    class Meta:
        ordering = ['id']
        verbose_name = "专业管理"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.major_name

# Create your models here.
class Clazz(models.Model):
    """班级"""
    year = models.CharField("年级", max_length=20)
    major = models.ForeignKey(Major, verbose_name="所属专业", on_delete=models.CASCADE)
    clazz = models.CharField("班级", max_length=20)

    class Meta:
        ordering = ['id']
        verbose_name = "班级管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.year}{self.major.major_name}{self.clazz}"



class Student(models.Model):
    """学生模型类"""
    GENDER_CHOICES = (
        ('m', '男'),
        ('f', '女')
    )
    college = models.ForeignKey(College, verbose_name="所属学院", on_delete=models.CASCADE)
    major = models.ForeignKey(Major, verbose_name="所属专业", on_delete=models.CASCADE)
    name = models.CharField("姓名", max_length=20, default="")
    user = models.OneToOneField(User, verbose_name="学号", on_delete=models.CASCADE)
    gender = models.CharField("性别", max_length=1, choices=GENDER_CHOICES, default="")
    clazz = models.ForeignKey(Clazz, verbose_name="班级", on_delete=models.CASCADE, default="1")


    class Meta:
        ordering = ['id']
        db_table = 'user_student'
        verbose_name = '学生管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    "教师模型类"
    GENDER_CHOICES = (
        ('男', '男'),
        ('女', '女')
    )
    TITLE_CHOICES = (
        ('讲师', '讲师'),
        ('副教授', '副教授'),
        ('教授', '教授')
    )
    name = models.CharField("姓名", max_length=20, default="")
    gender = models.CharField("性别", max_length=1, choices=GENDER_CHOICES, default="男")
    title = models.CharField("职称", max_length=5, choices=TITLE_CHOICES, default="讲师")
    institute = models.ForeignKey(College, verbose_name="所属学院", on_delete=models.CASCADE)
    telmobile = models.CharField("联系方式", max_length=11, default="")

    # 一对一关联字段
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="工号")

    class Meta:
        ordering = ['id']
        db_table = 'user_teacher'
        verbose_name = '教师管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
