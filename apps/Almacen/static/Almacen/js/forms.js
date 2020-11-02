$(document).ready(function(){
    var checkboxes = $('.form-check-input')
    if(checkboxes.length>0){
        var div = $('<div class="form-check">')
        div.append(checkboxes)
        $('#form').append(div)
    }
});