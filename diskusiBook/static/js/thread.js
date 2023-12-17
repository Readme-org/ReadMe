async function getPosts() {
    return fetch(get_post_url).then((res) => res.json())
}

async function getUsername(userId) {
    const response = await fetch(`/diskusi-book/get_username/${userId}/`);

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    const user = await response.json();
    return user.username;
}

async function refreshPosts() {
    document.getElementById("post-card").innerHTML = ""
    const posts = await getPosts()
    let htmlString = `` // needs revision
    const user = user_id
    for (let post of posts) {
        const usernameOfPost = await getUsername(post.fields.user)
        const editDeleteButtons = `
                <button class="btn btn-outline-primary" type="button" data-bs-toggle="modal" data-bs-target="#exampleModal${post.pk}">Edit</button>
                <button class="btn btn-outline-danger" type="button" data-bs-toggle="modal" data-bs-target="#deletePostModal${post.pk}">Delete</button>
                <div class="modal fade" id="deletePostModal${post.pk}" tabindex="-1" aria-labelledby="deletePostModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5" id="deletePostModalLabel">Delete Post</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <p>Apakah anda yakin ingin menghapus post ini?</p>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                                <button type="button" class="btn btn-danger" id="button_delete" data-bs-dismiss="modal" onclick="deletePost(${post.pk}); return false;">Delete</button>
                            </div>
                        </div>
                    </div>
                </div>
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
                                <input type="text" class="form-control" id="title" name="title" maxlength="300" required></input>
                            </div>
                            <div class="mb-3">
                                <label for="content" class="col-form-label">Content</label>
                                <textarea class="form-control" id="content" name="content" maxlength="40000" required></textarea>
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
                <div class="card" onmousedown="showPost2(event, ${post.pk}); return false;">
                    <div class="card-body">
                        <p class="card-text"><small class="text-muted">Posted by ${usernameOfPost}</small></p>
                        <h5 class="card-title ellipsis">${post.fields.title}</h5>
                        <p class="card-text ellipsis-content">${post.fields.content}</p>
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                            ${userOwnership ? editDeleteButtons : ``}
                        </div>
                    </div>
                </div>
            </div>`
    }

    document.getElementById("post-card").innerHTML = htmlString
}

refreshPosts();

function showPost2(event, postId) {
    // console.log('/diskusi-book/show_post/${bookId}/${postId}');
    var modalElement = document.getElementById(`deletePostModal${postId}`);
    var modal = bootstrap.Modal.getInstance(modalElement);
    if (modal && modal._isShown) {
        return;
    }
    if (event.target.tagName === 'BUTTON') {
        event.stopPropagation();
        return;
    }
    window.location.href = `/diskusi-book/show_post/${postId}/`;
}

// document.getElementById("button_edit").onclick = editPost

function editPost(postId) {
    const form = document.querySelector(`#form${postId}`);
    const title = form.querySelector('input[name="title"]');
    const content = form.querySelector('textarea[name="content"]');

    if (title.value.length === 0) {
        alert('Please enter a title.');
        return false;
    }

    else if (content.value.length === 0) {
        alert('Please enter a content.');
        return false;
    }

    else{
        fetch(`/diskusi-book/edit_post/${postId}/`, {
            method: "POST",
            body: new FormData(document.querySelector(`#form${postId}`))
        }).then(refreshPosts)
    }

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
