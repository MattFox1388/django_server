$(function(){
    $('#sortedTb').DataTable({
        searching:false
    });
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
   	var win = window.open();
        $.ajax({
           type:'GET',
           url:'/open_file/?q=' + filePath,
            success:function(data){
               $(win.document.body).html(data);
            }
        });
    });
});
