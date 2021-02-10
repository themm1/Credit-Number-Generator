$(document).ready(function() {

	$('#generate').on('submit', function(event) {

		$.ajax({
            data : {
                brand : $('#brand').val()
            },
			type : 'POST',
			url : '/generate'
		})
        .done(function(data) {
			$('#generatedNumber').text(data.number).show();
		});
		event.preventDefault();

	});

});