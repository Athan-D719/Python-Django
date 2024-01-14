var nodosp=document.getElementsByTagName("td"); //Se obtienen los elementos con la estiquetas "TagName":<p></p>.
alert(nodosp.length); // Me muestra una alerta con el nuer de elemntos recibidos.
for(var i=0; i < nodosp.length; i++){
	var contenido = nodosp[i].innerHTML; //Estamos obteniendo el valor nodosp en la ["posición"] del HTML(.innerHTML).
	alert(contenido);
};
nodosp[0,0].innerHTML="Lunes"; //Aquí estoy cambiendo los valores con respecto a la posicíon dependiendo de la fila.
nodosp[0,1].innerHTML="Martes";		//En estos casos[0,1,2....], Se reemplazan por los valores que ingresé.
nodosp[0,2].innerHTML="Miercoles";
nodosp[0,3].innerHTML="Jueves";
nodosp[0,4].innerHTML="Viernes";
nodosp[0,5].innerHTML="Sabado";
nodosp[0,6].innerHTML="Domingo";
