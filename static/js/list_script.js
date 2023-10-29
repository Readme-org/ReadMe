const scriptTag = document.querySelector('script[src*="list_script.js"]');
const getBookUrl = scriptTag.getAttribute('data-get-book-url');
const addBookUrl = scriptTag.getAttribute('data-add-book-url');

async function getBooks() {
    return fetch(getBookUrl).then((res) => res.json())
}

async function refreshProducts() {
    const books = await getBooks()
    
    const container = document.querySelector('.save-card');

    let productHTML = '';

    books.forEach(book => {
        productHTML += `
        <div class="card text-center">
            <div style="position: relative; z-index: 2;">
                <a href="/book-details/details-book/myBook/${book.pk}/" style="display: block; position: relative; z-index: 1;">
                    <img src="${book.fields.image}" alt="${book.fields.title} Cover" style="z-index: 0;"> 
                </a>
            </div>
            <div class="book-title">
                <h2>${book.fields.display_title}</h2>
            </div>
            <p>Penulis: ${book.fields.authors}</</p>
        </div>
        `;
    });

    container.innerHTML = productHTML;
}

refreshProducts()

function addBook() {
    fetch(addBookUrl, {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(refreshProducts)

    document.getElementById("form").reset();
    return false;
}

document.getElementById("button_add").onclick = addBook