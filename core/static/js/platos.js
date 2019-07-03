$(document).ready(function(){
	console.log("platos.js cargado");
	console.log("ctmre");
    $('.carrito').click(function(){

		var nombre_plato=$(this).parent().parent().find('.nombre').val(); 
		var cantidad_plato=$(this).parent().parent().find('.cantidad option:selected').text(); 

		console.log(nombre_plato);
		console.log(cantidad_plato);
        
        $.ajax({
			url: "http://127.0.0.1:8000/addcarritoplato/",
			method: 'POST', // or another (GET), whatever you need
			data: {'nombre': nombre_plato,'cantidad':cantidad_plato}, 
			success: function (data) {        
				// success callback
				// you can process data returned by function from views.py
				window.location.href = 'http://127.0.0.1:8000/platos/'
			}
		});
			
    });
	

});