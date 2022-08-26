$(function() {
    $('p').click(function() {

        $('p').animate({ 'left': '800px', 'fontSize': '30px', 'color': 'red', 'marginBottom': '200px', 'fontFamily': 'sans serif' }, 6000);
        $('p').css('color', 'red');
        $('p').addClass('border raduis');



    })

})