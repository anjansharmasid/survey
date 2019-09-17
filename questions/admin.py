from django.contrib import admin
from .models import Question, Answer, Candidate, CandidateAnswers, TestResult, TestIdentifier, Candidatelinkedtest


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Candidate)
admin.site.register(CandidateAnswers)
admin.site.register(TestResult)
admin.site.register(TestIdentifier)
admin.site.register(Candidatelinkedtest)

