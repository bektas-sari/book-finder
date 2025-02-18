from flask import Flask, render_template, request
from scraper import get_book_price_kitapyurdu

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    books = []
    if request.method == "POST":
        book_name = request.form["book"]
        books = get_book_price_kitapyurdu(book_name)
        
        if "error" in books:
            return render_template("index.html", error=books["error"])

    return render_template("index.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)
