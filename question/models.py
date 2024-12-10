from django.db import models
from user.models import College,Major

# Create your models here.
class Course(models.Model):
    """课程名称"""
    college = models.ForeignKey(College, verbose_name="所属学院", on_delete=models.CASCADE)
    major = models.ForeignKey(Major, verbose_name="所属专业", on_delete=models.CASCADE)
    course = models.CharField("课程名称", max_length=20)

    class Meta:
        ordering = ['id']
        verbose_name = "课程管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course


class Choice(models.Model):
    """选择题模型"""
    LEVEL_CHOICES = (
        ('1', '入门'),
        ('2', '简单'),
        ('3', '普通'),
        ('4', '较难'),
        ('5', '困难')
    )
    ANSWER_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    )
    course = models.ForeignKey(Course, verbose_name="课程名称", on_delete=models.CASCADE, default="")
    question = models.TextField("题目", default="")
    answer_A = models.CharField("A选项", max_length=200, default="")
    answer_B = models.CharField("B选项", max_length=200, default="")
    answer_C = models.CharField("C选项", max_length=200, default="")
    answer_D = models.CharField("D选项", max_length=200, default="")
    right_answer = models.CharField("正确选项", max_length=1, choices=ANSWER_CHOICES, default="A")
    analysis = models.TextField("题目解析", default="暂无")
    score = models.PositiveSmallIntegerField("分值", default=2)
    level = models.CharField("难度等级", max_length=1, choices=LEVEL_CHOICES, default='1')

    class Meta:
        ordering = ['id']
        verbose_name = '选择题管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


class Program(models.Model):
    """多选题模型"""
    LEVEL_CHOICES = (
        ('1', '入门'),
        ('2', '简单'),
        ('3', '普通'),
        ('4', '较难'),
        ('5', '困难')
    )
    ANSWER_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G')
    )
    course = models.ForeignKey('Course', verbose_name="课程名称", on_delete=models.CASCADE)
    question = models.TextField("题目")
    answer_A = models.CharField("A选项", max_length=200)
    answer_B = models.CharField("B选项", max_length=200)
    answer_C = models.CharField("C选项", max_length=200)
    answer_D = models.CharField("D选项", max_length=200)
    answer_E = models.CharField("E选项", max_length=200, blank=True, null=True)
    answer_F = models.CharField("F选项", max_length=200, blank=True, null=True)
    answer_G = models.CharField("G选项", max_length=200, blank=True, null=True)

    # 使用CharField并将多个正确答案存储为逗号分隔的字符串，例如："A,B,C"
    right_answers = models.CharField("正确选项", max_length=50, default="A,B")

    analysis = models.TextField("题目解析", default="暂无")
    score = models.PositiveSmallIntegerField("分值", default=2)
    level = models.CharField("难度等级", max_length=1, choices=LEVEL_CHOICES, default='1')

    class Meta:
        ordering = ['id']
        verbose_name = '多选题管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question

    # 解析正确答案为列表
    def get_right_answers(self):
        return self.right_answers.split(',')

    # 保存正确答案时，确保以逗号分隔的形式存储
    def set_right_answers(self, answers_list):
        self.right_answers = ','.join(answers_list)

class Fill(models.Model):
    """填空题模型"""
    LEVEL_CHOICES = (
        ('1', '入门'),
        ('2', '简单'),
        ('3', '普通'),
        ('4', '较难'),
        ('5', '困难')
    )
    course = models.ForeignKey(Course, verbose_name="课程名称", on_delete=models.CASCADE, default="")
    question = models.TextField("题目", default="")
    right_answer = models.CharField("正确答案", max_length=200, default="")
    analysis = models.TextField("题目解析", default="暂无")
    score = models.PositiveSmallIntegerField("分值", default=2)
    level = models.CharField("难度等级", max_length=1, choices=LEVEL_CHOICES, default='1')

    class Meta:
        ordering = ['id']
        verbose_name = '填空题管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


class Judge(models.Model):
    """判断题模型"""
    LEVEL_CHOICES = (
        ('1', '入门'),
        ('2', '简单'),
        ('3', '普通'),
        ('4', '较难'),
        ('5', '困难')
    )
    ANSWER_CHOICES = (
        ('T', '正确'),
        ('F', '错误')
    )
    course = models.ForeignKey(Course, verbose_name="课程名称", on_delete=models.CASCADE, default="")
    question = models.TextField("题目", default="")
    right_answer = models.CharField("正确答案", max_length=1, choices=ANSWER_CHOICES, default="T")
    analysis = models.TextField("题目解析", default="暂无")
    score = models.PositiveSmallIntegerField("分值", default=2)
    level = models.CharField("难度等级", max_length=1, choices=LEVEL_CHOICES, default='1')

    class Meta:
        ordering = ['id']
        verbose_name = '判断题管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


