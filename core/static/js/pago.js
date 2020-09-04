$(document).ready(function(){
	console.log("pago.js cargado");
    console.log("ctmre");
    var radioValue="Efectivo";
    $('.continuar').click(function(){

        console.log("me presionate");
        

        $(this).parent().parent().parent().find('.activar').removeClass("div-disabled"); 
        
    });

    $("input[type='radio']").click(function(){
        radioValue = $("input[name='exampleRadios']:checked").val();
        console.log(radioValue);
    });

    $('.continuar5').click(function(){

        console.log("me presionate 1.5");
        console.log(radioValue);
        

        //$(this).parent().parent().parent().parent().parent().find('.activar2').removeClass("div-disabled"); 
        //$('#exampleModalTarjeta').empty()

        
        
    });

    $('.continuar2').click(function(){

        console.log("me presionate 2");
        var numero="";
        numero=$('#exampleInputNumeroTarjeta').val();
        console.log(numero);
        var cvv="";
        cvv=$('#exampleInputCodigo').val();
        console.log(cvv);
        $(this).parent().parent().parent().parent().parent().find('.activar2').removeClass("div-disabled"); 
        //$('#exampleModalTarjeta').empty()
        if(numero=='' || cvv==''){
            alert("Por favor completa todos los campos!");
        }
        else if(numero.length!=16){
            alert("Por favor ingrese un numero de tarjeta válido...!!!!!!");

        }
        else if(cvv.length!=3){
            alert("Por favor ingrese correctamente el codigo de seguridad de la tarjeta!");

        }
        else{
            alert("Registro exitoso de su tarjeta "+radioValue);

            $('#exampleModalTarjeta').modal("hide");

        }

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