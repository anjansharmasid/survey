from django.shortcuts import render


# Create your views here.
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Answer, Candidate, CandidateAnswers ,TestIdentifier, Candidatelinkedtest, TestResult
from .forms import CandidateForm, RetakeForm

def test_first(request, candidate_id,testIdentifier_id):
    question_id = getFirstQuestionNumber(testIdentifier_id)
    nevigation = questionNevigation(question_id,candidate_id,testIdentifier_id)
    next = nevigation.get('next')
    previous = nevigation.get('previous')
    total = nevigation.get('total')
    username = nevigation.get('username')
    remaining = remaining_question_count(question_id,testIdentifier_id)
    question = Question.objects.filter(id=question_id,test_id=testIdentifier_id).first()
    answer = Answer.objects.filter(question_id=question_id,test_id=testIdentifier_id).first()

    return render(request, 'test.html', {'question': question, 'answer': answer, 'question_id': question_id,
                                         'next':next, 'previous': previous,'candidate_id': candidate_id,'remaining': remaining,
                                         'username': username, 'testIdentifier_id': testIdentifier_id})


def test(request, testIdentifier_id, candidate_id, question_id):
    if request.method == 'POST':
        youranswer = "not_given"
        candidate_id = request.POST['candidate_id']
        question_id = request.POST['question_id']
        remaining = int(request.POST['remaining'])
        username = request.POST['username']
        try:
            youranswer = request.POST['youranswer']
        except KeyError:
            youranswer = "not_given"

        testIdentifier_id = request.POST['testIdentifier_id']
        saveAnswers(candidate_id, question_id, youranswer, testIdentifier_id)
        question_id = request.POST['next']
        if remaining == 0:
            return showResultpage(request, testIdentifier_id, candidate_id, username )
    nevigation = questionNevigation(question_id,candidate_id,testIdentifier_id)
    next = nevigation.get('next')
    previous = nevigation.get('previous')
    total = nevigation.get('total')
    username = nevigation.get('username')
    remaining = remaining_question_count(question_id,testIdentifier_id)
    question = Question.objects.filter(id=question_id,test_id=testIdentifier_id).first()
    answer = Answer.objects.filter(question_id=question_id,test_id=testIdentifier_id).first()
    checkedAnswers = findCheckedAnswers(answer,candidate_id)
    if question_id == total:
        return showResultpage(request,testIdentifier_id,candidate_id,username)
    return render(request, 'test.html', {'question': question, 'answer': checkedAnswers, 'question_id': question_id,
                                         'next':next, 'previous': previous,'candidate_id': candidate_id,'remaining': remaining,
                                         'username': username, 'testIdentifier_id': testIdentifier_id})

def findCheckedAnswers(answer,candidate_id):
    candidateAnswers = CandidateAnswers.objects.filter(test_id=answer.test_id, candidate_id=candidate_id, question_id=answer.question_id).first()
    option_a_checked = False
    option_b_checked = False
    option_c_checked = False
    option_d_checked = False
    try:
        if answer.answer_a == candidateAnswers.candidateAnswer:
            option_a_checked = True
        if answer.answer_b == candidateAnswers.candidateAnswer:
            option_b_checked = True
        if answer.answer_c == candidateAnswers.candidateAnswer:
            option_c_checked = True
        if answer.answer_d == candidateAnswers.candidateAnswer:
            option_d_checked = True
    except AttributeError:
        checkedAnswers = CheckedAnswers(answer, False,False,False,False)
        return checkedAnswers
    checkedAnswers = CheckedAnswers(answer,option_a_checked,option_b_checked,option_c_checked,option_d_checked)
    return checkedAnswers


def showResultpage(request,testIdentifier_id, candidate_id,username):
    result_to_display = make_candidata_result(testIdentifier_id, candidate_id)
    score = result_to_display.get('candidate_score')
    testQuestions= result_to_display.get('testlist')
    test_name =  result_to_display.get('test_name')
    return render(request, 'result.html', {'candidate_id': candidate_id, 'username': username, 'score': score,'results': testQuestions, 'test_name': test_name})


