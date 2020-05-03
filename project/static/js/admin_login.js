console.log('admin login');
const username = document.querySelector('#username');
const password = document.querySelector('#password');

const toggleLoginError = {
	on: function() {
		document.querySelector('#login-error-message').style.display = 'block';
	},
	off: function() {
		document.querySelector('#login-error-message').style.display = 'none';
	}
};

function setInputError(selector) {
	document.querySelector(selector).classList.add('input-error');
}

function clearnInputErrors() {
	document.querySelectorAll('input').forEach((input) => {
		input.classList.remove('input-error');
	});
}

async function login() {
	toggleLoginError.off();
	clearnInputErrors();
	if (!username.value) {
		console.log('invalid username');
		toggleLoginError.on();
		setInputError('#username');
	} else if (!password.value) {
		console.log('invalid password');
		toggleLoginError.on();
		setInputError('#password');
	} else {
		let response = await postData('/admin/login', { username: username.value, password: password.value });
		console.log(response);
		if (response.result) {
			sessionStorage.setItem('adminToken@resv_maker', response.token);
			console.log('user has logged in successfully');
			location.href = '/admin/dashboard';
		} else {
			toggleLoginError.on();
		}
	}
}
