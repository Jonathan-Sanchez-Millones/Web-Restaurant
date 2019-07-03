$(document).ready(function(){
	console.log("base.js cargado");
    $('#registro').click(function(){


        console.log("registrando...");
        var nombres = $("#exampleInputNombresRegistrarse").val();
        var apellidos = $("#exampleInputApellidosRegistrarse").val();
        var email = $("#exampleInputEmailRegistrarse").val();
        var password = $("#exampleInputPasswordRegistrarse").val();
        var direccion=$("#exampleInputDireccionRegistrarse").val();
        if (nombres == '' || email == '' || password == '' || apellidos == '' || direccion == '') {
        alert("Por favor completa todos los campos...!!!!!!");
        }
        
        else if(email.indexOf('@', 0) == -1 || email.indexOf('.', 0) == -1){
            alert("Por favor ingrese un correo válido...!!!!!!");

        }
        else{
            alert("Bien hecho "+nombres);

            $.ajax({
                url: "http://127.0.0.1:8000/register/",
                method: 'POST', // or another (GET), whatever you need
                data: {'nombres': nombres,'apellidos':apellidos,'email':email,
                        'password':password,'direccion':direccion
                        }, 
                success: function (data) {        
                    // success callback
                    // you can process data returned by function from views.py
                    console.log(data);
                    //window.location.href = 'http://127.0.0.1:8000/platos/'
                }
            });
        }
		
			
    });
	

});