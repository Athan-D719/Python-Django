function mostrar(){
	var cantidad = parseInt(document.getElementById("cantidad").value);
	var cantidad1 = parseInt(document.getElementById("cantidad1").value);

	var contenido="";
	var contenido1="";

	for(var i=1; i<=cantidad; i++) {
		contenido = contenido + "<input type='radio' name='juego'>Radio" + i;
		//Contador que me muestra dependiendo del numero del select un 'Radio' y el acumulado 'i': 1..2..3..4
		//Con mostrar me muestra tambien el numero de 'Radio's dependiendo el select.
		for(var a=1; a<=cantidad1; a++) {
		contenido1 = contenido1 + "<input type='radio' name='juego'>Radio" + a+"<br>";
		//Contador que me muestra dependiendo del numero del select un 'Radio' y el acumulado 'i': 1..2..3..4
		//Con mostrar me muestra tambien el numero de 'Radio's dependiendo el select.

	}
	}

	
	document.getElementById("contenedor").innerHTML=contenido; //Muestra el 'contenido' en el HTML
	//The innerHTML property sets or returns the HTML content (inner HTML) of an element.

	document.getElementById("contenedor").innerHTML=contenido1; //Muestra el 'contenido' en el HTML
	//The innerHTML property sets or returns the HTML content (inner HTML) of an element.


	document.getElementById("contenedor").style.display="block";
}
function ocultar(){
	document.getElementById("contenedor").style.display="none";
}
