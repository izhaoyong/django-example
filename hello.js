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

		$('.file-uploader').on('change', function (event) {
			uploadFile();
		});
	}


	function uploadFile() {
		let file = $('.file-uploader')[0].files[0];
		console.log(file.name);

		let formData = new FormData()
		formData.append('file', file);
		formData.append('name', 'haha');

		let url = '/polls/file/upload/'
		var xhr = new XMLHttpRequest;
		xhr.open('post', url);
		xhr.onreadystatechange = function (res) {
			if (xhr.readyState == 4 && xhr.status == 200) {
				console.log(xhr.response);
			}
		}
		xhr.send(formData);
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
