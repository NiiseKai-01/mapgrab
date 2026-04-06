import csv, time, re, os
from openpyxl import Workbook

FILES_DIR = "files"


def safe_filename(query):
    query = query.strip().lower().replace(" ", "_")
    return re.sub(r'[^a-z0-9_]', '', query)


# CLEANUP FUNCTION
def clean_files():
    for file in os.listdir(FILES_DIR):
        file_path = os.path.join(FILES_DIR, file)

        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Error deleting {file}: {e}")


def generate_files(data, query):
    if not data:
        return None, None

    clean_files()

    safe_name = safe_filename(query)
    timestamp = int(time.time())

    csv_filename = f"{FILES_DIR}/{safe_name}_{timestamp}.csv"
    excel_filename = f"{FILES_DIR}/{safe_name}_{timestamp}.xlsx"

    keys = list(data[0].keys())

    #CSV
    with open(csv_filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    #Excel
    wb = Workbook()
    ws = wb.active
    ws.append(keys)

    from openpyxl.styles import Font

    for row_idx, row in enumerate(data, start=2):  # start=2 because header is row 1
        for col_idx, key in enumerate(keys, start=1):
            value = row.get(key)

            cell = ws.cell(row=row_idx, column=col_idx)

            if key == "GOOGLE_MAPS_LINK" and value != "-":
                cell.value = "Open Map"
                cell.hyperlink = value
                cell.font = Font(color="0000FF", underline="single")
            else:
                cell.value = value

    wb.save(excel_filename)

    return csv_filename.split("/")[-1], excel_filename.split("/")[-1]