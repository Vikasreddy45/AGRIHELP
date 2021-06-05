from flask import Flask,render_template,request
import numpy as np
import pickle

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home() :
    return render_template('main.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    crops=['wheat','mungbean','Tea','millet','maize','lentil','jute','cofee','cotton','ground nut','peas','rubber','sugarcane','tobacco','kidney beans','moth beans','coconut','blackgram','adzuki beans','pigeon peas','chick peas','banana','grapes','apple','mango','muskmelon','orange','papaya','watermelon','pomegranate']
    cr='rice'
    predictions = model.predict(final_features)
    count=0
    for i in range(0,30):
        if(predictions[0][i]==1):
            c=crops[i]
            count=count+1
            break
        i=i+1
    if(count==0):
       final_pred=cr
    else:
        final_pred=c

    return render_template('main.html', prediction_text="{}".format(final_pred))


if __name__ == "__main__" :
    app.run(debug = True)