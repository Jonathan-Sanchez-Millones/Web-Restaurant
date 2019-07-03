$(document).ready(function(){
	console.log("entradas.js cargado");
	console.log("ctmre");
    $('.carrito').click(function(){

		var nombre_entrada=$(this).parent().parent().find('.nombre').val(); 
		var cantidad_entrada=$(this).parent().parent().find('.cantidad option:selected').text(); 

		console.log(nombre_entrada);
		console.log(cantidad_entrada);
        
        $.ajax({
			url: "http://127.0.0.1:8000/addcarritoentrada/",
			method: 'POST', // or another (GET), whatever you need
			data: {'nombre': nombre_entrada,'cantidad':cantidad_entrada}, 
			success: function (data) {        
				// success callback
				// you can process data returned by function from views.py
				window.location.href = 'http://127.0.0.1:8000/entradas/'
			}
		});
			
    });
	

});