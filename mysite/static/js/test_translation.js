$(document).ready(function(){
  var url = $('#test_translation').data('url');
  test_translation_view(url);
});

function test_translation_view(url) {
    $.ajax({
     url: url,
     type: 'GET',
     error: function(error) {
        console.log(error);
     },
     success: function(data) {
        console.log(data);
     },
  });
}
