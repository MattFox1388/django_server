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



    $('#submitTag').click(function(){
        let valStr = $('#tagInput').val();
        console.log('valStr: ' + valStr);
        tagInput = valStr.split(',');
        $.ajax({
           type:'POST',
           url: window.location.href,
            data: {'tagInput': tagInput},
            success:function(data){
               console.log('changed');
            }
        });
    });
});
