function mostrar(){
	var cantidad = parseInt(document.getElementById("cantidad").value);

	var contenido="";
	for(var i=1; i<=cantidad; i++) {
		contenido = contenido + "<input type='radio' name='juego'>Radio" + i + "<br>";
		//Contador que me muestra dependiendo del numero del select un 'Radio' y el acumulado 'i': 1..2..3..4
		//Con mostrar me muestra tambien el numero de 'Radio's dependiendo el select.
	}
	document.getElementById("contenedor").innerHTML=contenido; //Muestra el 'contenido' en el HTML
	//The innerHTML property sets or returns the HTML content (inner HTML) of an element.

	document.getElementById("contenedor").style.display="block";
}
function ocultar(){
	document.getElementById("contenedor").style.display="none";
}
function cambio()
{
	if(document.getElementById("piedra").checked) //cheked: Pasa al seleccionar el elemento.
	  {
	  	alert("Piedra"); //Mensaje que muestra el mensaje en un script de que ha seleccionado.
	  }
	   if(document.getElementById("papel").checked)
	  {
		alert("Papel");
	  }
	  if(document.getElementById("tijera").checked)
	  {
	  	alert("Tijera");
	  }
}