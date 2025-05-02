from django.shortcuts import render

import mysql.connector as sql

# Create your views here.


def insertqry():
	qry = 'INSERT INTO log( name, email, pas) VALUES (%s,%s,%s)'
	return qry

def datainsert(n,e,p):

	con = sql.connect(host='localhost',user='root',password='',database='reg',port=3306)
	db = con.cursor()

	db.execute(insertqry(),(n,e,p,))
	con.commit()

	db.close()
	con.close()
	print('Data inserted successfully')



def signup(request):

	if request.method == "POST":
		n = request.POST.get('name')
		e = request.POST.get('email')
		p = request.POST.get('password')

		print(n,e,p)

		if n!=None and e!=None and p!=None:
			datainsert(n,e,p)

	return render(request,'signup.html')
