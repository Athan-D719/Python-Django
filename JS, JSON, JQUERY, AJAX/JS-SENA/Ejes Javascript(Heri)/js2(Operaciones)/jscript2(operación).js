var nodosp=document.getElementsByTagName("p"); //Se obtienen los elementos con la estiquetas "TagName":<p></p>.
var suma = 0;
alert(nodosp.length); // Me muestra una alerta con el nuer de elemntos recibidos.
for(var i=0; i < nodosp.length; i++){
	var numero = parseInt(nodosp[i].innerHTML); //Se obtiene como un entero el valor o los valores ingresados
	suma = suma + numero;
};
document.getElementById("resultado").innerHTML="El resultado es: "+suma; //Se obtiene por id el "resultado" del html(.innerHTML); y se concatena.
																		 //Recordar "Element" no "Elements" 