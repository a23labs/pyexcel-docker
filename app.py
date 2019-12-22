from flask import Flask, request, jsonify
import flask_excel as excel

app = Flask(__name__)
excel.init_excel(app)


@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        return jsonify({"result": request.get_records(field_name='file')})
    return '''
    <!doctype html>
    <title>Upload an excel file here</title>
    <h1>Excel file upload (csv, tsv, csvz, tsvz, xls, xlsx only)</h1>
    <form action="" method=post enctype=multipart/form-data><p>
    <input type=file name=file><input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0')
