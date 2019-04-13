$(function(){
    //setting up csrf token for ajax requests
    csrftoken = Cookies.get('csrftoken');

    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    //is called when a file link is clicked
    $('.file_link').click(function(){
        let filePath = $(this).text();
        $.ajax({
           type:'GET',
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