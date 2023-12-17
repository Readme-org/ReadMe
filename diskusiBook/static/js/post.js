async function getComments() {
    return fetch(get_comment_url).then((res) => res.json())
}

async function getReplies(id) {
    var get_reply_url = `/diskusi-book/get_reply/${id}/`;
    return fetch(get_reply_url).then((res) => res.json())
}

async function getSinglePost() {
    const response = await fetch(get_single_post_url);
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    const post = await response.json();
    return post[0];
}

async function getUsername(userId) {
    const response = await fetch(`/diskusi-book/get_username/${userId}/`);

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    const user = await response.json();
    return user.username;
}

async function refreshComments() {
    document.getElementById("comment-card").innerHTML = ""
    const singlePost = await getSinglePost()
    const comments = await getComments()
    let htmlString = `` // needs revision
    const user = user_id
    const usernameOfPost = await getUsername(singlePost.fields.user) 

    const editDeleteButtonsPost = `
                <button class="btn btn-outline-primary" type="button" data-bs-toggle="modal" data-bs-target="#exampleModal${singlePost.pk}">Edit</button>
                <button class="btn btn-outline-danger" type="button" data-bs-toggle="modal" data-bs-target="#deletePostModal${singlePost.pk}">Delete</button>
                <div class="modal fade" id="deletePostModal${singlePost.pk}" tabindex="-1" aria-labelledby="deletePostModalLabel" aria-hidden="true">
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
                                <button type="button" class="btn btn-danger" id="button_delete" data-bs-dismiss="modal" onclick="deletePost(${singlePost.pk}); return false;">Delete</button>
                            </div>
                        </div>
                    </div>
                </div>
        `;
    const userOwnershipPost = +user === +singlePost.fields.user

    htmlString += `\n
        <div class="modal fade" id="exampleModal${singlePost.pk}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Edit Post</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form id="form${singlePost.pk}" onsubmit="return false;">
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
                <button type="button" class="btn btn-primary" id="button_edit" data-bs-dismiss="modal" onclick="editPost(${singlePost.pk}); return false;">Edit</button>
            </div>
        </div>
    </div>
</div>
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <p class="card-text"><small class="text-muted">Posted by ${usernameOfPost}</small></p>
                        <h5 class="card-title">${singlePost.fields.title}</h5>
                        <p class="card-text">${singlePost.fields.content}</p>
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <div class="modal fade" id="CommentModal${singlePost.pk}" tabindex="-1" aria-labelledby="CommentModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="CommentModalLabel">Comment</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form id="Commentform${singlePost.pk}" onsubmit="return false;">
                    <div class="mb-3">
                        <label for="Commentcontent${singlePost.pk}" class="col-form-label">Content</label>
                        <textarea class="form-control" id="Commentcontent${singlePost.pk}" name="Commentcontent${singlePost.pk}" maxlength="40000" required></textarea>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" id="button_comment" data-bs-dismiss="modal" onclick="createAComment(${singlePost.pk}); return false;">Add Comment</button>
            </div>
        </div>
    </div>
</div>
<button class="btn btn-outline-secondary" type="button" data-bs-toggle="modal" data-bs-target="#CommentModal${singlePost.pk}">Comment</button>
                            ${userOwnershipPost ? editDeleteButtonsPost : ``}
                        </div>
                    </div>
                </div>
            </div>
            <div class="comments-section">
            </div>
            <h2>Comments</h2>`
    for (let comment of comments) {
        const usernameOfComment = await getUsername(comment.fields.user) 
        const replies = await getReplies(comment.pk)
        const editDeleteButtonsComment = `
        <button class="btn btn-outline-primary" type="button" data-bs-toggle="modal" data-bs-target="#CommentEditModal${comment.pk}">Edit</button>
                <button class="btn btn-outline-danger" type="button" data-bs-toggle="modal" data-bs-target="#deleteCommentModal${comment.pk}">Delete</button>
                <div class="modal fade" id="deleteCommentModal${comment.pk}" tabindex="-1" aria-labelledby="deleteCommentModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5" id="deleteCommentModalLabel">Delete Comment</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <p>Apakah anda yakin ingin menghapus comment ini?</p>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                                <button type="button" class="btn btn-danger" id="button_delete" data-bs-dismiss="modal" onclick="deleteComment(${comment.pk}); return false;">Delete</button>
                            </div>
                        </div>
                    </div>
                </div>
        `;
        const userOwnershipComment = +user === +comment.fields.user

        htmlString += `\n
        <div class="modal fade" id="CommentEditModal${comment.pk}" tabindex="-1" aria-labelledby="CommentEditModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="CommentEditModalLabel">Edit Comment</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form id="CommentEditform${comment.pk}" onsubmit="return false;">
                    <div class="mb-3">
                        <label for="CommentEditcontent${comment.pk}" class="col-form-label">Content</label>
                        <textarea class="form-control" id="CommentEditcontent${comment.pk}" name="CommentEditcontent${comment.pk}" maxlength="40000" required></textarea>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" id="button_CommentEdit" data-bs-dismiss="modal" onclick="editComment(${comment.pk}); return false;">Edit</button>
            </div>
        </div>
    </div>
</div>
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <p class="card-text"><small class="text-muted">Commented by ${usernameOfComment}</small></p>
                        <p class="card-text">${comment.fields.content}</p>
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <div class="modal fade" id="ReplyModal${comment.pk}" tabindex="-1" aria-labelledby="ReplyModalLabel" aria-hidden="true">
                        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h1 class="modal-title fs-5" id="ReplyModalLabel">Reply</h1>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <div class="modal-body">
                                    <form id="Replyform${comment.pk}" onsubmit="return false;">
                                        <div class="mb-3">
                                            <label for="Replycontent${comment.pk}" class="col-form-label">Content</label>
                                            <textarea class="form-control" id="Replycontent${comment.pk}" name="Replycontent${comment.pk}" maxlength="40000" required></textarea>
                                        </div>
                                    </form>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    <button type="button" class="btn btn-primary" id="button_reply" data-bs-dismiss="modal" onclick="createAReply(${comment.pk}); return false;">Add Reply</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <button class="btn btn-outline-secondary" type="button" data-bs-toggle="modal" data-bs-target="#ReplyModal${comment.pk}">Reply</button>
                            ${userOwnershipComment ? editDeleteButtonsComment : ``}
                        </div>
                    </div>
                </div>
            </div>`;
        
            for (let reply of replies) {
            const usernameOfReply = await getUsername(reply.fields.user) 
            const editDeleteButtonsReply = `
            <button class="btn btn-outline-primary" type="button" data-bs-toggle="modal" data-bs-target="#ReplyEditModal${reply.pk}">Edit</button>
                    <button class="btn btn-outline-danger" type="button" data-bs-toggle="modal" data-bs-target="#deleteReplyModal${reply.pk}">Delete</button>
                    <div class="modal fade" id="deleteReplyModal${reply.pk}" tabindex="-1" aria-labelledby="deleteReplyModalLabel" aria-hidden="true">
                        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h1 class="modal-title fs-5" id="deleteReplyModalLabel">Delete Reply</h1>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <div class="modal-body">
                                    <p>Apakah anda yakin ingin menghapus reply ini?</p>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                                    <button type="button" class="btn btn-danger" id="button_delete" data-bs-dismiss="modal" onclick="deleteReply(${reply.pk}); return false;">Delete</button>
                                </div>
                            </div>
                        </div>
                    </div>
            `;
            const userOwnershipReply = +user === +reply.fields.user

            htmlString += `\n
            <div class="modal fade" id="ReplyEditModal${reply.pk}" tabindex="-1" aria-labelledby="ReplyEditModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="ReplyEditModalLabel">Edit Reply</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form id="ReplyEditform${reply.pk}" onsubmit="return false;">
                        <div class="mb-3">
                            <label for="ReplyEditcontent${reply.pk}" class="col-form-label">Content</label>
                            <textarea class="form-control" id="ReplyEditcontent${reply.pk}" name="ReplyEditcontent${reply.pk}" maxlength="40000" required></textarea>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" id="button_ReplyEdit" data-bs-dismiss="modal" onclick="editReply(${reply.pk}); return false;">Edit</button>
                </div>
            </div>
        </div>
    </div>
                <div class="col">
                    <div class="card reply-card">
                        <div class="card-body">
                            <p class="card-text"><small class="text-muted">Replied by ${usernameOfReply}</small></p>
                            <p class="card-text">${reply.fields.content}</p>
                            <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                                ${userOwnershipReply ? editDeleteButtonsReply : ``}
                            </div>
                        </div>
                    </div>
                </div>`;
        }
            
    }

    document.getElementById("comment-card").innerHTML = htmlString
}

