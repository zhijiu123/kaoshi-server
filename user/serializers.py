from django.contrib.auth.models import User
from rest_framework import serializers

from user.models import Student, Clazz, Major,College

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'

class ClazzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clazz
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    # 覆盖外键字段 只读
    # user = UserDetailSerializer()
    # clazz = ClazzSerializer(read_only=True)

    # 用于创建的只写字段
    clazz_id = serializers.PrimaryKeyRelatedField(queryset=Clazz.objects.all(), source='clazz', write_only=True)

    class Meta:
        model = Student
        fields = '__all__'
