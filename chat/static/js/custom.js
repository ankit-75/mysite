/*start custom js*/

(function() {
    'use strict';
    $('.hamburger-menu').click(function (e) {
        e.preventDefault();
        if ($(this).hasClass('active')){
            $(this).removeClass('active');
            $('.menu-overlay').fadeToggle( 'fast', 'linear' );
            $(' .menu-list').slideToggle( 'slow', 'swing' );
            $('.hamburger-menu-wrapper').toggleClass('bounce-effect');
        } else {
            $(this).addClass('active');
            $('.menu-overlay').fadeToggle( 'fast', 'linear' );
            $(' .menu-list').slideToggle( 'slow', 'swing' );
            $('.hamburger-menu-wrapper').toggleClass('bounce-effect');
        }
    })
})();

/*start search mb secton*/
$(document).ready(function(){
  $("#mb").click(function(){
  $("#mb-form").slideToggle('slow');

  });

});

/*start custom crousel code*/
    var $item = $('.carousel .item'); 
var $wHeight = $(window).height();
$item.eq(0).addClass('active');
$item.height($wHeight); 
$item.addClass('full-screen');

$('.carousel img').each(function() {
  var $src = $(this).attr('src');
  var $color = $(this).attr('data-color');
  $(this).parent().css({
    'background-image' : 'url(' + $src + ')',
    'background-color' : $color
  });
  $(this).remove();
});

$(window).on('resize', function (){
  $wHeight = $(window).height();
  $item.height($wHeight);
});

$('.carousel').carousel({
  interval:false,
  pause: "false"
}); 

