$(document).ready(function() {
   $.ajax({
    url: RECENT_ACTIVITY,
    type: "GET",
    data: {
        user: user
    },
    dataType: 'html',
    success: function(data) {
              console.log(data);
          }
  });
});