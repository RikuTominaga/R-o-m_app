from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        session['defict'] = request.form['defict']

        #安全係数sfについて
        if request.form['defict'] == '0.1%':
            sf = 3.10
        elif request.form['defict'] == '1.0%':
            sf = 2.33
        elif request.form['defict'] == '2.0%':
            sf = 2.06
        elif request.form['defict'] == '5.0%':
            sf = 1.65
        elif request.form['defict'] == '10.0%':
            sf = 1.29
        elif request.form['defict'] == '20.0%':
            sf = 0.85
        elif request.form['defict'] == '3.0%':
            sf = 0.53

        print(f"安全係数sf={sf}")

        span1 = int(request.form['span1'])
        span2 = int(request.form['span2'])
        span3 = int(request.form['span3'])
        span4 = int(request.form['span4'])
        span5 = int(request.form['span5'])
        span6 = int(request.form['span6'])
        span7 = int(request.form['span7'])
        span8 = int(request.form['span8'])
        
        stock = int(request.form['stock'])
        no_in = int(request.form['no-in'])

        #標準偏差sdについて
        list =[]
        list += [span1, span2, span3, span4, span5, span6, span7, span8]
        print(list)
        
        import numpy as np
        sd = round(np.std(list),2)
        print(f"標準偏差sd={sd}")

        #安全在庫ssについて
        import math
        ss = math.ceil(sf * sd * 2.83)
        print(f"安全在庫ss={ss}")

        #発注量Qについて
        SUM = span1 + span2 + span3 + span4 + span5 + span6 + span7 + span8 
        Q = SUM + ss - no_in - stock
        print(f"消費量合計:{SUM}")
        print(f"発注量Q={Q}")

        session['SUM'] = SUM
        session['Q'] = Q
        session['sd'] = sd
        session['ss'] = ss

        return redirect(url_for('output'))
    return render_template('input.html')

@app.route('/output')
def output():
    return render_template('output.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
        



