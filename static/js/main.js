function delete_comment(comment_id) {
    console.log(comment_id);
    $.ajax({
        url: '/rango/delete_comment/',
        type:"POST",
        data: {"comment_id":comment_id},
        success: function(e){
        if(e=="1"){
            parent.location.reload();
            console.log("删除成功");
        }else{
            console.log("删除失败");
        }

        },
    })


}
 // 确认删除评论的函数
 function confirm_delete(comment_id ) {
    // 调用layer弹窗组件
    layer.open({
        // 弹窗标题
        title: "delete comment？",
        // 正文
        content: "This can’t be undone and it will be removed from the web. ",
        // 点击按钮后调用的回调函数
        yes: function(index, layero) {
            // 指定应当前往的 url
            
            delete_comment(comment_id)
        },
    })
}

function like_category(category_id) {
    console.log(category_id);
    $.ajax({
        url: '/rango/like_category/',
        type:"POST",
        data: {"category_id":category_id},
        success: function(e){
        if(e=="1"){
            parent.location.reload();
            console.log("点赞成功");
        }else{
            console.log("点赞失败");
        }

        },
    })

}

function like_comment(comment_id) {
    console.log(comment_id);
    $.ajax({
        url: '/rango/like_comment/',
        type:"POST",
        data: {"comment_id":comment_id},
        success: function(e){
        if(e=="1"){
            parent.location.reload();
            console.log("点赞成功");
        }else{
            console.log("点赞失败");
        }

        },
    })

}




$(function () {

    
    console.log('okokok');

    

});

