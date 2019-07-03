

$(document).ready(function(){

    
	console.log("baselogin.js cargado");
    $('#login').click(function(){


        console.log("iniciando sesion...");
    
        var email = $("#exampleInputEmailIniciarSesion").val();
        var password = $("#exampleInputPasswordIniciarSesion").val();
        if (email == '' || password == '') {
        alert("Por favor completa todos los campos...!!!!!!");
        }
        
        else if(email.indexOf('@', 0) == -1 || email.indexOf('.', 0) == -1){
            alert("Por favor ingrese un correo válido...!!!!!!");

        }
        
        else{
            
            $.ajax({
                url: "http://127.0.0.1:8000/login/",
                method: 'POST', // or another (GET), whatever you need
                //contentType: 'application/json; charset=utf-8',
                data: {'email':email,
                        'password':password
                        }, 
                success: function (data) {        
                    // success callback
                    // you can process data returned by function from views.py
                    arr=data.split("-");
                    rpta=arr[0];
                    name=arr[1];
                    surname=arr[2];
                    if(rpta=="existe"){
                        alert("Bienvenido "+name+" "+surname);
                        $('.remove').empty();
                        $('.user').html(name+" "+surname);
                        $('.cerrar').html("Cerrar Sesion");

                        //window.location.href = 'http://127.0.0.1:8000/'

                    }
                    else{
                        alert("Usuario no existente");
                    }
                }
            });
         
        }
			
    });
	

});