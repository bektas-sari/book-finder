import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_book_price_kitapyurdu(book_name):
    """Kitapyurdu sitesinden kitap fiyatlarını çeker."""
    search_url = f"https://www.kitapyurdu.com/index.php?route=product/search&filter_name={book_name}"
    
    response = requests.get(search_url, headers=HEADERS)
    if response.status_code != 200:
        return {"error": "Failed to connect to Kitapyurdu"}
    
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("div", class_="product-cr")

    if not books:
        return {"error": "No books found"}
    
    results = []
    
    for book in books[:5]:  # İlk 5 kitabı alalım
        try:
            title = book.find("div", class_="name").text.strip()
            price = book.find("div", class_="price").text.strip()
            
            book_link = book.find("a")["href"]
            if not book_link.startswith("http"):
                book_link = "https://www.kitapyurdu.com" + book_link
                   # Eğer link tam URL değilse düzelt
            img_url = book.find("img")["src"]
            results.append({
                "title": title,
                "price": price,
                "link": book_link,
                "image": img_url
            })
        except AttributeError:
            continue

    return results if results else {"error": "No valid book data found"}
