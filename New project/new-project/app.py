from flask import Flask, render_template, request, redirect, url_for, send_file
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def resume_form():
    return render_template('resume_form.html')

@app.route('/preview', methods=['POST'])
def resume_preview():
    data = request.form
    return render_template('resume_preview.html', data=data)

@app.route('/download', methods=['POST'])
def download_resume():
    data = request.form
    html = render_template('resume_preview.html', data=data)
   

   

if __name__ == '__main__':
    app.run(debug=True)
