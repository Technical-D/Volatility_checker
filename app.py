from flask import Flask, request, jsonify, render_template
from calculation import calculate_volatility
import os

app = Flask(__name__)

# Index page to show form to upload csv file
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/compute_volatility', methods=['POST'])
def compute_volatility():
    """
    This Function handle the uploading of datasetand save them to desired folder.
    It return the result in json format.
    """
    try:
        file = request.files['file']

        # Creating folder to save csv files
        upload_folder = os.path.join(os.getcwd(), 'uploaded_datasets')
        os.makedirs(upload_folder, exist_ok=True)

        # Saving the file to a specific location
        file_path = os.path.join(upload_folder, file.filename)
        file.save(file_path)

        # Checking if the file is a CSV file
        if not file.filename.endswith('.csv'):
            return jsonify({"error": "Uploaded file must be a CSV file."}), 400
        
        result = calculate_volatility(file_path)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True)