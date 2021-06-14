(function($){
    $(document).ready(function(){  
       $("#cssmenu").menumaker({
          title: "Menu",
          breakpoint: 800,
          format: "multitoggle",
          import: "nav.html"
        });       
    });
  })(jQuery);
  