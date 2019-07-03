$(document).ready(function(){
	console.log("promociones.js cargado");
	console.log("ctmre");
    $('.carrito').click(function(){

		var nombre_promocion=$(this).parent().parent().find('.nombre').val(); 
		var cantidad_promocion=$(this).parent().parent().find('.cantidad option:selected').text(); 

		console.log(nombre_promocion);
		console.log(cantidad_promocion);
        
		$.ajax({
			url: "http://127.0.0.1:8000/addcarrito/",
			method: 'POST', // or another (GET), whatever you need
			data: {'nombre': nombre_promocion,'cantidad':cantidad_promocion}, 
			success: function (data) {        
				// success callback
				// you can process data returned by function from views.py
				window.location.href = 'http://127.0.0.1:8000/promociones/'
			}
		});	
    });
	

});