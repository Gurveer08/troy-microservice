from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)


@app.route("/highly-reviewed", methods=["GET"])
def get_highly_reviewed_music():

    conn = sqlite3.connect("music.db")
    cursor = conn.cursor()

    cursor.execute("SELECT title, artist, rating FROM music WHERE rating >= 4.5 ORDER BY rating DESC")
    rows = cursor.fetchall()
    conn.close()

    # Convert query results to JSON format
    return jsonify([
        {"title": title, "artist": artist, "rating": rating}
        for (title, artist, rating) in rows
    ])


if __name__ == "__main__":
    app.run(debug=True)
