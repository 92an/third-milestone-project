  $(document).ready(function(){
    // sidenav functionality materialize
    $(".sidenav").sidenav({edge: "right"});

    // Carousel functionality materialize
    $('.carousel').carousel({
        numVisible: 1,
        fullWidth: true,
        indicators: true
    });

        // function that will automate the carousel
        setInterval(function(){
            $('.carousel').carousel('next');
        }, 12000);

    // Dropdown functionality materialize
    $(".dropdown-trigger").dropdown();
  });