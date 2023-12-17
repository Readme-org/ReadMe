async function getPosts() {
    return fetch(get_post_url).then((res) => res.json())
}

async function refreshPosts() {
    document.getElementById("post-card").innerHTML = ""
    const posts = await getPosts()
    let htmlString = `` // needs revision
    const user = user_id
    posts.forEach((post, index) => {
        const editDeleteButtons = `
        <button class="btn btn-outline-primary" type="button" data-bs-toggle="modal" data-bs-target="#exampleModal${post.pk}">Edit</button>
                <button class="btn btn-outline-danger" type="button" onclick="deletePost(${post.pk}); return false;">Delete</button>
        `;
        const userOwnership = +user === +post.fields.user

        htmlString += `\n
        <div class="modal fade" id="exampleModal${post.pk}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Edit Post</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form id="form${post.pk}" onsubmit="return false;">
                    <div class="mb-3">
                        <label for="title" class="col-form-label">Title</label>
                        <input type="text" class="form-control" id="title" name="title"></input>
                    </div>
                    <div class="mb-3">
                        <label for="content" class="col-form-label">Content</label>
                        <textarea class="form-control" id="content" name="content"></textarea>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" id="button_edit" data-bs-dismiss="modal" onclick="editPost(${post.pk}); return false;">Edit</button>
            </div>
        </div>
    </div>
</div>
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title"><button  onclick="showPost2(${post.pk}); return false;">${post.fields.title}</button></h5>
                        <p class="card-text">${post.fields.content}</p>
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                            ${userOwnership ? editDeleteButtons : ``}
                        </div>
                    </div>
                </div>
            </div>`
    })

    document.getElementById("post-card").innerHTML = htmlString
}

refreshPosts();

function showPost2(postId) {
    // console.log('/diskusi-book/show_post/${bookId}/${postId}');
    window.location.href = `/diskusi-book/show_post/${postId}/`;
}

// document.getElementById("button_edit").onclick = editPost

function editPost(postId) {
    fetch(`/diskusi-book/edit_post/${postId}/`, {
        method: "POST",
        body: new FormData(document.querySelector(`#form${postId}`))
    }).then(refreshPosts)

    document.getElementById(`form${postId}`).reset()
    return false
}

function deletePost(postId) {
    fetch(`/diskusi-book/remove_post/${postId}/`, {
        method: "GET",

    }).then(refreshPosts)
    return false;
}

function showPost1() {

    console.log(`5532523`)
}
