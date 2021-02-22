$(document).ready(function() {

	$(".message").css('visibility', 'hidden');
	$('select').selectpicker();


	$(document).on('click', '.nav-item a', function () {
        $(this).parent().addClass('active').siblings().removeClass('active');
    });


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
});