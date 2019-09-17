# survey
Test survey project with a questionnaire and answers 



Example Print:

number = 2
print (number)
print (f'number: {number}')


Example: Data Type
string = 'some test'
print (string)

string_again = "some test again"
print (string_again)

booleanValue = True
print(booleanValue)

floaf_value = 23.45
print(floaf_value)

number = 2
print (number)
print (f'number: {number}')



Example : Input and Type custing 

text =  input("Enter some text", )
print(f'text: {text}')

number =  int(input("Enter a number", ))
print(f'number: {number}')

float = input('Enter a floating point number')
print(f'float: {float}')

true =  bool(input("Enter a  True/False", ))
print(f'true:{true}')



Example Except: 

try:
    number =  int(input("Enter a number", ))
    print(f'number: {number}')
except ValueError:
    print( "Only digits please")



Example List:

list = [3, 8, 1, 6, 0, 8, 4]
print(list)
print(len(list))

list.append(100)
print(list)
print(len(list))

ist.append(elem)
list.insert(index, elem)
list.extend(list2)
list.index(elem)
list.remove(elem)
list.sort() 
list.reverse()
list.pop(index)
 

Example tuple: Ordered and unchangeable.

tuple = ("apple", "banana", "cherry")
print(tuple)


Example Dictionary:(Key value pair)

dictionary= {
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}
print(dictionary)

key1 = dictionary.get("key1")
print(key1)

dictionary['key4']="value4"
print(dictionary)

key4 = dictionary.get("key4")
print(key4)


Example if statement:

boolVal = bool(True)
print(f'boolVal {boolVal}')
if boolVal:
    print(f'Than block:  the value is {boolVal}' )
else:
    print(f'Else block:  the value is {boolVal}')



Example for statement (loop)


for i in range (0,10,1):
    print(i)

list = [3, 8, 1, 6, 0, 8, 4]
for i in list:
    print(i)



Example while statement (loop)

start = True
count =0
while start:
    if count <10:
        print (count)
        count = count + 1
    else:
        start = false



Example function:

def function():
    print("function executed ")
function()


def function(param1, param2, param3):
    print(f'function executed  param1: {param1}  param2: {param2} param3: {param3}'  )
function("String",100,False)


#keyword arguments
function(param3=False, param2="some text", param1=123)



Example Class and Instance:

class ClassA:
    attributeA = "Some attributeA value"
    attributeB = "Some attributeB value"

    def __init__(self,name,address):
        self.attributeA=name
        self.attributeB=address

    def printclass(self):
        print(f'attributeA: {self.attributeA}')
        print(f'attributeB: {self.attributeB}')


instanceClassA = ClassA("John","London")
instanceClassA.printclass()


Example inheritance:

class ClassA:
    attributeA = "Some attributeA value"
    attributeB = "Some attributeB value"

    def __init__(self,name,address):
        self.attributeA=name
        self.attributeB=address

    def printme(self):
        print(f'attributeA: {self.attributeA}')
        print(f'attributeB: {self.attributeB}')



class PII:
    attributeA_PII = "Some PII data field"
    attributeB_PII = "Some more PII data field"

    def __init__(self,email,phomenumber):
        self.attributeA_PII=email
        self.attributeB_PII=phomenumber

    def printme(self):
        i_am_a_local_variable = "i_am_a_local_variable"
        print(f'self.attributeA_PII: {self.attributeA_PII}')
        print(f'self.attributeB_PII:{self.attributeB_PII}')
        print(f'local variable:{i_am_a_local_variable}')



class Person(ClassA,PII):
    pass
    person_attributeA="Some default person_attributeA"

    def __init__(self, ClassA, PII, Bank_name ):
        self.ClassA=ClassA
        self.PII=PII
        self.person_attributeA = Bank_name

    def printme(self):
        print(self.person_attributeA)


instanceClassA = ClassA("John","London")
instanceClassPII = PII("John@john.net","07756453420")
bank_Name = "HSBC London UK"
person = Person(instanceClassA,instanceClassPII,bank_Name)
person.printme()
person.ClassA.printme()
person.PII.printme()


Example import:

from <packagename> import <classname>
from time import sleep
sleep(1000)



Example 1: Thread

from _thread import start_new_thread
from time import sleep

threadId = 1  # thread counter
waiting = 2  # 2 sec. waiting time


def factorial(n):
    global threadId
    rc = 0

    if n < 1:  # base case
        print("{}: {}".format('\nThread', threadId))
        threadId += 1
        rc = 1
    else:
        returnNumber = n * factorial(n - 1)  # recursive call
        print("{} != {}  threadID: {}".format(str(n), str(returnNumber), threadId))
        rc = returnNumber

    return rc

start_new_thread(factorial, (5,))
start_new_thread(factorial, (4,))
start_new_thread(factorial, (10,))


print("Waiting for threads to return...")
sleep(waiting)






Example 2: Thread


import threading
import datetime

class myThread (threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    def run(self):
        print("\nStarting " + self.name)
        print_date(self.name, self.counter)
        print("Exiting " + self.name)

def print_date(threadName, counter):
    datefields = []
    today = datetime.date.today()
    datefields.append(today)
    print("{}[{}]: {}".format( threadName, counter, datefields[0] ))

# Create new threads
thread1 = myThread("Thread", 1)
thread2 = myThread("Thread", 2)

# Start new Threads
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("\nExiting the Program!!!")





1. Django installation.
Command : pip install django==2.2

2. Django installation update
Command : python manage.py migrate

3. Create a Django Web project named survey
Command : django-admin startproject survey .

4. Create a Django application named questions.
Command : python manage.py startapp questions

5. Create a application url file.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
    

6. Add application url file to project url file.
path('questions/', include('questions.urls')),
    path('', include('questions.urls'))
    

7. Start Server
Command : python manage.py runserver


8. Add admin users
Command : python manage.py createsuperuser


9. Models file

from django.db import models


class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    candidate_name = models.CharField(max_length=255)
    candidate_email = models.CharField(max_length=255)

    def __str__(self):
        retval = "Name: " + self.candidate_name + "  Email :" + self.candidate_email
        return retval
        
      
10. Project admin file (Register model to Admin Area, admin.py )

from django.contrib import admin
from .models import Candidate

admin.site.register(Candidate)


11. View files. 

from django.shortcuts import render

# Create your views here.
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('You are in index page')
    
    
12. Install application through settings.py
INSTALLED_APPS = [
    'questions.apps.QuestionsConfig'
]


13. Front end files.
 Create a directory named <appname>\templates
 Keep all html and css file inside <appname>\templates
 
14.  Copy base html for Bootstrap depending on CSS style you like, make a base.html and keep inside <appname>\templates

15.  Inside HTML file,start with 
     a. {% extends 'base.html'%}
     b. {% block content%}
     c.  keep all html inside 'block content'
     4. {% endblock%}

16. Use of Django form for data input and automatic field validation
     1. Create a class in <appname>/forms.py
     2. Import the form class in to view file and send to HTML file to render
     3. Inside the HTML file use the form as ' {{' form_name '}}'
