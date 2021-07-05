from flask import Flask,render_template,request,json
import datetime
tim1 = []
flag = [0,0]

app = Flask(__name__)
def time_obj(t):
    if t != "":
        date_h = datetime.datetime.now().date()
        t = t.split(":")
        t = datetime.time(int(t[0]),int(t[1]),0)
        t = datetime.datetime.combine(date_h,t)
        return t
    else :
        return None
@app.route('/',methods=["get","post"])
def hello_world():
    global tim1 
    global flag
    if request.method=="GET":
        return render_template("page.html")
    else:
        data=json.loads(request.data.decode('utf-8'))
        for i in range(1,5):
            ind = 'time'+str(i)
            #print(ind)
            t = time_obj(data[ind])
            if t != None:
                tim1.append(t)
        tim2 = []
        tim = datetime.datetime.now()
        for i in range(1,5):
            if len(tim1) == 0:
                break
            mx = min(tim1)
            tim2.append(mx)
            tim1.remove(mx)
        for i in tim2:print(i)
        return ""  
if __name__ == "__main__":
    app.run(debug= True,host ='0.0.0.0')