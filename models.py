class Enrollment(models.Model):
    user = models.CharField(max_length=100)  # simple version
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return f"Submission {self.id} for enrollment {self.enrollment.id}"
