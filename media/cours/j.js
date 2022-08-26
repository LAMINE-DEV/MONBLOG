$(function() {
    var btn = $('button').click(function() {

        var input_name = $('input[name=prenom]').val() == "";
        if (input_name) {
            var image = "<img src='t.jpg'/>";
            $('body').html(image);
        } else {
            var image = "<img src='t.jpg'/>";
            $('.ima').html(image);
        }
    });
    $('#exampleCheck1').change(function() {


        swal("vous avez cohez la case", "error");
        $('#exampleInputPassword1').hide();
        $('body').css('background-color', 'yellow');

    })
});