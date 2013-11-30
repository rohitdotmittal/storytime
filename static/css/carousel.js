      $(document).ready(function() {
	/* buttons that can be turned on (1) and off (0) */
	/* turns auto moving on */
	var auto_slide = 1;
	/* disables the auto moving feature when mouse is hovered over the carousel */
	var hover_pause = 1;
	/* sets auto moving by one image width at once every 5 seconds */
	var auto_slide_seconds = 5000;
	
	/* puts one image to the left of the first one so that when the right arrow is clicked there's a image to be moved over from the left. The 'left: -200px;' css makes it so that this moved over image is hidden to the left combined with the css 'overflow: hidden;' */
	$('#restaurants_carousel li:first').before($('#restaurants_carousel li:last'));
	
	if (auto_slide == 1) {
		/* setInterval function causes the slide() function to be run every few seconds defined by the various auto_slid_seconds. It is currently set to go right but you can change it to left if you wish */
		var timer = setInterval('slide("right")', auto_slide_seconds);
	}
	
	if (hover_pause == 1) {
		// remove the previously set setInterval function when mouse pointer is hovered over the #carousel_ul unordered list
		$('#restaurants_carousel').hover(function() {
			clearInterval(timer)
		}, function() {
			// add back in the setInterval auto-moving function when the mouse moves out of the unordered list area
			timer = setInterval('slide("right")', auto_slide_seconds); 
		});
	}
});

// main slide function
function slide(where) {
	// .outerWidth() is different than the jQuery .outer() function in that .outerWidth() can be set to grab both the padding and margin of an element, while the default setting is to just grab the left and right padding, which is what's being used here
	var item_width = $('#restaurants_carousel li').outerWidth();
	
	if (where == 'left') {
		// parseInt() is a javascript function that parses out the non-numerical values in a string and returns a numeric value. Here, the 'px' portion of the string is removed so the variable 'left_indent' can be used further down in another function
		// in the css file global.css, relative position of the unordered list #carousel_ul is set to -200 to match the image widths (plus margins if necessary), here that css property is being added or subtracted with the image width depending on the direction of the carousel flow
		var left_indent = parseInt($('#restaurants_carousel').css('left')) + item_width;
	} else {
		var left_indent = parseInt($('#restaurants_carousel').css('left')) - item_width;
	}
	// a jquery .animate() function is used to move the unordered list to the near css position in a smooth transition animation.
	// the ':not(:animated)' portion ensures that the jquery animation portion caused by the click of the arrow button is only initiated if there is no auto-move currently in progress on the unordered list. If this isn't set, then a double-move can happen, which screws up the jquery animation
	$('#restaurants_carousel:not(:animated)').stop().animate({'left': left_indent}, 500, function() {
		// after the jQuery animation is finished, the furthest left/right item is moved to the furthest right/left so that a unlimited carousel loop flow can be achieved and maintained regardless of the number of times the left and right buttons are clicked.
		if (where == 'left') {
			$('#restaurants_carousel li:first').before($('#restaurants_carousel li:last'));
		} else {
			$('#restaurants_carousel li:last').after($('#restaurants_carousel li:first'));
		}
		// once the left or right image ordering has been finished, the css position 'left:' is resetted to -200px since the reording of the image elements after the jQuery animation has now been completed. This is done because the jQuery animation portion changed this css property and if left by itself, will eventually take the unordered list element off of the visible screen area.
		$('#restaurants_carousel').css({'left' : '-200px'});
	});
}


      $(document).ready(function() {
	/* buttons that can be turned on (1) and off (0) */
	/* turns auto moving on */
	var auto_slide = 1;
	/* disables the auto moving feature when mouse is hovered over the carousel */
	var hover_pause = 1;
	/* sets auto moving by one image width at once every 5 seconds */
	var auto_slide_seconds = 5000;
	
	/* puts one image to the left of the first one so that when the right arrow is clicked there's a image to be moved over from the left. The 'left: -200px;' css makes it so that this moved over image is hidden to the left combined with the css 'overflow: hidden;' */
	$('#shopping_carousel li:first').before($('#shopping_carousel li:last'));
	
	if (auto_slide == 1) {
		/* setInterval function causes the slide() function to be run every few seconds defined by the various auto_slid_seconds. It is currently set to go right but you can change it to left if you wish */
		var timer = setInterval('slide("right")', auto_slide_seconds);
	}
	
	if (hover_pause == 1) {
		// remove the previously set setInterval function when mouse pointer is hovered over the #carousel_ul unordered list
		$('#shopping_carousel').hover(function() {
			clearInterval(timer)
		}, function() {
			// add back in the setInterval auto-moving function when the mouse moves out of the unordered list area
			timer = setInterval('slide("right")', auto_slide_seconds); 
		});
	}
});

// main slide function
function slide_2(where) {
	// .outerWidth() is different than the jQuery .outer() function in that .outerWidth() can be set to grab both the padding and margin of an element, while the default setting is to just grab the left and right padding, which is what's being used here
	var item_width = $('#shopping_carousel li').outerWidth();
	
	if (where == 'left') {
		// parseInt() is a javascript function that parses out the non-numerical values in a string and returns a numeric value. Here, the 'px' portion of the string is removed so the variable 'left_indent' can be used further down in another function
		// in the css file global.css, relative position of the unordered list #carousel_ul is set to -200 to match the image widths (plus margins if necessary), here that css property is being added or subtracted with the image width depending on the direction of the carousel flow
		var left_indent = parseInt($('#shopping_carousel').css('left')) + item_width;
	} else {
		var left_indent = parseInt($('#shopping_carousel').css('left')) - item_width;
	}
	// a jquery .animate() function is used to move the unordered list to the near css position in a smooth transition animation.
	// the ':not(:animated)' portion ensures that the jquery animation portion caused by the click of the arrow button is only initiated if there is no auto-move currently in progress on the unordered list. If this isn't set, then a double-move can happen, which screws up the jquery animation
	$('#shopping_carousel:not(:animated)').stop().animate({'left': left_indent}, 500, function() {
		// after the jQuery animation is finished, the furthest left/right item is moved to the furthest right/left so that a unlimited carousel loop flow can be achieved and maintained regardless of the number of times the left and right buttons are clicked.
		if (where == 'left') {
			$('#shopping_carousel li:first').before($('#shopping_carousel li:last'));
		} else {
			$('#shopping_carousel li:last').after($('#shopping_carousel li:first'));
		}
		// once the left or right image ordering has been finished, the css position 'left:' is resetted to -200px since the reording of the image elements after the jQuery animation has now been completed. This is done because the jQuery animation portion changed this css property and if left by itself, will eventually take the unordered list element off of the visible screen area.
		$('#shopping_carousel').css({'left' : '-200px'});
	});
}
      

                $(document).ready(function(){
        $('.image_holder').hover(function(){
                  $(this).children('.bottom-caption').stop().animate({top:'180px'},{queue:false,duration:300});
                  $(".top-caption", this).stop().animate({top:'0px'},{queue:false,duration:300});
    }, function() {
            $(".bottom-caption", this).stop().animate({top:'200px'},{queue:false,duration:300});
            $(".top-caption", this).stop().animate({top:'-20px'},{queue:false,duration:300});
        }) }) ;

