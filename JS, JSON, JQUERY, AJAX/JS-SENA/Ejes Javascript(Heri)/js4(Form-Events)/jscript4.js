function mostrar(){
	var can = parsInt(document.getElementById("cantidad").value);
	var html="";
	for (var i = 0; i < can; i++) {
		html = html+1; 
		}
		document.getElementById("parrafos").innerHTML ="El resultado es: "+html;
	}