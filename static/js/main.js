// click event funciton to delete comment
function delete_comment(comment_id) {
    console.log(comment_id);
    $.ajax({
        url: '/rango/delete_comment/',
        type: "POST",
        data: { "comment_id": comment_id },
        success: function (e) {
            if (e == "1") {
                parent.location.reload();
                console.log("delete successed");
            } else {
                console.log("delete failed");
            }

        },
    })


}

// click event funciton to open confirm delete modal
function confirm_delete(comment_id) {

    layer.open({
        // title
        title: "delete comment？",
        // text
        content: "This can’t be undone and it will be removed from the web. ",
        // click the button and call the function
        yes: function (index, layero) {
            // go to the url or the function

            delete_comment(comment_id)
        },
    })
}

// click event funciton to like a category
function like_category(category_id) {
    console.log(category_id);
    $.ajax({
        url: '/rango/like_category/',
        type: "POST",
        data: { "category_id": category_id },
        success: function (e) {
            if (e == "1") {
                parent.location.reload();
                console.log("like successed");
            } else {
                console.log("like failed");
            }

        },
    })

}
// click event funciton to like a comment
function like_comment(comment_id) {
    console.log(comment_id);
    $.ajax({
        url: '/rango/like_comment/',
        type: "POST",
        data: { "comment_id": comment_id },
        success: function (e) {
            if (e == "1") {
                parent.location.reload();
                console.log("like successed");
            } else {
                console.log("like failed");
            }

        },
    })

}



