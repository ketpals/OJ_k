from django.db import models

from django.contrib.auth.models import User


class Problem(models.Model):
    # problem_id = models.IntegerField(max_length=100)
    problem_name = models.CharField(max_length=100)
    problem_desc = models.CharField(max_length=500)
    diff = models.CharField(max_length=50)
    problem_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.problem_name


class Testcases(models.Model):
    input = models.CharField(max_length=500)
    output = models.CharField(max_length=500)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def __str__(self):
        return self.input



LANGUAGES = (
                ("C", "GNU C"),
                ("CPP", "GNU C++"),
                )


class Submissions(models.Model):
    # STATUSES = (
    #     ("NT", "Not tested"),
    #     ("AC", "Accepted"),
    #     ("WA", "Wrong Answer")
    # )
    # submitter = models.ForeignKey(Coder, null=True, on_delete=models.CASCADE)
    # status = models.CharField(max_length=2, default="NT", choices=STATUSES)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    verdict = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    code = models.CharField(max_length=1000)
    lang = models.CharField(max_length=4, default="C", choices=LANGUAGES)
    file = models.FileField(null=True, upload_to='solutions', max_length=1000)

    def __str__(self):
        return self.verdict


class Important(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    Imp_status = models.BooleanField(default=False)

    def __str__(self):
        return self.Imp_status
# Create your models here.

# Create your models here.

# Create your models here.
