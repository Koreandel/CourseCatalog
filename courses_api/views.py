from django.http import JsonResponse
from django.views import View
import json
from courses_api.db import courses_db


class CourseView(View):
    def post(self, request):
        data = json.loads(request.body.decode())
        new_course = courses_db.create_course(data)
        return JsonResponse({"created": new_course})

    def get(self, request):
        if request.GET.get('name'):
            courses = courses_db.get_course_by_name(request.GET.get('name'))
        elif request.GET.get('pk'):
            courses = courses_db.get_course_by_id(request.GET.get('pk'))
        else:
            courses = courses_db.get_all()
        return JsonResponse(courses, safe=False)

    def put(self, request):
        data = json.loads(request.body.decode())
        course = courses_db.update_course_by_id(data, request.GET.get('pk'))
        return JsonResponse({"changed": course})

    def delete(self, request):
        status = courses_db.delete_course_by_id(request.GET.get('pk'))
        return JsonResponse(status)