refreshComments()

// document.getElementById("button_edit").onclick = editPost

function troll(postId){
    console.log("troll" + postId)
}

function showDiscussion(bookId) {
    // console.log('/diskusi-book/show_post/${bookId}/${postId}');
    window.location.href = `/diskusi-book/diskusi-book/${bookId}/`;
}

function createAComment(postId){
    const form = document.querySelector(`#Commentform${postId}`);
    const content = form.querySelector(`textarea[name="Commentcontent${postId}"]`);

    if (content.value.length === 0) {
        alert('Please enter a content.');
        return false;
    }

    else{
        fetch(`/diskusi-book/create_comment/${postId}/`, {
            method: "POST",
            body: new FormData(document.querySelector(`#Commentform${postId}`))
        }).then(refreshComments)
    }

    document.getElementById(`Commentform${postId}`).reset()
    return false
}

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
        }).then(refreshComments)
    }

    document.getElementById(`form${postId}`).reset()
    return false
}

function deletePost(postId) {
    fetch(`/diskusi-book/remove_post/${postId}/`, {
        method: "GET",

    }).then(showDiscussion(book_id))
    return false;
}

function editComment(commentId){
    const form = document.querySelector(`#CommentEditform${commentId}`);
    const content = form.querySelector(`textarea[name="CommentEditcontent${commentId}"]`);

    if (content.value.length === 0) {
        alert('Please enter a content.');
        return false;
    }

    else{
        fetch(`/diskusi-book/edit_comment/${commentId}/`, {
            method: "POST",
            body: new FormData(document.querySelector(`#CommentEditform${commentId}`))
        }).then(refreshComments)
    }

    document.getElementById(`CommentEditform${commentId}`).reset()
    return false
}

