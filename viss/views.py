from django.shortcuts import render
import time
from datetime import datetime

# Create your views here.

def result(request,result_id):
    dt = datetime.now()
    s=str(dt.microsecond)

    #result_id에 따라서 respon값을 달리해서 context변수 전송해주기 
    respon={"action":"get", "requestId":result_id,"value":"2372","timestamp":s}
    context={"result":respon}
    return render(request,'viss/result.html',context)