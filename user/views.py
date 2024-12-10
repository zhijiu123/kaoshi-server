from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import Student, Clazz,Major,College
from user.serializers import StudentSerializer, UserDetailSerializer, ClazzSerializer, MajorSerializer,CollegeSerializer


# Create your views here.
class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def jwt_response_payload_handler(token, user=None, request=None):
    """
    设置jwt登录之后返回token和user信息
    """
    student = Student.objects.get(user=user)
    return {
        'token': token,
        'user': UserDetailSerializer(user, context={'request': request}).data,
        'student': StudentSerializer(student, context={'request': request}).data
    }

class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    用户注册
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    def create(self, request, *args, **kwargs):
        # 从request.data中提取params字典
        params = request.data.get('params')
        if not params:
            return Response({'error': 'params is required'}, status=status.HTTP_400_BAD_REQUEST)

        # 从params字典中提取registerForm和其他字段
        register_form = params.get('registerForm')
        college_id = params.get('college_id')
        major_id = params.get('major_id')
        clazz_id = params.get('clazz_id')
        # 确保这些字段都存在
        if not college_id:
            return Response({'msg': '请选择学院'}, status=status.HTTP_400_BAD_REQUEST)
        if not major_id:
            return Response({'msg': '请选择专业'}, status=status.HTTP_400_BAD_REQUEST)
        if not clazz_id:
            return Response({'msg': '请选择班级'}, status=status.HTTP_400_BAD_REQUEST)

        # 检查用户名是否已存在
        if User.objects.filter(username=register_form['username']).exists():
            return Response({'msg': '用户名已存在'}, status=status.HTTP_400_BAD_REQUEST)
        
        # 序列化用户详细信息
        user_detail_serializer = UserDetailSerializer(data=register_form)
        if user_detail_serializer.is_valid():
            # 保存用户信息
            user = user_detail_serializer.save()
            # 加密密码
            user.password = make_password(register_form['password'])
            user.save()

            # 创建并保存学生信息
            student = Student(
                user=user,
                name=register_form['name'],
                college_id=college_id,
                major_id=major_id,
                clazz_id=clazz_id
            )
            student.save()

            return Response({'msg': '注册成功'}, status=status.HTTP_200_OK)
        else:
            # 序列化器验证失败，返回错误信息
            return Response(user_detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdatePwdApi(APIView):
    """
    修改用户密码
    """

    def patch(self, request):
        # 获取参数
        old_pwd = request.data['oldpwd']
        new_pwd = request.data['newpwd']
        user_id = request.data['userid']
    
        # 获得请求用户
        user = User.objects.get(id=user_id)
        # 检查原始密码是否正确
        if user.check_password(old_pwd):
            user.set_password(new_pwd)
            user.save()
        else:
            return Response(data={'msg': 'fail'}, status=status.HTTP_200_OK)
        # 返回数据
        return Response(data={'msg': 'success'}, status=status.HTTP_200_OK)

class CollegeViewSet(viewsets.ModelViewSet):
    """
    学院信息
    """
    queryset = College.objects.all().order_by('id')
    serializer_class = CollegeSerializer
    def get_queryset(self):
        # 这里可以根据请求或其他条件来进一步过滤查询集
        return self.queryset
    
class MajorLisViewSet(viewsets.ModelViewSet):
    """
    专业信息
    """
    queryset = Major.objects.all().order_by('id')
    serializer_class = MajorSerializer

    def get_queryset(self):
        college_name_id = self.request.query_params.get('college_name_id', None)
        if college_name_id:
            return Major.objects.filter(college_name_id=college_name_id).order_by('id')
        return Major.objects.all().order_by('id')


class ClazzListViewSet(viewsets.ModelViewSet):
    """
    班级信息
    """
    queryset = Clazz.objects.all().order_by('id')
    serializer_class = ClazzSerializer

    def get_queryset(self):
        major_id = self.request.query_params.get('major_id', None)
        if major_id:
            return Clazz.objects.filter(major_id=major_id).order_by('id')
        return Clazz.objects.all().order_by('id')

class StudentViewSet(viewsets.ModelViewSet):
    """
    学生信息
    """
    # 查询集
    queryset = Student.objects.all().order_by('id')
    # 序列化
    serializer_class = StudentSerializer

class CollegeMajorClazzViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    """
    学院、专业和班级信息的接口
    """

    def list(self, request):
        # 获取所有学院信息
        colleges = College.objects.all().order_by('id')
        college_serializer = CollegeSerializer(colleges, many=True)

        # 构建学院级别的选项
        options = []
        for college in college_serializer.data:
            college_option = {
                'value': str(college['id']),
                'label': college['college_name'],
                'children': []
            }

            # 获取当前学院下的所有专业信息
            majors = Major.objects.filter(college_name_id=college['id']).order_by('id')
            major_serializer = MajorSerializer(majors, many=True)

            # 构建专业级别的选项
            for major in major_serializer.data:
                major_option = {
                    'value': str(major['id']),
                    'label': major['major_name'],
                    'children': []
                }

                # 获取当前专业下的所有班级信息
                clazzes = Clazz.objects.filter(major_id=major['id']).order_by('id')
                clazz_serializer = ClazzSerializer(clazzes, many=True)

                # 构建班级级别的选项
                for clazz in clazz_serializer.data:
                    clazz_option = {
                        'value': str(clazz['id']),
                        'label': clazz['clazz']
                    }
                    major_option['children'].append(clazz_option)

                college_option['children'].append(major_option)

            options.append(college_option)

        return Response({'options': options})