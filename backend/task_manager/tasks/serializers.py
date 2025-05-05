from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# # tasks/serializers.py (Alternative fields definition)

# from rest_framework import serializers
# from .models import Task

# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ['id', 'title', 'description', 'completed', 'created_at', 'due_date']
#         # Or if you want to exclude some fields:
#         # exclude = ['field_to_exclude']