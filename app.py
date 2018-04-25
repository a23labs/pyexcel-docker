from flask import Flask, request, jsonify
import flask_excel as excel
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Know Your Rights!'


@app.route("/upload", methods=['GET', 'POST'])
@cross_origin()
def upload_file():
    if request.method == 'POST':
        return jsonify({"result": request.get_records(field_name='file')})
        #return jsonify(excel.ExcelRequest.get_array())
    return '''
    <!doctype html>
    <title>Upload an excel file</title>
    <h1>Excel file upload (xls, xlsx, csv only)</h1>
    <form action="" method=post enctype=multipart/form-data><p>
    <input type=file name=file><input type=submit value=Upload>
    </form>
    '''


@app.route("/download", methods=['GET'])
def download_file():
    return excel.make_response_from_array([[1, 2], [3, 4]], "csv")


@app.route("/export", methods=['GET'])
def export_records():
    return excel.make_response_from_array([[1, 2], [3, 4]], "csv", file_name="export_data")


# insert database related code h

if __name__ == '__main__':
    app.run()
