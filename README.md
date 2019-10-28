<div class="row">
    <div class="col-sm-2"> </div>
    <div class="col-sm-9">
         <div class="card">
           <div class="card-header">
               Language and Syntax  : print, input, data type, assignment, list and dictionary, if, for, while, functions, class, instance, inheritance, import, publish packages.
           </div>
           <div class="card-body">
                <h5 class="card-title"> </h5>
                    <p class="card-text"> <p>


<p><br /><strong>Python Indentation:</strong></p>
<p>Python uses colon (:) and indentation, unlike most programming languages that uses curly braces coma or semicolon (, ;) and {} to identify a block of code. Python does not use any end of statement symbol like semicolon.<br />count = 1<br />for count &gt; 10:<br />&nbsp; &nbsp; &nbsp;print(count)</p>
<p>print("You have seen Python Indentation Example")</p>
<p><br /><strong>Example 1 Print:</strong></p>
<p>number = 2<br />print (number)<br />print (f'number: {number}')</p>
<p><br />Example: Data Type<br />string = 'some test'<br />print (string)</p>
<p>string_again = "some test again"<br />print (string_again)</p>
<p>booleanValue = True<br />print(booleanValue)</p>
<p>floaf_value = 23.45<br />print(floaf_value)</p>
<p>number = 2<br />print (number)<br />print (f'number: {number}')</p>
<p>&nbsp;</p>
<p><strong>Example 2 Input and Type custing:</strong></p>
<p>text = input("Enter some text", )<br />print(f'text: {text}')</p>
<p>number = int(input("Enter a number", ))<br />print(f'number: {number}')</p>
<p>float = input('Enter a floating point number')<br />print(f'float: {float}')</p>
<p>true = bool(input("Enter a True/False", ))<br />print(f'true:{true}')</p>
<p>&nbsp;</p>
<p><strong>Example 3 Except:</strong></p>
<p>try:<br />&nbsp; &nbsp;number = int(input("Enter a number", ))<br />&nbsp; &nbsp;print(f'number: {number}')<br />except ValueError:<br />&nbsp; &nbsp;print( "Only digits please")</p>
<p>&nbsp;</p>
<p><strong>Example 4 List:</strong></p>
<p>list = [3, 8, 1, 6, 0, 8, 4]<br />print(list)<br />print(len(list))</p>
<p>list.append(100)<br />print(list)<br />print(len(list))</p>
<p>ist.append(elem)<br />list.insert(index, elem)<br />list.extend(list2)<br />list.index(elem)<br />list.remove(elem)<br />list.sort() <br />list.reverse()<br />list.pop(index)</p>
<p><strong>Example 5 tuple: Ordered and unchangeable.</strong></p>
<p>tuple = ("apple", "banana", "cherry")<br />print(tuple)</p>
<p><br /><strong>Example 6 Dictionary:(Key value pair)</strong></p>
<p>dictionary= {<br /> "key1": "value1",<br /> "key2": "value2",<br /> "key3": "value3"<br />}<br />print(dictionary)</p>
<p>key1 = dictionary.get("key1")<br />print(key1)</p>
<p>dictionary['key4']="value4"<br />print(dictionary)</p>
<p>key4 = dictionary.get("key4")<br />print(key4)</p>
<p><br /><strong>Example 7 if statement:</strong></p>
<p>boolVal = bool(True)<br />print(f'boolVal {boolVal}')<br />if boolVal:<br />&nbsp; &nbsp;print(f'Than block: the value is {boolVal}' )<br />else:<br />&nbsp; print(f'Else block: the value is {boolVal}')</p>
<p>&nbsp;</p>
<p><strong>Example 8 for statement (loop)</strong></p>
<p><br />for i in range (0,10,1):<br />&nbsp; &nbsp;print(i)</p>
<p>list = [3, 8, 1, 6, 0, 8, 4]<br />for i in list:<br />&nbsp; &nbsp;print(i)</p>
<p>&nbsp;</p>
<p><strong>Example 9 while statement (loop)</strong></p>
<p>start = True<br />count =0<br />while start:<br />&nbsp; &nbsp;if count &lt;10:<br />&nbsp; &nbsp; &nbsp; print (count)<br />&nbsp; &nbsp; &nbsp; count = count + 1<br />&nbsp; &nbsp;else:<br />&nbsp; &nbsp; &nbsp; start = false</p>
<p>&nbsp;</p>
<p><strong>Example 10 function:</strong></p>
<p>def function():<br />&nbsp; &nbsp; print("function executed ")</p>
<p>function()</p>
<p><br />def function(param1, param2, param3):<br />&nbsp; &nbsp; print(f'function executed param1: {param1} param2: {param2} param3: {param3}' )<br /> <br />function("String",100,False)</p>
<p><br />#keyword arguments<br />function(param3=False, param2="some text", param1=123)</p>
<p>&nbsp;</p>
<p><br /><strong>Example 11 Class and Instance:</strong></p>
<p>class ClassA:<br />&nbsp; &nbsp; attributeA = "Some attributeA value"<br />&nbsp; &nbsp; attributeB = "Some attributeB value"</p>
<p>&nbsp; &nbsp; def __init__(self,name,address):<br />&nbsp; &nbsp; &nbsp; &nbsp; self.attributeA=name<br />&nbsp; &nbsp; &nbsp; &nbsp; self.attributeB=address</p>
<p>&nbsp; &nbsp; def printclass(self):<br />&nbsp; &nbsp; &nbsp; &nbsp; print(f'attributeA: {self.attributeA}')<br />&nbsp; &nbsp; &nbsp; &nbsp; print(f'attributeB: {self.attributeB}')</p>
<p><br />instanceClassA = ClassA("John","London")<br />instanceClassA.printclass()</p>
<p><br /><span style="text-decoration: underline;"><strong>Example 12 inheritance:</strong></span></p>
<p>class ClassA:<br />&nbsp; &nbsp; &nbsp;attributeA = "Some attributeA value"<br />&nbsp; &nbsp; &nbsp;attributeB = "Some attributeB value"</p>
<p>&nbsp; &nbsp; &nbsp;def __init__(self,name,address):<br />&nbsp; &nbsp; &nbsp; &nbsp; self.attributeA=name<br />&nbsp; &nbsp; &nbsp; &nbsp; self.attributeB=address</p>
<p>&nbsp; &nbsp; def printme(self):<br />&nbsp; &nbsp; &nbsp; &nbsp; print(f'attributeA: {self.attributeA}')<br />&nbsp; &nbsp; &nbsp; &nbsp; print(f'attributeB: {self.attributeB}')</p>
<p>&nbsp;</p>
<p>class PII:<br />&nbsp; &nbsp; &nbsp;attributeA_PII = "Some PII data field"<br />&nbsp; &nbsp; &nbsp;attributeB_PII = "Some more PII data field"</p>
<p>&nbsp; &nbsp; def __init__(self,email,phomenumber):<br />&nbsp; &nbsp; &nbsp; &nbsp; self.attributeA_PII=email<br />&nbsp; &nbsp; &nbsp; &nbsp; self.attributeB_PII=phomenumber</p>
<p>&nbsp; &nbsp; def printme(self):<br />&nbsp; &nbsp; &nbsp; &nbsp; i_am_a_local_variable = "i_am_a_local_variable"<br />&nbsp; &nbsp; &nbsp; &nbsp; print(f'self.attributeA_PII: {self.attributeA_PII}')<br />&nbsp; &nbsp; &nbsp; &nbsp; print(f'self.attributeB_PII:{self.attributeB_PII}')<br />&nbsp; &nbsp; &nbsp; &nbsp; print(f'local variable:{i_am_a_local_variable}')</p>
<p>&nbsp;</p>
<p>class Person(ClassA,PII):<br />&nbsp; &nbsp; &nbsp;pass<br />&nbsp; &nbsp; &nbsp;person_attributeA="Some default person_attributeA"</p>
<p>&nbsp; &nbsp; def __init__(self, ClassA, PII, Bank_name ):<br />&nbsp; &nbsp; &nbsp; &nbsp; self.ClassA=ClassA<br />&nbsp; &nbsp; &nbsp; &nbsp; self.PII=PII<br />&nbsp; &nbsp; &nbsp; &nbsp; self.person_attributeA = Bank_name</p>
<p>&nbsp; &nbsp; def printme(self):<br />&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;print(self.person_attributeA)</p>
<p><br />instanceClassA = ClassA("John","London")<br />instanceClassPII = PII("John@john.net","07756453420")<br />bank_Name = "HSBC London UK"<br />person = Person(instanceClassA,instanceClassPII,bank_Name)<br />person.printme()<br />person.ClassA.printme()<br />person.PII.printme()</p>
<p><br /><span style="text-decoration: underline;"><strong>Example 13 import:</strong></span></p>
<p>from &lt;packagename&gt; import &lt;classname&gt;<br />from time import sleep<br />sleep(1000)</p>
<p>&nbsp;</p>
<p><span style="text-decoration: underline;"><strong>Example 14: Thread</strong></span></p>
<p>from _thread import start_new_thread<br />from time import sleep</p>
<p>threadId = 1 # thread counter<br />waiting = 2 # 2 sec. waiting time</p>
<p><br />def factorial(n):<br />&nbsp; &nbsp; global threadId<br />&nbsp; &nbsp; rc = 0</p>
<p>if n &lt; 1: # base case<br />&nbsp; &nbsp; print("{}: {}".format('\nThread', threadId))<br />&nbsp; &nbsp; threadId += 1<br />&nbsp; &nbsp; rc = 1<br /> else:<br />&nbsp; &nbsp; returnNumber = n * factorial(n - 1) # recursive call<br />&nbsp; &nbsp; print("{} != {} threadID: {}".format(str(n), str(returnNumber), threadId))<br />&nbsp; &nbsp; rc = returnNumber</p>
<p>return rc</p>
<p>start_new_thread(factorial, (5,))<br />start_new_thread(factorial, (4,))<br />start_new_thread(factorial, (10,))</p>
<p><br />print("Waiting for threads to return...")<br />sleep(waiting)</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><br /><span style="text-decoration: underline;"><strong>Example 15: Thread</strong></span></p>
<p><br />import threading<br />import datetime</p>
<p>class myThread (threading.Thread):<br />&nbsp; &nbsp; def __init__(self, name, counter):<br />&nbsp; &nbsp; &nbsp; &nbsp; threading.Thread.__init__(self)<br />&nbsp; &nbsp; &nbsp; &nbsp; self.threadID = counter<br />&nbsp; &nbsp; &nbsp; &nbsp; self.name = name<br />&nbsp; &nbsp; &nbsp; &nbsp; self.counter = counter</p>
<p>&nbsp; &nbsp; def run(self):<br />&nbsp; &nbsp; &nbsp; &nbsp; print("\nStarting " + self.name)<br />&nbsp; &nbsp; &nbsp; &nbsp; print_date(self.name, self.counter)<br />&nbsp; &nbsp; &nbsp; &nbsp; print("Exiting " + self.name)</p>
<p>&nbsp; &nbsp; def print_date(threadName, counter):<br />&nbsp; &nbsp; &nbsp; &nbsp;datefields = []<br />&nbsp; &nbsp; &nbsp; &nbsp;today = datetime.date.today()<br />&nbsp; &nbsp; &nbsp; &nbsp;datefields.append(today)<br />&nbsp; &nbsp; &nbsp; &nbsp;print("{}[{}]: {}".format( threadName, counter, datefields[0] ))</p>
<p># Create new threads<br />thread1 = myThread("Thread", 1)<br />thread2 = myThread("Thread", 2)</p>
<p># Start new Threads<br />thread1.start()<br />thread2.start()</p>
<p>thread1.join()<br />thread2.join()<br />print("\nExiting the Program!!!")</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
               <h3> <p> Django Framework and Web Application Development: </p> </h3>
