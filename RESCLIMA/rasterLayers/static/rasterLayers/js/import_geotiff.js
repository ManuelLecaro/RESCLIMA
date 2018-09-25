function renderError(error){
	errorMsg.innerHTML = '<div class="red"><b>' + error + '</b></div>'
	var progressContainer = document.getElementById("progress-container");
	progressContainer.style.visibility = "hidden";
	window.scrollTo(0, 0);
}

// crea un objeto xmlhttprequest 
// con el evento upload.progress
function createXHR(){
	var xhr = new window.XMLHttpRequest();
	
	// este evento mostrara el progreso de la subida
	// de los datos
	xhr.upload.addEventListener("progress",function(evt){
	if (evt.lengthComputable){
		// hace visible el contenedor de la barra de progreso
		var progressContainer = document.getElementById("progress-container");
		progressContainer.style.visibility = "visible";
		var percentComplete = evt.loaded / evt.total;
		percentComplete = parseInt(percentComplete * 100);
		var percentComplete_str = String(percentComplete) + "%"
		uploadPercent.style.width = percentComplete_str;
		if (percentComplete === 100){
			uploadPercentLabel.innerText = "Completado, espere por favor";
			return;
		}
		uploadPercentLabel.innerText = "Subiendo " + percentComplete_str;
	}
	},false);
	return xhr;
}

// se ejecuta cuando la subida de los datos
// es exitosa
function successHandler(data){
	if(data=="OK"){
		window.location = "/raster"
	}
	else{
		renderError(data);
	}
}

// se ejecuta si ocurre un error en la subida el form
function errorHandler(data){
	status = String(data.status);
	msg = "Ha ocurrido un error " + status+ " en el servidor"
	renderError(msg);
}

// obtiene el string de categorias
function getCategoriesString(){
	categories_string = "";
	nodes = document.querySelectorAll("#categories .selected");
	for(var i=0; i<nodes.length; i++){
		var node = nodes[i];
		categories_string += node.innerText + " ";
	}
	categories_string = categories_string.slice(0, -1);
	return categories_string;
}

// revisa las condiciones de los
// archivos
function checkFile(){
	var file_input = document.getElementById("id_import_file");
	var list_files = file_input.files;
	var fileName = list_files[0].name

	var parts = fileName.split(".");

	if(parts.length!=2){
		return "El archivo debe tener extension y no contener puntos en el nombre" 
	}
	// se obtiene el nombre y extension del archivo
	var fname = parts[0].toLowerCase();
	var extension = parts[1].toLowerCase();

	if(extension!="tiff" & extension!="tif"){
		return "La extension debe ser tif"
	}
	return null;
}

// se ejecuta cuando se da click en una categoria
function markCategory(event){
	var category = event.target;
	var classCategory = category.className;
	if(classCategory.indexOf("selected") !== -1){
		category.className = "chip z-depth-3"
	}else{
		category.className = "chip z-depth-3 cyan selected"
	}
}

// se ejecuta cuando se hace submit
// al form
function formSubmit(e){
	e.preventDefault(e);
	
	var formImport = $("#rasterForm");
	// se obtiene los datos del formulario
	var data = new FormData(formImport.get(0));
	// se obtiene el string de categorias
	var categories_string = getCategoriesString();
	data.append("categories_string",categories_string);

	// se checkean las condiciones de los archivos
	var result = checkFile();
	if(result){
		alert(result);
		return;
	}

	// se envian los datos al servidor
	$.ajax({
		type: formImport.attr('method'),
		url: formImport.attr('action'),
		data: data,
		processData: false,
		contentType: false,
		xhr: createXHR,
		success: successHandler,
		error: errorHandler
	});
	return false;
}

$(document).ready(function() {
	document.getElementById('data_date').valueAsDate = new Date();
	var formImport = $("#rasterForm");
	formImport.submit(formSubmit);
});