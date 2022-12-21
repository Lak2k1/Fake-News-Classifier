from flask import *
app = Flask(__name__) 

import pickle
with open('fknews_pkl', 'rb') as f:
    fk=pickle.load(f)

@app.route('/') 
def home():  
    return render_template("layout.html",pr='')

@app.route('/pred',methods=['GET','POST'])   
def pred():
    title=[request.form['title']]
    if((fk[0].predict(fk[1].transform(title))[0])==1):
        return render_template("layout.html",pr="Unreliable")
    else:
        return render_template("layout.html",pr="Reliable")

if __name__ =='__main__':  
    app.run(debug = True)