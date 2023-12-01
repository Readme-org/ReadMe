const scriptTag = document.querySelector('script[src*="list_script.js"]');

async function getWishlist() {
    return fetch("{% url 'wishlistBook:get-books-json'}").then((res) => res.json())
}

async function refreshProducts(){
    const books = await getWishlist()

    let productHTML = '';

    books.forEach(book => {
        productHTML +=` 
        <div class="card text-center">
                <div style="position: relative; z-index: 2;">
                    <a href="{% url 'bookDetails:show_details' id=${book.book.id} %}" style="display: block; position: relative; z-index: 1;">
                        <img src="${book.book.image}" alt="${book.book.title} Cover" style="z-index: 0;"> 
                    </a>
                </div>
                <div class="book-title">
                    <h2>${book.book.display_title}</h2>
                </div>
                <p>Penulis: ${book.book.authors}</p>
            </div>`;
    });
    document.getElementById('card-container').innerHTML = productHTML;
}

refreshProducts()

function deleteWishlist(id){
    fetch(`/wishlistBook/delete-wishlist/${id}/`, {
        method: "DELETE",
    }).then(refreshProducts());
}
