from flask import Blueprint, request, jsonify
from services.jsfetcher import jsfetcher
from services.generator import generate_files
from services.exporter import download_file

routes = Blueprint("routes", __name__)


@routes.route("/generate", methods=["GET"])
def generate():
    query = request.args.get("q")

    if not query:
        return {"error": "Missing query"}, 400

    data = jsfetcher(query)

    csv_file, excel_file = generate_files(data, query)

    return jsonify({
        "csv": csv_file,
        "excel": excel_file
    })


@routes.route("/download/<filename>", methods=["GET"])
def download(filename):
    return download_file(filename)