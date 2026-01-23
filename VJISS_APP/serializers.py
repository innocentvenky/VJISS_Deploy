from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

from . models import Create_User
from. models import Courses_Model
from . models import Syllabus_Model
from . models import InternshipOffers
from. models import Apply_Internship
from .models import Job_Notifications
from .models import About_Trainers
from . models import About_Company
from . models import NewBatchs
from . models import Student_Enrollment
from . models import Batch_Enrollment

# from . models import Student_Enrollment

class Create_User_Serializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model=Create_User
        fields='__all__'
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Create_User(**validated_data)
        user.set_password(password)  # ✅ hashes password
        user.save()
        return user


class Login_User_Serializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = Create_User.objects.get(email=data.get('email'))
            
        except Create_User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")

        user = authenticate(email=data.get('email'), password=data.get('password'))
        print(data.get('email'))
        print(data.get('password'))
        print(user)
        if not user:
            raise serializers.ValidationError("Invalid email or password")

        data['user'] = user
        return data 
    



        
    
class Course_serializer(serializers.ModelSerializer):
    class Meta:
        model=Courses_Model
        fields="__all__"

class Syllabus_serializer(serializers.ModelSerializer):
  
  
    class Meta:
        model=Syllabus_Model
        fields=[ "syllabus_id",
            "module",
            "description", "course_id", 
            ]
        
class CouresWithSyllabus_serializer(serializers.ModelSerializer):
    syllabus_courses = Syllabus_serializer(many=True, read_only=True)
    class Meta:
        model=Courses_Model
        fields=["course_id","course_name","course_logo","course_duration","course_fee","course_description","course_level","syllabus_courses"]

class InternshipOffers_serializer(serializers.ModelSerializer):
    class Meta:
        model=InternshipOffers
        fields="__all__"
        
class Apply_Internship_serializer(serializers.ModelSerializer):
    student = Create_User_Serializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(queryset=Create_User.objects.all(),write_only=True, source='student')
    internship_offers = InternshipOffers_serializer(read_only=True)
    internship_offers_id = serializers.PrimaryKeyRelatedField(queryset=InternshipOffers.objects.all(),write_only=True, source='internship_offers')
    class Meta:
        model=Apply_Internship
        fields="__all__"

class Job_Notifications_serializer(serializers.ModelSerializer):
    class Meta:
        model=Job_Notifications
        fields="__all__"

class About_Trainers_serializer(serializers.ModelSerializer):
    class Meta:
        model=About_Trainers
        fields="__all__"


class About_Company_serializer(serializers.ModelSerializer):
    class Meta:
        model=About_Company
        fields="__all__"   
        
         
class NewBatchModel_serializer(serializers.ModelSerializer):
    faculty = About_Trainers_serializer(read_only=True)
    trainer_id=serializers.PrimaryKeyRelatedField(queryset=About_Trainers.objects.all(),write_only=True,source='faculty')
    course=Course_serializer(read_only=True)
    course_id=serializers.PrimaryKeyRelatedField(queryset=Courses_Model.objects.all(),write_only=True,source='course')
    class Meta:
        model=NewBatchs     
        fields="__all__"
class Student_Enrollment_serializer(serializers.ModelSerializer):
    student = Create_User_Serializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(queryset=Create_User.objects.all(),write_only=True, source='student')
    course = Course_serializer(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(queryset=Courses_Model.objects.all(),write_only=True, source='course')
    class Meta:
        model=Student_Enrollment
        fields="__all__"


class Batch_Enrollment_serializer(serializers.ModelSerializer):
    student = Create_User_Serializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(queryset=Create_User.objects.all(),write_only=True, source='student')
    batch = NewBatchModel_serializer(read_only=True)
    batch_id = serializers.PrimaryKeyRelatedField(queryset=NewBatchs.objects.all(),write_only=True, source='batch')
    class Meta:
        model=Batch_Enrollment
        fields="__all__"