def getFirstQuestionNumber(testidentifier_id):
    question =  Question.objects.filter(test_id=testidentifier_id).order_by('id').first()
    return question.id

def questionNevigation(question_id,candidate_id,testidentifier_id):
    nevigation = {}
    next_privious = nevigatequestionnumber(question_id,testidentifier_id)
    candidate = Candidate.objects.get(pk=candidate_id)
    nevigation['username'] = candidate.candidate_name
    nevigation['question_id'] = question_id
    nevigation['next'] = next_privious.get("next")
    nevigation['previous'] = next_privious.get("previous")
    nevigation['total'] = next_privious.get("total")
    return nevigation


def nevigatequestionnumber(question_id,testidentifier_id):
    next_privious = {}
    total = Question.objects.filter(test_id=testidentifier_id).count()
    previous = get_previous_question_id(question_id,testidentifier_id)
    next = get_next_question_id(question_id,testidentifier_id)
    next_privious['next']=next
    next_privious['previous'] = previous
    next_privious['total'] = total
    next_privious['question_id'] = question_id
    return next_privious


def remaining_question_count(current_question_id,testidentifier_id):
    question_count = Question.objects.filter(test_id=testidentifier_id).filter(id__gte=current_question_id).count()
    return int(question_count) -1


def get_next_question_id(current_question_id,testidentifier_id):
    position = int(current_question_id)
    try:
        current_question_id = int(current_question_id) + 1
        question = Question.objects.filter(test_id=testidentifier_id).filter(id__gte=current_question_id ).first()
        retval = question.id
    except AttributeError:
        return position
    except ObjectDoesNotExist:
        return position
    return retval


def get_previous_question_id(current_question_id,testidentifier_id):
    position = int(current_question_id)
    try:
        current_question_id = int(current_question_id) - 1
        question = Question.objects.filter(test_id=testidentifier_id).filter(id__lte=current_question_id ).last()
        retval = question.id
    except AttributeError:
        return position
    except ObjectDoesNotExist:
        return position
    return retval


