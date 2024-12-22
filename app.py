#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask, render_template, request, redirect
import pymongo

app = Flask(__name__)

# Connect to MongoDB
# client = pymongo.MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=5000)
client = pymongo.MongoClient("mongodb+srv://jstshile:7Nl4VWJ9yuxo6j5o@toyecluster.zuzx2.mongodb.net/", serverSelectionTimeoutMS=5000)

db = client['survey_data']
collection = db['user_expenses']

@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        data = {
            'age': request.form['age'],
            'gender': request.form['gender'],
            'total_income': float(request.form['income']),
            'expenses': {
                'utilities': float(request.form['utilities']),
                'entertainment': float(request.form['entertainment']),
                'school_fees': float(request.form['school_fees']),
                'shopping': float(request.form['shopping']),
                'healthcare': float(request.form['healthcare'])
            }
        }
        collection.insert_one(data)
        return redirect('/')
    return render_template('survey.html')

if __name__ == '__main__':
    app.run(debug=False)


# In[ ]:




