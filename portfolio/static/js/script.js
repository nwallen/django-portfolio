/* Author:
Nicholas Wallen
*/

jQuery(document).ready(function($) {
 
	$(".scroll").click(function(event){		
		event.preventDefault();
                var hash =  this.hash;
		$('html,body').animate({scrollTop:$(this.hash).offset().top}, 500, '', function(){ location.hash = hash;});
        });

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
        


});




