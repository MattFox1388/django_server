$(function(){
    //setting up csrf token for ajax requests
    csrftoken = Cookies.get('csrftoken');

    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
       return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
});