  $(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $('.carousel').carousel({
        numVisible: 1,
        fullWidth: true,
        indicators: true
    });
        // function that will automate the carousel
        setInterval(function(){
            $('.carousel').carousel('next');
        }, 12000);
  });