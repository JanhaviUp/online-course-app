from django.shortcuts import render, redirect
from .models import Course, Lesson, Question, Choice, Submission

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=course)
    questions = Question.objects.filter(course=course)

    return render(request, 'course_details_bootstrap.html', {
        'course': course,
        'lessons': lessons,
        'questions': questions
    })


def submit(request, course_id):
    if request.method == 'POST':
        selected_choices = request.POST.getlist('choice')
        submission = Submission.objects.create()

        for choice_id in selected_choices:
            choice = Choice.objects.get(id=choice_id)
            submission.choices.add(choice)

        return redirect('show_exam_result', course_id=course_id)


def show_exam_result(request, course_id):
    submission = Submission.objects.last()
    total = submission.choices.count()
    correct = submission.choices.filter(is_correct=True).count()

    score = (correct / total) * 100 if total > 0 else 0

    return render(request, 'course_details_bootstrap.html', {
        'score': score,
        'correct': correct,
        'total': total
    })
