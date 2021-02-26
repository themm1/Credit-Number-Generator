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
		event.preventDefault();
	  
		$.ajax({
		  	data: {
				brand: $('#brand').val(),
				count: $('#count').val(),
				data_format: $('#data_format').val()
		  	},
		  	type: 'POST',
		  	url: '/file_generator'
		})
		
		.done(function(data) {
		  	textarea = document.getElementById('textarea')
			file_format = data.file_format
		  	if (file_format == 'csv' || file_format == 'xml') {
				textarea.value = data.file;
		  	} 
		  	else {
				textarea.value = JSON.stringify(data.file, null, 2);
		  	}
		});
	});
	  
	
	$('#download').on('click', function() {
		var text = $('#textarea').val().replace(/\n/g, '\r\n');
		var blob = new Blob([text], { type: 'text/plain' });
		$(`<a download="creditnumbers.${file_format}" href="${window.URL.createObjectURL(blob)}
		"target="_blank" style="display: none;">`).appendTo(document.body)[0].click().remove();
	});
});