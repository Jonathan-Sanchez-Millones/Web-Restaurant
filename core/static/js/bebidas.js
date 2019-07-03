$(document).ready(function(){
	console.log("bebidas.js cargado");
	console.log("ctmre");
    $('.carrito').click(function(){

		var nombre_bebida=$(this).parent().parent().find('.nombre').val(); 
		var cantidad_bebida=$(this).parent().parent().find('.cantidad option:selected').text(); 

		console.log(nombre_bebida);
		console.log(cantidad_bebida);
        
        $.ajax({
			url: "http://127.0.0.1:8000/addcarritobebida/",
			method: 'POST', // or another (GET), whatever you need
			data: {'nombre': nombre_bebida,'cantidad':cantidad_bebida}, 
			success: function (data) {        
				// success callback
				// you can process data returned by function from views.py
				window.location.href = 'http://127.0.0.1:8000/bebidas/'
			}
		});
			
    });
	

});