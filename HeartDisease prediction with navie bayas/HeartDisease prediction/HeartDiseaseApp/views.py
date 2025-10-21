from django.shortcuts import render
import pymysql
from sklearn.naive_bayes import GaussianNB
import pandas as pd

# -------------------------
# Pages
# -------------------------
def index(request):
    return render(request, 'index.html')

def Login(request):
    return render(request, 'Login.html')

def Register(request):
    return render(request, 'Register.html')

def Predict(request):
    return render(request, 'Predict.html')


# -------------------------
# Heart Disease Prediction
# -------------------------
def PredictHeartCondition(request):
    if request.method == 'POST':
        # Get form data
        age = request.POST.get('age', '')
        gender = request.POST.get('gender', '')
        cp = request.POST.get('cp', '')
        bps = request.POST.get('trestbps', '')
        chol = request.POST.get('chol', '')
        fbs = request.POST.get('fbs', '')
        ecg = request.POST.get('restecg', '')
        thalach = request.POST.get('thalach', '')
        exang = request.POST.get('exang', '')
        oldpeak = request.POST.get('oldpeak', '')
        slope = request.POST.get('slope', '')
        ca = request.POST.get('ca', '')
        thal = request.POST.get('thal', '')

        # Save test data
        data = 'age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal\n'
        data += f"{age},{gender},{cp},{bps},{chol},{fbs},{ecg},{thalach},{exang},{oldpeak},{slope},{ca},{thal}"
        with open('testdata.txt', 'w') as file:
            file.write(data)

        # Train model
        train = pd.read_csv('dataset')
        X = train.values[:, 0:13]
        Y = train.values[:, 13]

        cls = GaussianNB()
        cls.fit(X, Y)

        # Predict
        test = pd.read_csv('testdata.txt')
        test_X = test.values[:, 0:13]
        y_pred = cls.predict(test_X)

        result = ''
        for i in range(len(test_X)):
            if str(y_pred[i]) == '0.0':
                result = f"{test_X[i]}<br/>Result = No Heart Disease Detected"
            elif str(y_pred[i]) == '1.0':
                result = f"{test_X[i]}<br/>Result = Heart Disease Detected"

        return render(request, 'Result.html', {'data': result})


# -------------------------
# User Signup
# -------------------------
def Signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        contact = request.POST.get('contact', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')

        try:
            connection = pymysql.connect(
                host='localhost', port=3306,
                user='root', password='',  # XAMPP default
                database='HeartDisease', charset='utf8'
            )
            cursor = connection.cursor()
            query = "INSERT INTO register(username,password,contact,email,address) VALUES(%s,%s,%s,%s,%s)"
            cursor.execute(query, (username, password, contact, email, address))
            connection.commit()

            if cursor.rowcount == 1:
                context = {'data': 'Signup Process Completed'}
            else:
                context = {'data': 'Error in signup process'}

        except Exception as e:
            context = {'data': f'Error: {str(e)}'}

        finally:
            cursor.close()
            connection.close()

        return render(request, 'Register.html', context)


# -------------------------
# User Login
# -------------------------
def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        utype = 'none'

        try:
            connection = pymysql.connect(
                host='localhost', port=3306,
                user='root', password='',  # XAMPP default
                database='HeartDisease', charset='utf8'
            )
            with connection:
                cursor = connection.cursor()
                cursor.execute("SELECT username, password FROM register WHERE username=%s AND password=%s", (username, password))
                row = cursor.fetchone()
                if row:
                    utype = 'success'

        except Exception as e:
            utype = 'none'

        if utype == 'success':
            with open('session.txt', 'w') as f:
                f.write(username)
            context = {'data': f'Welcome {username}'}
            return render(request, 'UserScreen.html', context)
        else:
            context = {'data': 'Invalid login details'}
            return render(request, 'Login.html', context)