def starttest(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            username = form['username'].value()
            email = form['email'].value()
            testidentifier_id = form['tests'].value()
            candidate_id = find_candidate_create(username, email)
            find_create_candidate_test_link(candidate_id, testidentifier_id)
            return test_first(request, candidate_id, testidentifier_id)
    else:
        form = CandidateForm()
    return render(request, 'createcandidate.html', {'form': form})


def find_candidate_create(username, email):
    try:
        candidate = Candidate.objects.get(candidate_name=username, candidate_email=email)
    except ObjectDoesNotExist:
        candidate = Candidate(candidate_name=username, candidate_email=email)
        candidate.save()
        return candidate.id
    return candidate.id


def find_create_candidate_test_link(candidate_id, testidentifier_id):
    try:
        candidatelinkedtest = Candidatelinkedtest.objects.get(candidate_id=candidate_id, testidentifier_id=testidentifier_id)
    except ObjectDoesNotExist:
        candidate = Candidate.objects.get(pk=candidate_id)
        testidentifier = TestIdentifier.objects.get(pk=testidentifier_id)
        candidatelinkedtest = Candidatelinkedtest(candidate_id=candidate, testidentifier_id=testidentifier)
        candidatelinkedtest.save()
        return candidatelinkedtest.id
    return candidatelinkedtest.id


def saveAnswers(candidate_id, question_id, youranswer, testIdentifier_id):
    answer = Answer.objects.filter(question_id=question_id, test_id=testIdentifier_id).first()
    correctAns = answer.correct_answer
    status = False
    if youranswer == correctAns:
        status = True
    testIdentifier = TestIdentifier.objects.get(pk=int(testIdentifier_id))
    candidate = Candidate.objects.get(pk=int(candidate_id))
    question = Question.objects.get(pk=int(question_id))

    # first check if this question was answered before
    # if yes, update the last nswer.
    # else create and save.
    try:
        candidateAnswers = CandidateAnswers.objects.filter(test_id=testIdentifier,candidate_id=candidate, question_id=question).first()
        candidateAnswers.candidateAnswer=youranswer
        candidateAnswers.actualAnswer=correctAns
        candidateAnswers.status=status
        candidateAnswers.save()
    except AttributeError:
        candidateAnswers =  CandidateAnswers(test_id=testIdentifier,candidate_id=candidate,
                                         question_id=question,candidateAnswer=youranswer,actualAnswer=correctAns,
                                         status=status)
        candidateAnswers.save()


def retake(request,username,candidate_id):
    form = RetakeForm()
    return render(request,'retake.html', {'form': form, 'username': username, 'candidate_id': candidate_id})


def redirect(request,candidate_id):
    form = RetakeForm(request.POST)
    testIdentifier_id = form['test'].value()
    return test_first(request, candidate_id, testIdentifier_id)


def make_candidata_result(testIdentifier_id,candidate_id):
    print("Work in progress")
    result_to_display = {}
    testIdentifier = TestIdentifier.objects.get(pk=testIdentifier_id)
    test_name = testIdentifier.description
    candidate =  Candidate.objects.get(pk=candidate_id)
    testResultList = CandidateAnswers.objects.filter(test_id=testIdentifier, candidate_id=candidate)
    result = calculate_candidata_score(testResultList)
    candidate_score = result.get('candidate_score')
    candidate_answers_id = result.get('candidate_answers_id')
    result_to_display['candidate_score'] = result.get('candidate_score')
    result_to_display['testlist'] = result.get('testlist')
    result_to_display['test_name'] = test_name
    try:
        testResult = TestResult.objects.filter(test_id=testIdentifier, candidate_id=candidate).first()
        testResult.candidate_score=candidate_score
        testResult.candidate_answers_id=candidate_answers_id
        testResult.save()
    except AttributeError:
        testResult = TestResult(test_id=testIdentifier,candidate_id=candidate,candidate_score=candidate_score,candidate_answers_id=candidate_answers_id)
        testResult.save()
    return result_to_display

def calculate_candidata_score(testResultList):
    total = len(testResultList)
    correct = 0;
    count = 1
    test = ""
    testlist = {}
    result = {}
    #print(connection.queries)
    for testResult in testResultList:
        if testResult.status:
            correct = correct + 1
        test = test +'   Question  :'+testResult.question_id.question  + '      Your answer: '+ testResult.candidateAnswer + '      Correct answer: ' + testResult.actualAnswer
        testlist['Question  :'+testResult.question_id.question  + '      Your answer: '+ testResult.candidateAnswer + '      Correct answer: ' + testResult.actualAnswer] = count
        count = count + 1

    pc_score = correct / total * 100
    result['candidate_score'] = pc_score
    # Get questions and answers.
    result['candidate_answers_id'] = test
    result['testlist'] = testlist
    return result



def index(request):
    return HttpResponse('You are in Questions Application, please login   <a href="/questions/starttest" class="btn btn-primary">login</a>')


def questions(request):
    return HttpResponse('You are in Questions Application, please login   <a href="/questions/starttest" class="btn btn-primary">login</a>')


def answers(request):
    return HttpResponse('You are in Answers Application')


def candidate(request):
    return HttpResponse('You are in candidate page')


def candidateanswers(request):
    return HttpResponse('You are in candidate answers page')


def testresult(request):
    return HttpResponse('You are in candidate test result page')


def home(request):
    return render(request,'Home.html')


class CheckedAnswers:
    id=''
    question_id = ''
    test_id = ''
    answer_a = ''
    answer_b = ''
    answer_c = ''
    answer_d = ''
    correct_answer = ''
    answer_a_checked = ''
    answer_b_checked = ''
    answer_c_checked = ''
    answer_d_checked = ''

    def __init__(self,answer,answer_a_checked,answer_b_checked,answer_c_checked,answer_d_checked):
        self.answer_a_checked=answer_a_checked
        self.answer_b_checked = answer_b_checked
        self.answer_c_checked = answer_c_checked
        self.answer_d_checked = answer_d_checked
        self.id = answer.id
        self.question_id=answer.question_id
        self.test_id=answer.test_id
        self.answer_a=answer.answer_a
        self.answer_b=answer.answer_b
        self.answer_c=answer.answer_c
        self.answer_d=answer.answer_d
        self.correct_answer=answer.correct_answer


