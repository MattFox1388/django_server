$(function(){
    $('#sortedTb').DataTable();
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
           url:'/open_file/?q=' + filePath,
            success:function(data){
               var win = window.open("", "Title", "toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=780,height=200,top="+(screen.height-400)+",left="+(screen.width-840));
               win.document.body.innerHTML = data;
            }
        });
    });
});
