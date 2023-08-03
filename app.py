from flask import Flask, render_template, request
import pandas as pd
import pickle
import sklearn

file = open("dp_model.pickle", "rb")
modle = pickle.load(file)

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("base.html")

@app.route("/index.html", methods = ["GET", "POST"])
def predictor():
    
    if request.method == "POST":
        
        
        
        features=['age','Gender','self_employed','family_history','work_interfere','no_employees','remote_work',
                  'tech_company','benefits','care_options','wellness_program','seek_help','anonymity','leave',
                  'mental_health_consequence','phys_health_consequence','coworkers','supervisor','mental_health_interview',
                  'phys_health_interview','mental_vs_physical','obs_consequence']
        
        x= {col: 0 for col in features}
        print(x)
        
        x['age'] = int(request.form.get('age'))
        x['Gender'] = int(request.form.get('gender'))
        x['self_employed'] = int(request.form.get('self_employed'))
        x['family_history'] = int(request.form.get('family_history'))
        x['work_interfere'] = int(request.form.get('work_interfere'))
        x['no_employees'] = int(request.form.get('no_employees'))
        x['remote_work'] = int(request.form.get('remote_work'))
        x['tech_company'] = int(request.form.get('tech_company'))
        x['benefits'] = int(request.form.get('benefits'))
        x['care_options'] = int(request.form.get('care_options'))
        x['wellness_program'] = int(request.form.get('wellness_program'))
        x['seek_help'] = int(request.form.get('seek_help'))
        x['anonymity'] = int(request.form.get('anonymity'))
        x['leave'] = int(request.form.get('leave'))
        x['mental_health_consequence'] = int(request.form.get('mental_health_consequence'))
        x['phys_health_consequence'] = int(request.form.get('phys_health_consequence'))
        x['coworkers'] = int(request.form.get('coworkers'))
        x['supervisor'] = int(request.form.get('supervisor'))
        x['mental_health_interview'] = int(request.form.get('mental_health_interview'))
        x['phys_health_interview'] = int(request.form.get('phys_health_interview'))
        x['mental_vs_physical'] = int(request.form.get('mental_vs_physical'))
        x['obs_consequence'] = int(request.form.get('obs_consequence'))

        df = pd.DataFrame(x, index=[1])
        x_input = df.values
        print(x)
        print(df)
        print(x_input)
        

        output = modle.predict(x_input)[0]
        if output==1:
            text='Yes you should go for counseling'
        else:
            text="No you don't need to go anywhere just be happy"
        print(output)
        return render_template("index.html", prediction_text=text)
        
        
    return render_template("index.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)