import sys
import os
from datetime import datetime
from flask import Flask, request, jsonify, render_template, redirect, url_for


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from archive_handler import ArchiveHandler
from database_manager import DatabaseManager

app = Flask(__name__)
db_manager = DatabaseManager("archiver.db")
archive_handler = ArchiveHandler(db_manager)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_archive', methods=['GET', 'POST'])
def create_archive():
    if request.method == 'POST':
        try:
            data = request.json
            archive_name = data.get('archive_name')
            files = data.get('files')
            if not archive_name or not files:
                return jsonify({"error": "Invalid input"}), 400
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archive_id = archive_handler.create_archive(archive_name, files, timestamp)
            return jsonify({"message": "Archive created", "archive_id": archive_id})
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"error": f"An error occurred during archive creation: {e}"}), 500
    return render_template('create_archive.html')

@app.route('/extract_archive', methods=['GET', 'POST'])
def extract_archive():
    if request.method == 'POST':
        archive_name = request.form['archive_name']
        destination_folder = request.form['destination_folder']
        if not archive_name or not destination_folder:
            return jsonify({"error": "Invalid input"}), 400
        archive_handler.extract_archive(archive_name, destination_folder)
        return redirect(url_for('home'))
    return render_template('extract_archive.html')

@app.route('/show_database')
def show_database():
    archives = db_manager.get_archives()
    db_info = ""
    for archive in archives:
        archive_id, archive_name, timestamp = archive
        db_info += f"Архів: {archive_name} (створено: {timestamp})\n"
        files = db_manager.get_files_in_archive(archive_id)
        for file in files:
            db_info += f"  Файл: {file[0]}\n"
    return render_template('show_database.html', database_info=db_info)

@app.route('/clear_database', methods=['POST'])
def clear_database():
    try:
        db_manager.clear_database()
        return redirect(url_for('show_database'))
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred during database clearing"}), 500

if __name__ == '__main__':
    app.run(debug=True)
