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
   // $('.file_link').click(function(){
       /* let file_id = $(this).parent().attr('data-id');
        console.log('data-id: ' + file_id)
   	var win = window.open();
        $.ajax({
           type:'GET',
           url:'/details/' + file_id,
            success:function(data){
               $(win.document.body).html(data);
            }
        });
    });*/
});
