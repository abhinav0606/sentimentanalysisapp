from flask import Flask,render_template,request
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from collections import Counter
import matplotlib
# from dh import hanging
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def hello():
    return render_template("main.html")
@app.route("/wait",methods=['GET','POST'])
def wait():
    text = request.form.get('name')
    matplotlib.use("Agg")
    text = text.lower().replace("\n", "").replace("’", "").replace("”", "")
    text = text.translate(str.maketrans("", "", string.punctuation))
    def sentiments(text):
        return SentimentIntensityAnalyzer().polarity_scores(text)
    token_words = word_tokenize(text)
    clean_words = []
    for i in token_words:
        if i not in stopwords.words("english"):
            clean_words.append(i)
    d = []
    with open("emotion.txt", "r") as f:
        for i in f:
            clean = i.replace("\n", "").strip().replace("'", "").replace(" ", "").replace(",", "")
            t, emotion = clean.split(":")
            if t in clean_words:
                d.append(emotion)
    y = Counter(d)
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.bar(y.keys(),y.values())
    # plt.show(
    fig.savefig("/home/abhinav/PycharmProjects/SentimentFlask/static/i.png")
    w = sentiments(text)
    fig1=plt.figure()
    ax1=fig1.add_subplot(111)
    ax1.bar(w.keys(),w.values())
        # plt.show()
    fig1.savefig("/home/abhinav/PycharmProjects/SentimentFlask/static/j.png")
    return render_template("wait.html")
@app.route("/analyze",methods=['GET','POST'])
def analysis():
    return render_template("analysis.html")
app.run(debug=True)