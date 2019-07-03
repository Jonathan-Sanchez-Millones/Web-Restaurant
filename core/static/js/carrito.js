$(document).ready(function(){
	console.log("carrito.js cargado");
	console.log("ctmre");
    $('.quitar').click(function(){

		var nombre_plato=$(this).parent().parent().find('.nombre').text(); 
        
        console.log(nombre_plato);

        $.ajax({
			url: "http://127.0.0.1:8000/deleteproducto/",
			method: 'POST', // or another (GET), whatever you need
			data: {'nombre': nombre_plato}, 
			success: function (data) {        
				// success callback
				// you can process data returned by function from views.py
				console.log("Si entra");
				window.location.href = 'http://127.0.0.1:8000/carrito/'
			}
		});
			
			
	});
	
	$('.actualizar').click(function(){

		//1 ra parte (Perfect)
		var nombres=$(this).parent().parent().find('.nombre'); 
		var cantidades=$(this).parent().parent().find('.cant option:selected'); 

		console.log("Actualizar?");
		console.log(nombres);
		console.log(cantidades);
		var productos=[];
		for(var i=0;i<nombres.length;i++){

				var producto={nombre:$(nombres[i]).text(),
							cantidad:$(cantidades[i]).text()};
				productos.push(producto);

			

		}
		console.log(productos);

	//2 da parte
		productos=JSON.stringify({'productos':productos});
		var datos={'gaaa':"Bota tu ga"};
		datos=JSON.stringify(datos);
		$.ajax({
			contentType: 'application/json; charset=utf-8',
			dataType: 'json',
			type: 'POST', // or another (GET), whatever you need
			url: "http://127.0.0.1:8000/updatecarrito/",
			
			data: productos, 
			
			success: function (data) {        
				// success callback
				// you can process data returned by function from views.py
				console.log("Si entra 2");
				window.location.href = 'http://127.0.0.1:8000/carrito/'
			}
		});
			

			

		
        
    });
	

});