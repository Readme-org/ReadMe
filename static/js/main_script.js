function searchBooks(query) {
    var csrftoken = getCookie('csrftoken');  // Get CSRF token

    // Save search query to database
    fetch('history/add/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken  // Add CSRF token to request header
        },
        body: JSON.stringify({ query: query })
      });

    return fetch('https://octopus-app-cvv6j.ondigitalocean.app/AI_Search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ context: query })
    }).then(response => response.json())
      .then(data => {
        if (!data || !data.books) {
            console.error('Invalid data from server:', data);
            return;
        }
        console.log(data); 
        displayBooks(data.books);
    }).catch((error) => {
        console.error('Error:', error);
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function closeModal() {
    document.querySelector('.book-list').classList.remove('show'); 
    setTimeout(() => document.getElementById('bookModal').style.display = 'none', 300);
}

function displayBooks(books) {
    if (!books || !Array.isArray(books)) {
        console.error('Invalid books data:', books);
        return;
    }
    
    const bookList = document.querySelector('.book-list');
    bookList.innerHTML = ''; // Clear any previous results
    bookList.classList.add('show'); // Add transition effect

    books.forEach(book => {
        if (!book || !book.volumeInfo) {
            return;
        }
        const bookVolumeInfo = book.volumeInfo || {};
        
        const bookItem = document.createElement('div');
        bookItem.className = 'book-item';

        const bookCover = document.createElement('img');
        bookCover.className = 'book-cover';
        // Cek jika imageLinks dan thumbnail ada
        if (bookVolumeInfo.imageLinks?.thumbnail) {
            bookCover.src = bookVolumeInfo.imageLinks.thumbnail;
        } else {
            bookCover.src = "{% static 'default_cover.jpg' %}"; 
        }

        const bookDetails = document.createElement('div');
        bookDetails.className = 'book-details';

        const bookTitle = document.createElement('h2');
        bookTitle.className = 'book-title';
        bookTitle.innerText = bookVolumeInfo.title || 'Judul tidak tersedia';

        const bookDescription = document.createElement('p');
        bookDescription.className = 'book-description';
        bookDescription.innerText = bookVolumeInfo.description || 'Deskripsi tidak tersedia';

        const bookRating = document.createElement('p');
        bookRating.className = 'book-rating';
        bookRating.innerText = `Rating: ${(bookVolumeInfo.averageRating || 0)}/5`;

        const bookAuthors = document.createElement('p');
        bookAuthors.className = 'book-authors';
        if (bookVolumeInfo.authors && Array.isArray(bookVolumeInfo.authors) && bookVolumeInfo.authors.length) {
            bookAuthors.innerText = `Authors: ${bookVolumeInfo.authors.join(', ')}`;
        } else {
            bookAuthors.innerText = "Authors: Tidak diketahui";
        }

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



