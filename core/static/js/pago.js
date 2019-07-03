$(document).ready(function(){
	console.log("pago.js cargado");
	console.log("ctmre");
    $('.continuar').click(function(){

        console.log("me presionate");
        

        $(this).parent().parent().parent().find('.activar').removeClass("div-disabled"); 
        
    });

    $('.continuar2').click(function(){

        console.log("me presionate");
        

        $(this).parent().parent().parent().parent().parent().find('.activar2').removeClass("div-disabled"); 
        //$('#exampleModalTarjeta').empty()

    });

    $('#finalizar').click(function(){

        console.log("me presionateeeeeee");

        $('#tt2').removeAttr( 'style' );

        setTimeout(
            function() 
            {
                $.ajax({
                    url: "http://127.0.0.1:8000/deletecarrito/",
                    method: 'POST', // or another (GET), whatever you need
                    success: function (data) {        
                        // success callback
                        // you can process data returned by function from views.py
                        console.log(data)
                        window.location.replace('http://127.0.0.1:8000/promociones/');

                    }
                });
            }, 6000);

            

        

        //$('#exampleModalTarjeta').empty()

    });
	

});