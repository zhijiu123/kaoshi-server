import subprocess

from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from question.models import Choice, Fill, Judge, Program, Course
from question.serializers import ChoiceSerializer, FillSerializer, JudgeSerializer, ProgramSerializer, CourseSerializer


# Create your views here.
# 课程列表页
class CourseListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """课程列表页"""
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer

    def get_queryset(self):
        major_id = self.request.query_params.get("major_id")
        # 这里可以根据请求或其他条件来进一步过滤查询集
        if major_id:
            self.queryset = Course.objects.filter(major_id=major_id)
        return self.queryset
    

class ChoiceListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """选择题列表页"""
    # 这里要定义一个默认的排序，否则会报错
    queryset = Choice.objects.all().order_by('id')[:0]
    # 序列化
    serializer_class = ChoiceSerializer

    # 重写queryset
    def get_queryset(self):
        # 题目数量
        choice_number = int(self.request.query_params.get("choice_number"))
        level = int(self.request.query_params.get("level", 1))
        course_id = int(self.request.query_params.get("course_id", 1))

        if choice_number:
            self.queryset = Choice.objects.all().filter(level=level).order_by('?')[:choice_number]
            self.queryset = Choice.objects.all().filter(course_id=course_id).order_by('?')[:choice_number]
        return self.queryset

class ProgramListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """多选题列表页"""
    queryset = Program.objects.none()  # 使用空的queryset
    serializer_class = ProgramSerializer

    def get_queryset(self):
        # 获取请求参数
        program_number = self.request.query_params.get("program_number")
        level = self.request.query_params.get("level", '1')  # 难度等级默认为'1'
        course_id = self.request.query_params.get("course_id")  # 课程ID可以为空

        # 将字符串参数转换为整数
        try:
            program_number = int(program_number) if program_number else 0
            level = int(level)
        except ValueError:
            raise ValidationError("program_number 和 level 需要是整数")

        # 构建queryset
        queryset = Program.objects.filter(level=level).order_by('?')
        
        # 如果提供了course_id，需要筛选出对应课程的Programs
        if course_id:
            queryset = queryset.filter(course_id=course_id)

        # 使用切片操作限制返回结果的数量
        if program_number > 0:
            queryset = queryset[:program_number]

        return queryset

class FillListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """填空题列表页"""
    queryset = Fill.objects.none()  # 使用空的queryset
    serializer_class = FillSerializer

    def get_queryset(self):
        # 获取请求参数
        fill_number = self.request.query_params.get("fill_number")
        level = self.request.query_params.get("level", '1')
        course_id = self.request.query_params.get("course_id", '1')

        # 将字符串参数转换为整数
        try:
            fill_number = int(fill_number) if fill_number else 0
            level = int(level)
            course_id = int(course_id)
        except ValueError:
            raise ValidationError("fill_number, level 和 course_id 都需要是整数")

        # 构建queryset
        queryset = Fill.objects.filter(level=level, course_id=course_id).order_by('?')

        # 使用切片操作限制返回结果的数量
        if fill_number > 0:
            queryset = queryset[:fill_number]

        return queryset

class JudgeListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """判断题列表页"""
    queryset = Judge.objects.none()  # 使用空的queryset
    serializer_class = JudgeSerializer

    def get_queryset(self):
        # 获取请求参数
        judge_number = self.request.query_params.get("judge_number")
        level = self.request.query_params.get("level", '1')
        course_id = self.request.query_params.get("course_id", '1')

        # 将字符串参数转换为整数
        try:
            judge_number = int(judge_number) if judge_number else 0
            level = int(level)
            course_id = int(course_id)
        except ValueError:
            raise ValidationError("judge_number, level 和 course_id 都需要是整数")

        # 构建queryset
        queryset = Judge.objects.filter(level=level, course_id=course_id).order_by('?')

        # 使用切片操作限制返回结果的数量
        if judge_number > 0:
            queryset = queryset[:judge_number]

        return queryset