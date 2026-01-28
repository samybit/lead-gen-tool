from flask import Flask, render_template, request, send_file
from scraper import scrape_books
# import os <-- You can remove this now, as we aren't using file paths anymore!

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        target_url = request.form.get("url")

        # Call scraper (now returns a memory file object)
        excel_file, error = scrape_books(target_url)

        if error:
            return render_template("index.html", error=error)

        # Send file directly from RAM
        return send_file(
            excel_file,
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            as_attachment=True,
            download_name="scraped_data.xlsx",
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
