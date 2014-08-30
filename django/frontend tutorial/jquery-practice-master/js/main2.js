$(function () {

  var game = $('#game')

  game.hide();


  $('#character').on('change', function(){
    var name = $('#character').val();
    console.log(name);
    showGame();
    getName();
  });

  function showGame(){
    $('#name').hide();
    game.fadeIn(500);
  }
  function getName(){
    var name = $('#character').val();
    $('.character').html(name);
  }
  $('.homer').click(function(){
    //console.log($(this))
    $(this).fadeOut(1400);
  });

});
