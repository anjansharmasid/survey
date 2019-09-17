from django.db import models


class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    candidate_name = models.CharField(max_length=255)
    candidate_email = models.CharField(max_length=255)

    def __str__(self):
        retval = "Name: " + self.candidate_name + "  Email :" + self.candidate_email
        return retval


class TestIdentifier(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=2082)
    test_version = models.IntegerField(default=1)
    test_id = models.ForeignKey(TestIdentifier, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    test_id = models.ForeignKey(TestIdentifier, on_delete=models.CASCADE)
    answer_a = models.CharField(max_length=255)
    answer_b = models.CharField(max_length=255)
    answer_c = models.CharField(max_length=255)
    answer_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)



    def __str__(self):
        return self.correct_answer


class CandidateAnswers(models.Model):
    id = models.AutoField(primary_key=True)
    test_id = models.ForeignKey(TestIdentifier, on_delete=models.CASCADE)
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    candidateAnswer = models.CharField(max_length=255)
    actualAnswer = models.CharField(max_length=255)
    status = models.BooleanField(default=False)


class TestResult(models.Model):
    id = models.AutoField(primary_key=True)
    test_id = models.ForeignKey(TestIdentifier, on_delete=models.CASCADE)
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    candidate_score = models.FloatField(default=0.0)
    candidate_answers_id = models.CharField(max_length=2000)



class Candidatelinkedtest(models.Model):
    id = models.AutoField(primary_key=True)
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    testidentifier_id = models.ForeignKey(TestIdentifier, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.candidate_id, self.testidentifier_id)



