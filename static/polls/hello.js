$(function () {
	init();
	bindEvent();

	function init() {
		sayHello();
	}

	function sayHello() {
		console.log('Hello world');
	}

	function bindEvent() {
		$('.post').on('click', function (event) {
			sendMessage();
		});
	}


	function sendMessage() {
		let url = '/polls/post/message/'
		$.ajax({
			url: url,
			method: 'POST',
			dataType: 'json',
			data: {
				name: 'test',
				id: 123
			},
			success: function (res) {
				console.log(res);
			},
			error: function (xhr) {
				console.log(xhr);
			}
		})
	}
});
