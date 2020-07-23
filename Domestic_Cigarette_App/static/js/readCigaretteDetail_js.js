$(document).ready(function(){
    $('#star_grade a').click(function(){
      $(this).parent().children("a").removeClass("on");
      $(this).addClass("on").prevAll("a").addClass("on");
      var star = $(this).attr('value');
      star = parseInt(star);
      $('#starPoint').attr('value', star);
      return false;
    });
});
