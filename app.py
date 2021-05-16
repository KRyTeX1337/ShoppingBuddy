import main
import json
import Questions

from flask import Flask, render_template, request

app = Flask(__name__)

def ComplexHandler(Obj):
    if hasattr(Obj, 'jsonable'):
        return Obj.jsonable()
    else:
        raise TypeError('Object of type %s with value of %s is not JSON serializable' % (type(Obj), repr(Obj)))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/getAnswer")
def get_bot_response():
    #userInput = request.args.get('msg')
    #return str(main.get_response(userInput))
    answers = main.formatRequest(request.args.get('msg'))
    return str(main.get_response(answers))

@app.route("/getQuestions")
def get_questions():
    questions = Questions.Questions()
    questions.createQuestions()
    return json.dumps(questions.__dict__, default=ComplexHandler, ensure_ascii=False)

if __name__ == "__main__":
    app.run()