from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)


@app.route("/process-csv", methods=["POST"])
def process_csv():
    if "file" not in request.files:
        return "No file part", 400

    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    try:
        df = pd.read_csv(file)
    except Exception as e:
        return "Failed to read CSV file", 400

    column_totals = df.sum().tolist()
    column_averages = df.mean().tolist()

    return jsonify(
        {
            "header": df.columns.tolist(),
            "column_totals": column_totals,
            "column_averages": column_averages,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
