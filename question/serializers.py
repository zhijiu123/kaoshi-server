from rest_framework import serializers

from question.models import Choice, Fill, Judge, Program, Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class FillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fill
        fields = '__all__'


class JudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = '__all__'


# class ProgramSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Program
#         fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
    answer_options = serializers.SerializerMethodField()  # 自定义字段来存储答案选项数组
    right_answers_list = serializers.SerializerMethodField()  # 自定义字段来存储正确答案的列表形式

    class Meta:
        model = Program
        fields = [
            'id', 'question', 'answer_A', 'answer_B', 'answer_C', 'answer_D',
            'answer_E', 'answer_F', 'answer_G', 'right_answers', 'right_answers_list',
            'analysis', 'score', 'level', 'course', 'answer_options'
        ]

    def get_answer_options(self, obj):
        # 创建一个字典来存储答案选项
        answer_options = {
            'A': obj.answer_A,
            'B': obj.answer_B,
            'C': obj.answer_C,
            'D': obj.answer_D,
            'E': obj.answer_E,
            'F': obj.answer_F,
            'G': obj.answer_G,
        }
        # 过滤掉空值，然后返回答案选项的列表
        return [opt for opt in answer_options.values() if opt]

    def get_right_answers_list(self, obj):
        # 使用模型中的方法来获取正确答案的列表形式
        return obj.get_right_answers()
