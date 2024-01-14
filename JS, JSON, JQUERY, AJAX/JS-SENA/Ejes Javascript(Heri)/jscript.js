var nodosp=document.getElementsByTagName("p"); //Se obtienen los elementos con la estiquetas "TagName":<p></p>.
alert(nodosp.length); // Me muestra una alerta con el nuer de elemntos recibidos.
for(var i=0; i < nodosp.length; i++){
	var contenido = nodosp[i].innerHTML; //Estamos obteniendo el valor nodosp en la ["posición"] del HTML(.innerHTML).
	alert(contenido);
};
nodosp[0].innerHTML="Amarillo" //Aquí estoy cambiendo los valores con respecto a la posicíon dependiendo de la fila.
nodosp[1].innerHTML="Azul"		//En estos casos[0,1,2....], Se reemplazan por los valores que ingresé.
nodosp[2].innerHTML="Rojo"