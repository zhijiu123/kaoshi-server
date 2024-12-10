import xadmin

from user.models import Student, Teacher, Clazz, College, Major
from import_export import resources

from user.resource import StudentResource


class CollegeAdmin(object):
    # 定义学院列表视图中要显示的字段
    list_display = ['id', 'college_name']
    # 定义学院列表视图中要使用的过滤字段
    list_filter = ['college_name']
    # 定义学院列表视图中可以搜索的字段
    search_fields = ['college_name']
    # 定义学院列表视图中可以点击链接的字段，通常是指向详细信息页面的链接
    list_display_links = ['college_name']
    # 定义学院列表视图中每页显示的记录数
    list_per_page = 10
    # 定义学院模型在Xadmin界面中的图标，使用Font Awesome图标
    model_icon = 'fa fa-graduation-cap'

class MajorAdmin(object):
    # 定义专业列表视图中要显示的字段
    list_display = ['id','college_name','major_name']
    # 定义专业列表视图中要使用的过滤字段
    list_filter = ['major_name']
    # 定义专业列表视图中可以搜索的字段
    search_fields = ['major_name']
    # 定义专业列表视图中可以点击链接的字段，通常是指向详细信息页面的链接
    list_display_links = ['major_name']
    # 定义专业列表视图中每页显示的记录数
    list_per_page = 10
    # 定义专业模型在Xadmin界面中的图标，使用Font Awesome图标
    model_icon = 'fa fa-graduation-cap'

class ClazzAdmin(object):
    list_display = ['id', 'year', 'major', 'clazz']
    list_filter = ['year', 'major']
    search_fields = ['id', 'year', 'major', 'clazz']
    list_display_links = ['clazz']
    list_per_page = 10
    # list_editable = ['name']
    model_icon = 'fa fa-institution '


class StudentAdmin(object):
    list_display = ['id', 'name', 'user','college','major', 'gender', 'clazz']
    list_filter = ['college', 'major']
    search_fields = ['name']
    list_display_links = ['name']
    list_per_page = 10
    model_icon = 'fa fa-user-circle-o'
    relfield_style = 'fk-ajax'
    # import_export_args = {'import_resource_class' : StudentResource, 'export_resource_class': StudentResource}
    import_export_args = {'import_resource_class' : StudentResource}


class TeacherAdmin(object):
    # 定义教师列表视图中要显示的字段
    list_display = ['id', 'name', 'user', 'gender', 'title', 'institute', 'telmobile']
    # 定义教师列表视图中要使用的过滤字段
    list_filter = ['gender', 'title', 'institute']
    # 定义教师列表视图中可以搜索的字段
    search_fields = ['id', 'name']
    # 定义教师列表视图中可以点击链接的字段，通常是指向详细信息页面的链接
    list_display_links = ['name','college_name']
    # 定义教师列表视图中每页显示的记录数
    list_per_page = 10
    # 定义教师模型在Xadmin界面中的图标，使用Font Awesome图标
    model_icon = 'fa fa-graduation-cap'

xadmin.site.register(College, CollegeAdmin)
xadmin.site.register(Major, MajorAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(Clazz, ClazzAdmin)
xadmin.site.register(Student, StudentAdmin)