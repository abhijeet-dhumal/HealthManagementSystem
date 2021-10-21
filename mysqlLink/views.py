from django.http.response import HttpResponse
from django.shortcuts import render
import mysql.connector as connector
# for flash message
from django.contrib import messages
   

# Create your views here.
def home(request):
    if request.method=='POST':
        # receive all input given to webpage
        usernameadd =request.POST.get('usernameAdd')
        useradd =request.POST.get('userAdd')
        userdelete =request.POST.get('userDelete')
        sqlPassword =request.POST.get('sqlPassword')
        username =request.POST.get('username')
        exercise =request.POST.get('exercise')
        diet =request.POST.get('diet')
        description =request.POST.get('description')
        insertAct = request.POST.get('insertAct')
        deleteAct = request.POST.get('deleteAct')
        updateAct = request.POST.get('updateAct')
        fetchAll=request.POST.get('fetchAll')
        print(useradd,username,exercise,diet,description,fetchAll)

        # fetch data of selected user 
        def fetch_user_activityData():
            query="select * from todo_activity where userName='{}'".format(username)
            cur=mydb.cursor()
            cur.execute(query)
            return cur

        # fetch all user data 
        def fetch_all_usersData():
            query="select * from todo_activity"
            cur=mydb.cursor()
            cur.execute(query)
            return cur
            
        if (exercise=='option1') :
                todoname = 'Exercise'
        elif(diet=='option2'):
                todoname = 'Diet'

        # user_activity insertion 
        def insert_user():
            query="insert into userclient(username) values('{}')".format(usernameadd)
            cur=mydb.cursor()
            cur.execute(query)
            mydb.commit() 

        # user_activity insertion 
        def insert_activity():
            if (exercise=='option1') :
                activityid = 1
                todoname = 'Exercise'
                query="insert into todo_activity(todoid,username,todoName,date,todo_act) values({},'{}','{}',now(),'{}')".format(int(activityid),username,todoname,description)
                cur=mydb.cursor()
                cur.execute(query)
                mydb.commit() 
            elif(diet=='option2'):
                activityid = 2
                todoname = 'Diet'
                query="insert into todo_activity(todoid,username,todoName,date,todo_act) values({},'{}','{}',now(),'{}')".format(int(activityid),username,todoname,description)
                cur=mydb.cursor()
                cur.execute(query)
                mydb.commit() 
    
        # user_activity_updation
        def update_user_activity():
            if (exercise=='option1') :
                activityid = 1
                todoname = 'Exercise'
                query = "update todo_activity set todo_act ='{}' where userName = '{}' and todoName = '{}' ".format(str(description),username,todoname)
                cur=mydb.cursor()
                cur.execute(query)
                mydb.commit()

            elif (diet=='option2') :
                activityid = 2
                todoname = 'Diet'
                query = "update todo_activity set todo_act ='{}' where userName = '{}' and todoName = '{}' ".format(str(description),username,todoname)
                cur=mydb.cursor()
                cur.execute(query)
                mydb.commit()

        # userDeletion
        def delete_user():
            query = "delete from userclient where username='{}' ".format(usernameadd)
            cur=mydb.cursor()
            cur.execute(query)
            mydb.commit()

        # user_activity_deletion
        def delete_user_activity():
            query = "delete from todo_activity where todo_act = '{}' and userName='{}' ".format(str(description),username)
            cur=mydb.cursor()
            cur.execute(query)
            mydb.commit()

        # check password  
        try:
            mydb = connector.connect(host='localhost',port='3305',user='root',password='{}'.format(sqlPassword),database='python_database')
            if(sqlPassword=="Abhijeet652@"):
                # link webpage with mysql 
                messages.success(request,'MySQL connected successfully !!!')
                
                # allrows=fetch_all_usersData()
            else:
                messages.warning(request,'Wrong MySQL password !!!') 
          
        except Exception as e:
            messages.warning(request,'Wrong MySQL password !!!') 
            return HttpResponse(f"<h1>Wrong Mysql password !!!</h1>{e}")
            
        if(insertAct=='on'):
            insert_activity()

        if(deleteAct=='on'):
            delete_user_activity()

        if(useradd=='on'):
            insert_user()

        if(userdelete=='on'):
            delete_user()
        
        if(updateAct=='on'):
            update_user_activity()

        if (fetchAll=='on'):
            allrows=fetch_all_usersData()
            print(allrows)
            context = {'allrows':allrows}    
            return render(request, 'home.html',context)
        else:
            rows=fetch_user_activityData()
            context = {'rows':rows}    
            return render(request, 'home.html',context)

    context={}
    return render(request, 'home.html',context)       

    

