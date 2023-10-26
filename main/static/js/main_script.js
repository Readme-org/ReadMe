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
      displayResults(data.books);
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
      // Jika Anda tidak memiliki URL, Anda mungkin perlu mendapatkannya dari API lain atau gunakan "#" sebagai placeholder
      a.href = `https://www.google.com/search?q=${encodeURIComponent(book)}`; // ini hanya contoh, sesuaikan URL dengan kebutuhan Anda
      a.textContent = book;
      a.target = "_blank"; // buka di tab baru

      li.appendChild(a);
      ul.appendChild(li);
  });

  searchResults.appendChild(ul);
}
