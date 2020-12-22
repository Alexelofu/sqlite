import pandas as pd
from flask import Flask
app = Flask(__name__)

@app.route("/head", methods = ['POST', 'GET'])
def head():
    df = pd.read_csv('http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv')
    return df.head().to_html()

@app.route("/tail", methods = ['POST', 'GET'])
def tail():
    df = pd.read_csv('http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv')
    return df.tail().to_html()


@app.route("/describe", methods = ['POST', 'GET'])
def describe():
    df = pd.read_csv('http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv')
    return df.describe().to_html()

    
if __name__ == "__main__":
    app.run() 



# @app.route('/view_data', methods = ['POST'])
# def get_head_tail_info():

#     # get the cleaned dataset
#     read_file = pd.read_csv('http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv')

#     # get the form submit button whose name is head and value is head
#     if request.form.get("head") == "head":
#         # show just the head
#         return read_file.head().to_html()
        
#     # get the form submit button whose name is tail and value is tail
#     elif request.form.get("tail") == "tail":
#         # show just the tail
#         return read_file.tail().to_html()

#     # get the form submit button whose name is info and value is info
#     elif request.form.get('info') == "info":
#         # return the dataset description
#         return read_file.describe().to_html()