$(function(){
    //is called when a file link is clicked
    $('.file_link').click(function(){
        let filePath = $(this).text();
        $.ajax({
           type:'POST',
           url:'/open_file/',
            data: {
               'file_path_clicked': filePath
            },
            success:function(){
               console.log("success!")
            }
        });
    });
});