document.addEventListener("DOMContentLoaded", function () {
    let books = document.querySelectorAll(".card");

    books.forEach((book, index) => {
        setTimeout(() => {
            book.classList.add("fade-in");
        }, index * 200); // Her kitap için gecikmeli animasyon
    });
});
