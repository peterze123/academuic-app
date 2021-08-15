from datetime import datetime
from flask import Blueprint, redirect, render_template, url_for, flash, session, request
from questions import q1, Question, Answer


#dummy questions and answers
qs = [q1]

bp = Blueprint('forum', __name__)

@bp.route('/forum/', methods=['POST', 'GET'])
@bp.route('/forum/<int:ansid>', methods=['POST', 'GET'])
def forum(ansid:int = None):
    global qs
    
    if request.method == 'GET':
        return render_template('forum.html', questions=qs)
    else:
        if ansid is None:
            #this is a question
            query = request.form['question']
            q = Question(query)
            qs.append(q)
        else:
            #this is an answer
            q: Question = qs[ansid]
            print(request.form)
            content = request.form['answer']
            ans = Answer('Abhishek', 1, content, submittedon=datetime.now())
            q.add_answer(ans)
        return redirect('/forum')