from flask import Flask,request,render_template
import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt

from PIL import Image

app=Flask(__name__,template_folder='template')
pickle_in=open("m_model.pkl","rb")
lr_model=pickle.load(open("m_model.pkl","rb"))
train = pd.read_csv('train.csv')
price=train['toxic']
lens = train.comment_text.str.len()
df1=pd.read_csv("submission.csv")
val1=df1.loc[0,'id']
val2=df1.loc[0,'toxic']

val4=df1.loc[0,'obscene']
val5=df1.loc[0,'threat']
val6=df1.loc[0,'insult']
#@app.route('/')
def hello():
        return  "<h1>hello world</h1>"

@app.route('/')
def charTest():
	return render_template('un.html',name1=val1,name2=val2,name4=val4,name5=val5,name6=val6)

if __name__=="__main__":
        app.run(host='127.0.0.1',port=4413,debug=True) 
