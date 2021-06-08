jQuery(function($){
$('header button.mn').click(function(){
  $('body').toggleClass('active');
	$(this).toggleClass('active');
	$('header ul.menu').toggleClass('active');
});
	 $('.slide_gal').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: true,
      fade: true,
      asNavFor: '.slide_nav'
    });
    $('.slide_nav').slick({
      slidesToShow: 5,
      slidesToScroll: 1,
      asNavFor: '.slide_gal',
      dots: false,
      nav:false,
      arrows:false,
      centerMode: true,
      focusOnSelect: true,
    });	
		$('.about_slide-list').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows:false,
      dots:false,
      autoplay: true,
			fade: true,
      autoplaySpeed: 4000,
      responsive: [
      {
        breakpoint: 790,
        settings: {
          slidesToShow: 1
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1
        }
      }
    ]
    });
//	$('.about_slide-list').on('afterChange', function(event, slick, currentSlide, nextSlide){
//			$('.about_slide-list .about_slide-list-item').removeClass('move1');
//			$('.about_slide-list .about_slide-list-item').removeClass('move2');
//  		console.log(currentSlide);
//		});
    $('.partners_list').slick({
      slidesToShow: 5,
      slidesToScroll: 1,
      arrows:true,
      dots:false,
      autoplay: true,
      autoplaySpeed: 2000,
      responsive: [
      {
        breakpoint: 790,
        settings: {
          slidesToShow: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1
        }
      }
    ]
    });     
    $('.product_list').slick({
      slidesToShow: 4,
      slidesToScroll: 1,
      arrows:true,
      dots:false,
      autoplay: true,
      autoplaySpeed: 2000,
      responsive: [
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1
        }
      }
    ]
    }); 
  
    $('.fabric_list').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: true,
      fade: true,
    });
    $('.diler_list').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: true,
      fade: true,
    });
    $('.doma_list').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: true,
      fade: true,
    });
    $('.mag_list').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: true,
      fade: true,
    });
});
$(window).on('scroll', function (event) {
    var scrollValue = $(window).scrollTop();
    if (scrollValue > 90) {
        $('header').addClass('affix');
    } else{
        $('header').removeClass('affix');
    }
});
$(document).ready(function() {
   var margin = 100; 
   $("a").click(function() { 
		 	$('body').removeClass('active');
		 	$('header ul.menu').removeClass('active');
		 	$('header button.mn').removeClass('active');
      $("html, body").animate({
         scrollTop: $($(this).attr("href")).offset().top-150+margin+ "px" 
      }, {
         duration: 1600, 
         easing: "swing"
      });
      return false;
   });
});