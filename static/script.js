$(document).ready(function() {

	$(".message").css('visibility', 'hidden');
	$('select').selectpicker();


	$('#generate').on('submit', function(event) {
		$.ajax({
			data : {
				brand : $('#brand').val()
			},
			type : 'POST',
			url : '/generate'
		})

		.done(function(data) {
			$('#generatedNumber').text(data.number).css('visibility', 'visible');
		});
		event.preventDefault();
	});

	
	$('#validate').on('submit', function(event) {
		$.ajax({
			data : {
				number : $('#number').val()
			},
			type : 'POST',
			url : '/validate'
		})

		.done(function(data) {
			$('#validatedNumber').text(data.message).css('visibility', 'visible');;
		});
		event.preventDefault();
	});


	$('#file_generator').on('submit', function(event) {
		$.ajax({
			data: {
				brand: $('#brand').val(),
				count: $('#count').val(),
				data_format: $('#data_format').val()
			},
			type : 'POST',
			url : '/file_generator'
		})

		.done(function(data) {
			if (data.data_format == 'csv' || data.data_format == 'xml') {
				$('textarea').text(data.file);
			}
			else {
				$('textarea').text(JSON.stringify(data.file, null, 2));
			}
		});
		event.preventDefault();
	});


	$('#download').on('click', function() {
		download(`creditnumbers.${$('#data_format').val()}`)
	});
});


function download(name){
    var text = document.getElementById("textarea").value;
    text = text.replace(/\n/g, "\r\n");
    var blob = new Blob([text], { type: "text/plain"});
    var anchor = document.createElement("a");
    anchor.download = name;
    anchor.href = window.URL.createObjectURL(blob);
    anchor.target ="_blank";
    anchor.style.display = "none";
    document.body.appendChild(anchor);
    anchor.click();
    document.body.removeChild(anchor);
 }