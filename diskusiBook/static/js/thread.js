// const scriptTag = document.querySelector('script[src*="thread.js"]');
// const getPostUrl = scriptTag.getAttribute('data-get-post-url');
// const addPostUrl = scriptTag.getAttribute('data-add-post-url');

// async function getPosts() {
//   return fetch(getPostUrl).then((res) =>
//     res.json()
//   );
// }

// async function refreshPosts() {
//   document.getElementById("post-card").innerHTML = "";
//   const posts = await getPosts();
//   let htmlString = ``; // needs revision
//   const user = "{{ user_id }}";
//   posts.forEach((post, index) => {
//     const editDeleteButtons = `
//                 <button class="btn btn-outline-primary" type="button" onclick="editPost(${post.pk}); return false;">Edit</button>
//                         <button class="btn btn-outline-danger" type="button" onclick="deletePost(${post.pk}); return false;">Delete</button>
//                 `;
//     const userOwnership = +user === +post.fields.user;

//     htmlString += `\n
//                     <div class="col">
//                         <div class="card">
//                             <div class="card-body">
//                                 <h5 class="card-title"><a  onclick="showPost(${
//                                   post.fields.title
//                                 }); return false;">${post.fields.title}</a></h5>
//                                 <p class="card-text">${post.fields.content}</p>
//                                 <div class="d-grid gap-2 d-md-flex justify-content-md-end">
//                                     ${userOwnership ? editDeleteButtons : ``}
//                                 </div>
//                             </div>
//                         </div>
//                     </div>`;
//   });

//   document.getElementById("post-card").innerHTML = htmlString;
// }

// refreshPosts();

// function showPost(postTitle) {
//   window.location.href = `show_post/${postTitle}`;
// }

// function createPost(postId) {
//   fetch(`create_post/${postId}`, {
//     method: "POST",
//     body: new FormData(document.querySelector("#createpostform")),
//   }).then(refreshPosts);

//   document.getElementById("createpostform").reset();
//   return false;
// }

// document.getElementById("button_create").onclick = createPost;

// function editPost(postId) {
//   fetch(addPostUrl, {
//     method: "GET",
//   }).then(refreshPosts);
//   return false;
// }

// function deletePost(postId) {
//   fetch(`remove_post/${postId}`, {
//     method: "GET",
//   }).then(refreshPosts);
//   return false;
// }
