from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hellow Folks!<br>নমস্কাৰ &#128591;<h1><p> I am Biraj Khound. I have done my masters in computer application from <a href="https://jecassam.ac.in/">Jorhat Engineering College.</a> During my masters i have done a web project named <a href="https://assamesedictionary.in/">Assamese Dictionary</a> under the supervision of Dr. Dhrubajyoti Baruah sir. This API is a part of that project. Here, we have implemented a function named assamese_soundex. To, know more about assamese soundex you can read this <a href="http://127.0.0.1:5000/assamese_soundex/%22%E0%A6%A8%E0%A6%AE%E0%A6%B8%E0%A7%8D%E0%A6%95%E0%A6%BE%E0%A7%B0%22">paper</a> by Dr. Dhrubajyoti Baruah and to try out this API you need to follow the <i><u>/assamese_soundex/(the assamese word whose soundex is you are finding)</u></i><p><br><h1>Thank you,<br>ধন্যবাদ 😊<h1>'
@app.route('/assamese_soundex/<string:word>')
def assamese_soundex(word):
  """ This function generates an Assamese soundex code for a given word. """
  soundex = ""
  for letter in word:
    if letter == "প":
      soundex += "P"
    elif letter == "ফ":
      soundex += "F"
    elif letter in ("ব", "ৱ"):
      soundex += "B"
    elif letter == "ভ":
      soundex += "V"
    elif letter in ("ত", "ট", "ৎ"):
      soundex += "T"
    elif letter in ("থ", "ঠ"):
      soundex += "1"
    elif letter in ("দ", "ড"):
      soundex += "D"
    elif letter in ("ধ", "ঢ"):
      soundex += "2"
    elif letter == "ক":
      soundex += "K"
    elif letter == "খ":
      soundex += "3"
    elif letter == "গ":
      soundex += "G"
    elif letter == "ঘ":
      soundex += "4"
    elif letter in ("চ", "ছ"):
      soundex += "C"
    elif letter in ("য", "জ"):
      soundex += "J"
    elif letter == "ঝ":
      soundex += "5"
    elif letter in ("শ", "ষ", "স"):
      soundex += "S"
    elif letter in ("হ", "ঃ", ":"):
      soundex += "H"
    elif letter == "ম":
      soundex += "M"
    elif letter in ("ন", "ণ"):
      soundex += "N"
    elif letter in ("ঙ", "ং"):
      soundex += "6"
    elif letter in ("ৰ", "ড়", "ঢ়"):
      soundex += "R"
    elif letter == "ল":
      soundex += "L"
    elif letter in ("য়", "ঞ"):
      soundex += "Y"
    elif letter in ("্", "্‌"):
      soundex += "X"
    elif letter == "অ":
      soundex += "A"
    elif letter in ("ঋ", "ৃ"):
      soundex += "W"
    elif letter == "া":
      soundex += "7"
    elif letter == "আ":
      soundex += "7"
    elif letter in ("ই", "ি", "ঈ", "ী"):
      soundex += "I"
    elif letter in ("উ", "ু", "ঊ", "ূ", "ও", "ো"):
      soundex += "U"
    elif letter in ("এ", "ে"):
      soundex += "E"
    elif letter in ("ঐ", "ৈ"):
      soundex += "8"
    elif letter in ("ঔ", "ৌ"):
      soundex += "9"
    else:
      soundex += "0"

  # Replacements
  soundex = soundex.replace("XX", "X")
  soundex = soundex.replace("0", "")
  soundex = soundex.replace("HXJ", "Q")
  soundex = soundex.replace("JXJ", "Q")
  soundex = soundex.replace("KXS", "3")
  soundex = soundex.replace("JXY", "Z")
  soundex = soundex.replace("GXJ", "Z")
  soundex = soundex.replace("YXC", "NC")
  soundex = soundex.replace("YXJ", "NJ")

  result = { 
    "given word" : word,
    "assamese_soundex_output" : soundex,
    }

  return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)