<p>&nbsp;</p>
               <p>&nbsp;</p>
               <p>&nbsp;</p>
<p><strong>1. Django installation. </strong></p>
<p>Command : pip install django==2.2</p>
<p>&nbsp;</p>
<p><strong>2. Django installation update</strong></p>
<p>Command : python manage.py migrate</p>
<p>&nbsp;</p>
<p><strong>3. Create a Django Web project named survey</strong></p>
<p>Command : django-admin startproject survey .</p>
<p>&nbsp;</p>
<p><strong>4. Create a Django application named questions.</strong></p>
<p>Command : python manage.py startapp questions</p>
<p>&nbsp;</p>
<p><strong>5. Create a application url file.</strong></p>
<p>from django.urls import path</p>
<p>from . import views</p>
<p>&nbsp;</p>
<p>urlpatterns = [</p>
<p>    path('', views.index)</p>
 <p>&nbsp;</p>

<p><strong>6. Add application url file to project url file.</strong></p>
<p>path('questions/', include('questions.urls')),</p>
<p>    path('', include('questions.urls'))</p>
 <p>&nbsp;</p>
<p>&nbsp;</p>
<p><strong>7. Start Server</strong></p>
<p>Command : python manage.py runserver</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><strong>8. Add admin users</strong></p>
<p>Command : python manage.py createsuperuser</p>
<p>&nbsp;</p>
 <p><strong>9. Models file</strong></p>
<p>&nbsp;</p>
<p>from django.db import models</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>class Candidate(models.Model):</p>
<p>    id = models.AutoField(primary_key=True)</p>
<p>    candidate_name = models.CharField(max_length=255)</p>
<p>    candidate_email = models.CharField(max_length=255)</p>
<p>&nbsp;</p>
<p>    def __str__(self):</p>
<p>        retval = "Name: " + self.candidate_name + "  Email :" + self.candidate_email</p>
<p>        return retval</p>
<p>        <p>&nbsp;</p>
      <p>&nbsp;</p>
<p><strong>10. Project admin file (Register model to Admin Area, admin.py )</strong></p>
<p>&nbsp;</p>
<p>from django.contrib import admin</p>
<p>from .models import Candidate</p>
<p>&nbsp;</p>
<p>admin.site.register(Candidate)</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><strong>11. View files. </strong></p>
<p>&nbsp;</p>
<p>from django.shortcuts import render</p>
<p>&nbsp;</p>
<p># Create your views here.</p>
<p>from django.db import connection</p>
<p>from django.core.exceptions import ObjectDoesNotExist</p>
<p>from django.http import HttpResponse</p>
<p>from django.shortcuts import render</p>
<p>&nbsp;</p>
<p>def index(request):</p>
<p>    return HttpResponse('You are in index page')</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
<p><strong>12. Install application through settings.py</strong></p>
<p>INSTALLED_APPS = [</p>
<p>    'questions.apps.QuestionsConfig'</p>
               <p>]</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><strong>13. Front end files.</strong></p>
<p> Create a directory named <appname>\templates</p>
 <p>Keep all html and css file inside <appname>\templates</p>
 <p>&nbsp;</p>
<p><strong>14.  Copy base html for Bootstrap depending </strong> on CSS style you like, make a base.html and keep inside <appname>\templates</p>
<p>&nbsp;</p>
<p><strong>15.  Inside HTML file,start with </strong></p>
<p>     a. {'%' extends 'base.html''%'}</p>
<p>     b. {'%' block content'%'}</p>
<p>     c.  keep all html inside 'block content'</p>
<p>     d. {'%' endblock '%'}</p>
<p>&nbsp;</p>
<p><strong>16.  Use of Django form for data input and automatic field validation</strong></p>
               <p>   1. Create a class in <appname>/forms.py</p>
               <p>   2. Import the form class in to view file and send to HTML file to render.</p>
               <p>   3. Inside the HTML file use the form as ' {{' form_name '}}'</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
           </div>
         </div>
        <div class="card-footer text-muted">
              Had enough ? Click to exit  <a href="/admin/" class="btn btn-primary">Exit Test</a>
        </div>
    </div>
</div>





<pre><span>import </span>os<br /><span>import </span>datetime<br /><span>import </span>re<br /><br /><span>def </span><span>print_file_dir_name</span>(root_path):<br />    paths = os.listdir(root_path)<br />    <span>for </span>path <span>in </span>paths:<br />        <span>if </span>os.path.isdir(path):<br />            print_file_dir_name(path)<br />        <span>else</span>:<br />            <span>print</span>(path)<br />testpath = os.path.expanduser(<span>'~'</span>)<br /><br /><span>def </span><span>print_date</span>():<br />    now = datetime.datetime.now<br />    now = <span>lambda </span>: datetime.datetime(<span>2019</span><span>,</span><span>10</span><span>,</span><span>16</span>)<br />    <span>print</span>(<span>f'</span><span>{</span>now<span>}</span><span>'</span>)<br /><br /><span>def </span><span>validateEmail</span>():<br />    regex  = <span>'[0-9a-zA-Z]+@[a-zA-Z]+\.([a-z][a-z][a-z]|co\.[a-z][a-z])+$'<br /></span><span>    </span>email = <span>'andr@sde.co.we'<br /></span><span>    </span><span>if </span>re.search(regex<span>,</span>email) :<br />         <span>print</span>(<span>f' Valid email </span><span>{ </span>email<span>} </span><span>'</span>)<br />    <span>else</span>:<br />        <span>print</span>(<span>f' Invalid email </span><span>{</span>email<span>} </span><span>'</span>)</pre>



<pre><span>from </span>django.test <span>import </span>TestCase<span>, </span>Client<br /><span>from </span>django.urls <span>import </span>reverse<br /><span>from </span>. models <span>import </span>Candidate<br /><span>from </span>django.contrib.auth.models <span>import </span>User<br /><span>from </span>django.http <span>import </span>response<br /><span># Create your tests here.<br /></span><span><br /></span><span>class </span>SurveyViewTest(TestCase):<br />    <span>def </span><span>setUp</span>(<span>self</span>):<br />        <span>self</span>.user = User.objects.creat_candidate(<span>username</span>=<span>'djangotesttestuser'</span><span>,</span><span>email</span>=<span>'djangotesttest@gmail.com'</span><span>,</span><span>password</span>=<span>'password'</span>)<br />        Candidate.objects.create(<span>candidate_name</span>=<span>'testcandidateA'</span><span>, </span><span>candidate_email</span>=<span>'testcandidateA@gmail.com'</span>)<br />        Candidate.objects.create(<span>candidate_name</span>=<span>'testcandidateB'</span><span>, </span><span>candidate_email</span>=<span>'testcandidateB@gmail.com'</span>)<br />        <span>self</span>.client = Client()<br />        <span>self</span>.url = reverse(<span>'starttest'</span>)<br /><br />    <span>def </span><span>test_get</span>(<span>self</span>):<br />        response =<span>self</span>.client.get(<span>self</span>.url)<br />        <span>self</span>.assertEquals(response.status_code<span>, </span><span>200</span>)<br />        data = response.context_data(<span>'starttest'</span>)<br />        <span>self</span>.assertEquals(<span>len</span>(data)<span>,</span><span>9</span>)<br />        <span>self</span>.assertEquals(<span>len</span>(data[<span>0</span>])<span>, </span><span>5</span>)</pre>



<p><strong>Numeric File permissions: </strong></p>
<p>0 No Permission---&nbsp;</p>
<p>1Execute--x&nbsp;</p>
<p>2Write-w-&nbsp;</p>
<p>3Execute + Write-wx&nbsp;</p>
<p>4Readr--&nbsp;</p>
<p>5Read + Executer-x&nbsp;</p>
<p>6Read +Writerw-&nbsp;</p>
<p>7Read + Write +Executerwx&nbsp;</p>
<p><br></p>
<p>Monitoring Command&nbsp;</p>
<p>Top&nbsp;</p>
<p>VmStat lsof - list of all open file and processes&nbsp;</p>
<p>Tcpdump (tcpdump -i eth0 )- network packet analyzer&nbsp;</p>
<p>Netstat (netstat -a | more)&nbsp;</p>
<p>Htop - Process Monitoring&nbsp;</p>
<p>Iotop - Monitoring Disk I/O&nbsp;</p>
<p>Iostat &ndash; Input/Output Statistics&nbsp;</p>
<p>IPTraf &ndash; Real Time IP LAN Monitoring&nbsp;</p>
<p>Psacct or Acct &ndash; Monitor User Activity&nbsp;</p>
<p>NetHogs &ndash; Monitor Per Process Network Bandwidth&nbsp;</p>
<p>iftop &ndash; Network Bandwidth Monitoring&nbsp;</p>
<p><br></p>
<p><strong>Ports:</strong> Telnet - 23&nbsp; &nbsp; SMTP - 25&nbsp; &nbsp; FTP - 20&nbsp; &nbsp; IMAP - 143&nbsp; &nbsp;RDP - 3389&nbsp; &nbsp;SSH -22</p>



Docker



| 
@ ,
~                                                                             
~     





docker --version
docker-compose --version
> pull mysql from docker hub
  docker pull mariadb:10.0.25

> Display images
  docker images

> Create database volume and run  /user/local/data
  docker run -d -v /user/local/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 --name my_mariadb mariadb:10.0.25

> Display volume
  docker volume ls

> compose file validation 
 docker-compose config 

> destroy all volumes
  docker-compose down

> Link containers
  docker run -d --name my_wordpress --link my_mariadb:mysql-p 8080:80  wordpress:version

> Display all containers including not running
  docker ps -a
> Remove docker images from local installation
  docker rm container_name
> Look inside a container
  docker run exec -ti container_name /bin/sh


  Basic compose file:(docker-compose.yml)
  version :'3'
  services:
    service_name:
       container_name: <my_web_container-name>
       build:
           context: .
           target: development
           args:
             - <build_args>:<build_args_values>
       image:<image_name_produced_by_the_build>
       env_file:
         - .env.txt
       environment:
         - <variable_name>=<variable>
       ports:
         - 8080:80
       network:
         - <network_name>
       volumes:
         - <volume_name>:/path/inside/container

  networks:
     network_name:
        driver: bridge
  volumes:
        volume_name:              


> build and run from docker-compose.yml
  docker-compose up -d

> verify docker logs
  docker-compose logs -f
  docker-compose logs -f <container_name>

> Build command
  docker-compose build ( if images need to be build.)  

> Display network list
  docker network ls

> Inspect a network
  docker networl inspect <network_name>

> Remove unused network
  docker network prune

> Stop all containers
  docker-compose stop

> Run contailer without modifyin the running containers (No port mapping)
  docker-compose run <container_name>

> Scalling
  docker-compose up -scale <container_name>=3  (will need a load balancer or there will be port conflict)

1. Docker states and Docker Events are used to monitoring docker in the production environment.
2. Memory-swap is a modified flag
3. What are the command to control Docker with Systemd


nginx proxy.conf :

service {
    listen 80;
    resolver 127.0.0.11;
    set $upstream http://app;
location / {
     proxy_pass $upstream;
    }
}

nginx proxy:

FROM nginx:alpine
RUN rm -r /etc/nginx/conf.d/
COPY proxy.conf /etc/nginx/conf.d
EXPOSE 80

docker-compose:(LB)
version : '3.2'

services:
    web:
      image: lb2-app

      links:
        - database
        - proxy

    database:
      image: redis

    proxy:
      image: proxy
      ports:
        - 80:85







