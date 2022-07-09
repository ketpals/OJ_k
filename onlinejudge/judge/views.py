from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.views import generic
import os, filecmp
# from judge.functions.functions import handle_uploaded_file

from .forms import ProblemForm, SubmissionForm
from .models import Problem, Submissions, Testcases


def intro(request):
    return render(request, 'base.html')


def view_problems(request):
    problems_list = Problem.objects.order_by('-problem_name')[:5]
    context = {'problems_list': problems_list}
    return render(request, 'prob.html', context)


def problem_detail(request, problem_id):
    prob = get_object_or_404(Problem, pk=problem_id)
    return render(request, 'detail.html', {'problem': prob})


def add_problem(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            problem_form = ProblemForm(request.POST, request.FILES)
            if problem_form.is_valid():
                # save a new problem
                problem = problem_form.save()
                problem.save()
                # link the to the problem and save the test case to db
                return HttpResponseRedirect("/judge/problem")
        else:
            # instantiate a new ProblemForm and then render the addproblem page
            problem_form = ProblemForm()
            return render(request, "addprob.html", {"problem_form": problem_form})
        # if user is not logged in, throw him to a sign-in page
        # if not request.user.is_authenticated:
        #     return HttpResponseRedirect("http://127.0.0.1:8000/login")
        # else:


def submit(request, problem_id):
    if request.method == 'POST':
        sub_form = SubmissionForm(request.POST, request.FILES)
        if sub_form.is_valid():
            # handle_uploaded_file(request.POST, request.FILES)
            sub = sub_form.save()
            sub.problem = Problem.objects.get(code=problem_id)
            print(sub.problem.code)
            # sub.submitter = Coder.objects.get(user=request.user)
            # print(sub.submitter)
            sub.save()
            # evaluate_submission.delay(sub.id)
            return HttpResponse("Code Submitted!")
    else:
        sub_form = SubmissionForm()
        payload = {"sub_form": sub_form, "pid": problem_id}
        return render(request, "detail.html", payload)



# Create your views here.