function deleteComment(commentId){
    fetch(`/diskusi-book/remove_comment/${commentId}/`, {
        method: "GET",

    }).then(refreshComments)
    return false;
}

function createAReply(commentId){
    const form = document.querySelector(`#Replyform${commentId}`);
    const content = form.querySelector(`textarea[name="Replycontent${commentId}"]`);

    if (content.value.length === 0) {
        alert('Please enter a content.');
        return false;
    }

    else{
        fetch(`/diskusi-book/create_reply/${commentId}/`, {
            method: "POST",
            body: new FormData(document.querySelector(`#Replyform${commentId}`))
        }).then(refreshComments)
    }

    document.getElementById(`Replyform${commentId}`).reset()
    return false
}

function editReply(replyId){
    const form = document.querySelector(`#ReplyEditform${replyId}`);
    const content = form.querySelector(`textarea[name="ReplyEditcontent${replyId}"]`);

    if (content.value.length === 0) {
        alert('Please enter a content.');
        return false;
    }

    else{
        fetch(`/diskusi-book/edit_reply/${replyId}/`, {
            method: "POST",
            body: new FormData(document.querySelector(`#ReplyEditform${replyId}`))
        }).then(refreshComments)
    }

    document.getElementById(`ReplyEditform${replyId}`).reset()
    return false
}

function deleteReply(replyId){
    fetch(`/diskusi-book/remove_reply/${replyId}/`, {
        method: "GET",

    }).then(refreshComments)
    return false;
}

function showPost1() {

    console.log(`5532523`)
}
