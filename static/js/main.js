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




$(function () {

    
    console.log('okokok');

    

});

