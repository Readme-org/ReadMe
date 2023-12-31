function searchBooks(query) {
    fetch('http://127.0.0.1:5000/AI_Search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ context: query })
    })
    .then(response => response.json())
    .then(data => {
        displayBooks(data.books);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
  
function displayResults(books) {
    const searchResults = document.getElementById("searchResults");

    // Bersihkan hasil pencarian lama
    searchResults.innerHTML = "";

    // Buat ul element untuk menampilkan hasil pencarian
    const ul = document.createElement("ul");
    ul.className = "book-list";
  
    books.forEach(book => {
        const li = document.createElement("li");
        const a = document.createElement("a");

        // asumsikan kita memiliki URL untuk setiap buku, tambahkan URL ke atribut href
        a.href = `https://www.google.com/search?q=${encodeURIComponent(book)}`; // ini hanya contoh, sesuaikan URL dengan kebutuhan Anda
        a.textContent = book;
        a.target = "_blank"; // buka di tab baru

        li.appendChild(a);
        ul.appendChild(li);
    });

    searchResults.appendChild(ul);
}

function displayBooks(books) {
    const bookList = document.querySelector('.book-list');
    bookList.innerHTML = ''; // Clear any previous results
    books.forEach(book => {
        const bookItem = document.createElement('div');
        bookItem.className = 'book-item';

        const bookCover = document.createElement('img');
        bookCover.src = book.volumeInfo.imageLinks.thumbnail;
        bookCover.className = 'book-cover';

        const bookDetails = document.createElement('div');
        bookDetails.className = 'book-details';

        const bookTitle = document.createElement('h2');
        bookTitle.className = 'book-title';
        bookTitle.innerText = book.volumeInfo.title;

        const bookDescription = document.createElement('p');
        bookDescription.className = 'book-description';
        bookDescription.innerText = book.volumeInfo.description;

        const bookRating = document.createElement('p');
        bookRating.className = 'book-rating';
        bookRating.innerText = `Rating: ${book.volumeInfo.averageRating}/5`;

        const bookAuthors = document.createElement('p');
        bookAuthors.className = 'book-authors';
        bookAuthors.innerText = `Authors: ${book.volumeInfo.authors.join(', ')}`;

        bookDetails.appendChild(bookTitle);
        bookDetails.appendChild(bookDescription);
        bookDetails.appendChild(bookRating);
        bookDetails.appendChild(bookAuthors);

        bookItem.appendChild(bookCover);
        bookItem.appendChild(bookDetails);

        bookList.appendChild(bookItem);
    });
    document.getElementById('bookModal').style.display = 'flex';
}
  
function closeModal() {
    document.getElementById('bookModal').style.display = 'none';
}