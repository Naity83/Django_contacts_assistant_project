$(window).on('load', function() { // makes sure the whole site is loaded 
    $('#status').fadeOut(); // will first fade out the loading animation 
    $('#preloader').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website. 
    $('body').delay(350).css({'overflow':'visible'});
})

$(document).ready(function () {
 
  $('.menu-link').click(function() {
      $('#menu').prop('checked', false); // Забезпечити закриття меню
  });
  
    // back to top button
    var offset = 300;
    var scroll_top_duration = 700;
    var $back_to_top = $('.backToTop');

    $(window).scroll(function(){
        ( $(this).scrollTop() > offset ) ? $back_to_top.addClass('backToTop-is-visible') : $back_to_top.removeClass('backToTop-is-visible backToTop-fade-out');
            
    });

    //smooth scroll

//scroll Offset Value
var scrollOffsetVal = 124;

// smaller screen value
if ($(window).width() < 1350) { 
    scrollOffsetVal = 75;
}

//check if hash exist on page
if(window.location.hash) {
    $(window).scrollTop($(window).scrollTop() + -scrollOffsetVal);
} 

//easy scroll

  $(function() {

    $('a[href*="#"]:not([href="#"])').click(function() {

        $('html, body').animate({
        scrollTop: $($(this).attr('href')).offset().top - scrollOffsetVal
        }, 1000);

    });
}); 

    
});


 // scroll menu
 $(window).scroll(function () {
    //closing menu if open
    $(".nav-icon1.open").click();

    if ($(this).scrollTop() > 400) {
      $(".floatingHeader").addClass("floating");
    } else if ($(this).scrollTop() === 0) {
      if ($(window).width() < 769) {
        $(".floatingHeader").removeClass("floating");
      } else {
        $(".floatingHeader").removeClass("floating");
      }
    }
  });

  //smooth scroll
