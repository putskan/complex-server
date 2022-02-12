from rest_framework import serializers

from ..models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["slug", "question_title", "question_text", "question_medias",
                  "solution_answer", "solution_text", "solution_medias", "difficulty"]
        read_only_fields = ["slug", "question_title", "question_text", "question_medias",
                            "solution_answer", "solution_text", "solution_medias", "difficulty"]
        # get all data from ManyToMany fields
        depth = 1

