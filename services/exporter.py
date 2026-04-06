from flask import send_from_directory, abort
import os

FILES_DIR = "files"


def download_file(filename):
    file_path = os.path.join(FILES_DIR, filename)

    if not os.path.isfile(file_path):
        abort(404)

    if not filename.endswith((".csv", ".xlsx")):
        abort(403)

    return send_from_directory(FILES_DIR, filename, as_attachment=True)