function searchBooks(query) {
    return fetch('http://127.0.0.1:5000/AI_Search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ context: query })
    }).then(response => response.json())
      .then(data => {
        displayBooks(data.books);
    }).catch((error) => {
        console.error('Error:', error);
    });
}

function closeModal() {
    document.querySelector('.book-list').classList.remove('show'); 
    setTimeout(() => document.getElementById('bookModal').style.display = 'none', 300);
}

function displayBooks(books) {
    const bookList = document.querySelector('.book-list');
    bookList.innerHTML = '';
    bookList.classList.add('show');
    books.forEach(book => {
        const li = document.createElement("li");
        const a = document.createElement("a");
        a.href = `https://www.google.com/search?q=${encodeURIComponent(book)}`;
        a.textContent = book;
        a.target = "_blank"; 
  
        li.appendChild(a);
        ul.appendChild(li);
    });
  
    document.getElementById('bookModal').style.display = 'flex';
  }  

  function displayBooks(books) {
    const bookList = document.querySelector('.book-list');
    bookList.innerHTML = ''; // Clear any previous results
    bookList.classList.add('show'); // Add transition effect
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
    document.querySelector('.book-list').classList.remove('show');
    setTimeout(() => {
        document.getElementById('bookModal').style.display = 'none';
    }, 300);
}
