from flask import Flask, render_template, request
import os
from grammar import read_grammar
from pda import build_pda, draw

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/graphs'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    cfg_text = '''S
a,b
S -> a S b | ε'''
    graph_path = None
    test_result = None
    test_string = ''
    error = None

    if request.method == 'POST':
        cfg_text = request.form['cfg']
        test_string = request.form.get('test_string', '')
        
        try:
            start, terms, prods = read_grammar(cfg_text)
            delta = build_pda(start, terms, prods)
            
            
            graph_path = os.path.join(app.config['UPLOAD_FOLDER'], 'pda_graph')
            draw(delta, graph_path)
            graph_path = graph_path + '.png'
            
        except ValueError as e:
            error = str(e)
    
    return render_template('index.html', 
                         cfg_text=cfg_text,
                         graph_path=graph_path,
                         test_string=test_string,
                         test_result=test_result,
                         error=error)

if __name__ == '__main__':
    app.run(debug=True)