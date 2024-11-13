from django.db import models


class Hunting(models.Model):
    """ Fields for Hunting table """

    question = models.CharField(max_length=255, blank=False)
    choice1 = models.CharField(max_length=200, blank=False)
    choice2 = models.CharField(max_length=200, blank=False)
    choice3 = models.CharField(max_length=200, blank=True)
    imgdir = models.CharField(max_length=250, blank=False)
    answer = models.IntegerField(blank=False, null=False)
    ansdesc = models.TextField(max_length=400, blank=False)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.question


class Response(models.Model):
    """ Fields for Responsee table """

    quest = models.ForeignKey(Hunting, on_delete=models.CASCADE)
    usranswer = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.quest


class Resume(models.Model):
    """ Fields for Recap table """

    description = models.TextField(blank=False)
    titre = models.CharField(max_length=60, blank=False)
    image = models.TextField(max_length=255, blank=False)


class Resumecat(models.Model):
    """ Fields for Recap by category table """

    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=False)































