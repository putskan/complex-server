from django.db import models
from server.utils.db import random_slug


class QuestionMedia(models.Model):
    slug = models.CharField(
        max_length=40,
        default=random_slug,
        unique=True,
    )
    label = models.CharField(blank=True, max_length=100)
    media = models.ImageField()

    def __str__(self):
        return f"{self.slug} | {self.label}"


class SolutionMedia(models.Model):
    slug = models.CharField(
        max_length=40,
        default=random_slug,
        unique=True,
    )
    label = models.CharField(blank=True, max_length=100)
    media = models.ImageField()

    def __str__(self):
        return f"{self.slug} | {self.label}"


class Question(models.Model):
    class Difficulty(models.TextChoices):
        EASY = "EASY", "Easy"
        MEDIUM = "MEDIUM", "Medium"
        HARD = "HARD", "Hard"

    slug = models.CharField(
        max_length=40,
        default=random_slug,
        unique=True,
    )
    question_title = models.CharField(blank=False, null=False, max_length=100)
    question_text = models.TextField(blank=True)
    question_medias = models.ManyToManyField(to=QuestionMedia, blank=True)

    solution_answer = models.CharField(blank=False, null=False, max_length=50)
    solution_text = models.TextField(blank=True)
    solution_medias = models.ManyToManyField(to=SolutionMedia, blank=True)

    difficulty = models.CharField(max_length=25, choices=Difficulty.choices)

    def __str__(self):
        return f"{self.question_title} | {self.question_text[:50]}"
