from import_export import resources

from question.models import Choice, Fill, Judge, Program, Course

class CourseResource(resources.ModelResource):
    class Meta:
        model = Course
        fields = ('id', 'college','major','course')

class ChoiceResource(resources.ModelResource):
    class Meta:
        model = Choice
        fields = ('id', 'question', 'answer_A', 'answer_B', 'answer_C', 'answer_D', 'right_answer', 'analysis', 'score', 'level','course')


class FillResource(resources.ModelResource):
    class Meta:
        model = Fill
        fields = ('id', 'question', 'right_answer', 'analysis', 'score', 'level','course')


class JudgeResource(resources.ModelResource):
    class Meta:
        model = Judge
        fields = ('id', 'question', 'right_answer', 'analysis', 'score', 'level','course')


class ProgramResource(resources.ModelResource):
    class Meta:
        model = Program
        fields = ('id', 'question', 'answer_A', 'answer_B', 'answer_C', 'answer_D','answer_E','answer_F','answer_G','right_answer', 'analysis', 'score', 'level','course')