import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    a=int(jsonObj['a'])
    b=int(jsonObj['b'])
    c=int(jsonObj['c'])
    d=int(jsonObj['d'])
    k=b
    b=a
    a=k
    response+="<b> The new value of a is <b>"+str(a)+" The new value of b is "+str(b)+"</b><br>"
    response+="<b> The new value of c is <b>"+str((c^d)^c)+" The new value of d is "+str((c^d)^d)+"</b><br>" 
    a = 20
    b = 10
    c = 15
    d = 5
    e1=(a + b) * c // d >>1
    e2=(a + b * c) // d>>1
    e3=(a + b) * (c // (d>>1))
    e4=a + (b * c) // d>>1
    response+="<b> Value of e1 is <b>"+str(e1)+"</b><br>"   
    response+="<b> Value of e2 is <b>"+str(e2)+"</b><br>"
    response+="<b> Value of e3 is <b>"+str(e3)+"</b><br>"
    response+="<b> Value of e4 is <b>"+str(e4)+"</b><br>" 
        
    
    	    
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
