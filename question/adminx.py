import xadmin

from question.models import Choice, Fill, Judge, Program, Course
from question.resource import ChoiceResource, FillResource, JudgeResource, ProgramResource, CourseResource

class CourseAdmin(object):
    list_display = ['id', 'college','major','course']
    list_filter = ['college','major']
    search_fields = ['id', 'course']
    list_display_links = ['course']
    list_per_page = 10
    # list_editable = ['question']
    model_icon = 'fa fa-question-circle-o'
    import_export_args = {'import_resource_class': CourseResource}


class ChoiceAdmin(object):
    list_display = ['id', 'course', 'question', 'answer_A', 'answer_B', 'answer_C', 'answer_D',
                    'right_answer', 'analysis', 'score', 'level']
    list_filter = ['level']
    search_fields = ['id', 'question']
    list_display_links = ['question']
    list_per_page = 10
    # list_editable = ['question']
    model_icon = 'fa fa-question-circle-o'
    import_export_args = {'import_resource_class': ChoiceResource}


class FillAdmin(object):
    list_display = ['id', 'course', 'question', 'right_answer', 'analysis', 'score', 'level']
    list_filter = ['level']
    search_field = ['id', 'question']
    list_display_links = ['question']
    list_per_page = 10
    # list_editable = ['question']
    model_icon = 'fa fa-edit '
    import_export_args = {'import_resource_class': FillResource}


class JudgeAdmin(object):
    list_display = ['id', 'course', 'question', 'right_answer', 'analysis', 'score', 'level']
    list_filter = ['level']
    search_field = ['id', 'question']
    list_display_links = ['question']
    list_per_page = 10
    # list_editable = ['question']
    model_icon = 'fa fa-check-square-o'
    import_export_args = {'import_resource_class': JudgeResource}


class ProgramAdmin(object):
    list_display = ['id', 'course', 'question', 'answer_A', 'answer_B', 'answer_C', 'answer_D','answer_E','answer_F','answer_G',
                    'right_answers', 'analysis', 'score', 'level']
    list_filter = ['level']
    search_field = ['id', 'question']
    list_display_links = ['question']
    list_per_page = 10
    # list_editable = ['question']
    model_icon = 'fa fa-laptop'
    import_export_args = {'import_resource_class': ProgramResource}

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Choice, ChoiceAdmin)
xadmin.site.register(Fill, FillAdmin)
xadmin.site.register(Judge, JudgeAdmin)
xadmin.site.register(Program, ProgramAdmin)
