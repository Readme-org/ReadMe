const idtest = document.getElementById("submit").getAttribute("data-book-id");
document.getElementById("submit").onclick = createPost(idtest);

function createPost(bookId) {
  fetch(`/diskusi-book/create_post/${bookId}/`, {
    method: "POST",
  }).then((response) => {
    if (response.ok) {
    } else {
    }
  });
}
