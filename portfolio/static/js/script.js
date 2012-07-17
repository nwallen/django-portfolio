/* Author:
Nicholas Wallen */

jQuery(document).ready(function($) {

        /* scrolling events */
         
        //scroll to anchor on click
         
	    $(".scroll").click(function(event){		
		    event.preventDefault();
             var hash =  this.hash;
		    $('html,body').animate({scrollTop:$(this.hash).offset().top}, 500, '', function(){ location.hash = hash;});
        });

        //update active project in nav menu

        $(".prt-project").waypoint(function(event,direction){
                $('.prt-nav-link').removeClass('active');
                var id = $(this).attr('id');
                if(direction == 'down'){
                    $('.prt-nav-link a[href=#'+id+']').parent().addClass('active');
                }
                else{
                    $('.prt-nav-link a[href=#'+id+']').parent().removeClass('active');
                    $('.prt-nav-link a[href=#'+id+']').parent().prev().addClass('active');
                }
        },{offset: '50' });

        $(".prt-project .description img").fadeTo(0,0);
       
        $(".prt-project .description img").waypoint(function(event,direction){
                src = $(this).src
                if(src == undefined){
                    new_src = $(this).attr('data-src');
                    $(this).attr('src', new_src);
                    $(this).fadeTo(300,1);
                }
                else{
                    $(this).fadeTo(0,1);
                }
        },{offset: '70' });

        //control visiblity of quick navigation menu 

         $("#prt-projects").waypoint(function(event,direction){
            if(direction =='down'){
                $('#quick-nav').removeClass('hide');
            }
         },{offset: '20%' });


         $("#prt-gallery").waypoint(function(event,direction){
            if(direction == 'up'){
                $('#quick-nav').addClass('hide');
            }  
         },{offset: '-20%' });

         
         $('#quick-nav-toggle').click(function(event){
		     event.preventDefault();
             $('#quick-nav').toggleClass('min');
         });


         /* slideshow */

         

        // disable the dragging of images on desktop browsers
        $(".prt-slideshow-container").children().bind("dragstart", function() { 
            return false; 
        });


        /**
        * super simple slideshow
        * animation between slides happens with css transitions
        */
        function Slideshow(container, overview)
        {
            container = $(container);
            overview = $(overview);

            var slides = $(">li", container);
            var width = container.parent().width();

            var self = this;
            var current = 0;
            var total_slides = slides.length;

            // overview dots
            overview.click(function(ev) {    
                self.slideTo( $(this).index() );
                ev.preventDefault();
            });

            this.updateOverview = function() {
                overview.removeClass("active");
                $(overview.get( current )).addClass('active');
            };
            self.updateOverview();


            // slide to given index
            this.slideTo = function( index ) {
                if(index > total_slides-1) {
                    index = total_slides-1;
                } 
                else if(index < 0) {
                    index = 0;
                } 

                if(index == current) {
                    return false;
                }

                container.css({ left: 0 - (width * index) });
                current = index;


                self.updateOverview();

                return true;
            };

            this.next = function() {
                return this.slideTo(current+1);	
            };

            this.prev = function() {
                return this.slideTo(current-1);	
            };

            this.getContainer = function() {
                return container;
            };

            this.getCurrent = function() {
                return $(slides.get(current));
            };
        }



        var hammer = new Hammer($(".prt-slideshow-container").get(0));
        var slideshow = new Slideshow(".prt-slideshow-container ul", "#overview li");


        // ondrag we preview the next/prev slide
        hammer.ondrag = function(ev) {
            var left = 0;

            // determine which direction we need to show the preview
            if(ev.direction == 'left') {
                left = 0 - ev.distance;
            } else if(ev.direction == 'right') {
                left = ev.distance;
            }

            // just move the marginLeft
            slideshow.getContainer().css({ marginLeft: left });
        };


        // ondragend we will move to the next/prev slide when we have 
        // opened it more then 100px on the screen
        hammer.ondragend = function(ev) {
            // restore the margin
            slideshow.getContainer().css({ marginLeft: 0 });
                
                
            
            // if we moved the slide 100px then navigate
            if(Math.abs(ev.distance) > 100) {
                if(ev.direction == 'right') {
                    slideshow.prev();
                } else if(ev.direction == 'left') {
                    slideshow.next();
                }
            }
        };

    
        
});
