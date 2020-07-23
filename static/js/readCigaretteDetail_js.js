$(document).ready(function(){

    var curUser = $('#user_username').html();
    var Nicknames = document.getElementsByClassName('EditAndDelete');    
    for(var i = 0; i<Nicknames.length; i++){
      var Nickname = Nicknames[i].getAttribute('value');
      if(curUser == Nickname){
        Nicknames[i].style.display = 'block';
      }
    }    
        
    $('#star_grade a').click(function(){
      $(this).parent().children("a").removeClass("on");
      $(this).addClass("on").prevAll("a").addClass("on");
      var star = $(this).attr('value');
      star = parseInt(star);
      $('#starPoint').attr('value', star);
      return false;
    });

    $('.deleteBtn').click(function(){
      if(confirm("정말 삭제하시겠습니까?") == true){
          
      }
      else{
        return false;
      }
    });
});
