$(function(){
    //setting up csrf token for ajax requests
    csrftoken = Cookies.get('csrftoken');

    //get tags and add to the tagsinput
    var js_tags = "{{js_tags|safe}}";
    console.log('js_tags: ' + js_tags);

    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
       return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
});