from flask import Flask, render_template, request, send_file
from scraper import scrape_books
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        target_url = request.form.get("url")

        # Call your scraper function
        filename, error = scrape_books(target_url)

        if error:
            return render_template("index.html", error=error)

        # Send the file to the user
        return send_file(os.path.join("downloads", filename), as_attachment=True)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
