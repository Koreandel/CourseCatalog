from django.shortcuts import get_object_or_404, get_list_or_404
from courses_api.models import Course


def create_course(data: dict) -> list:
    try:
        course = Course(
            name=data['name'],
            start_date=data['start_date'],
            expiration_date=data['expiration_date'],
            lecture_quantity=data['lecture_quantity'],
                )
        course.save()       
    except (ValueError, TypeError):
        return {"error": "not a valid data"}
    else:
        return Course.objects.filter(pk=course.id).values()[0]

    
def delete_course_by_id(pk: int) -> dict:
    try:
        course = Course.objects.get(pk=int(pk))
        course.delete()
    except Course.DoesNotExist:
        return {"error": "this course do not exist"}
    else:
        return {"deleted": True}


def get_all() -> list:
    all_courses = get_list_or_404(Course.objects.all().values())
    return all_courses


def update_course_by_id(data: dict, pk: int) -> dict:
    try:
        course = Course.objects.get(pk=pk)
        key_list = [key for key in data]
        for key in key_list:
            if key == 'name':
                course.name = data[key]
            elif key == 'lecture_quantity':
                course.lecture_quantity = data[key]
            elif key == 'start_date':
                course.start_date = data[key]
            elif key == 'expiration_date':
                course.expiration_date = data[key]
        course.save()
    except Course.DoesNotExist:
        return {"error": "this course do not exist"}
    except (ValueError, TypeError):
        return {"error": "not a valid data"}
    else:
        return Course.objects.filter(pk=course.id).values()[0]


def get_course_by_id(pk: int) -> dict:
    course = get_object_or_404(Course, pk=pk)
    return Course.objects.filter(pk=course.id).values()[0]


def get_course_by_name(name: str) -> dict:
    course = get_list_or_404(Course.objects.order_by('expiration_date').values(), name=name)
    return course
