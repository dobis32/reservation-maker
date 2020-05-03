let firstName = document.querySelector('#first-name');
let lastName = document.querySelector('#last-name');
let address = document.querySelector('#address');
let newsletter = document.querySelector('#newsletter');
let clientId = document.querySelector('#client-id');
let reservationId = document.querySelector('#reservation-id');

const toggleVerificationError = {
	on: function() {
		document.querySelector('#verification-error').style.display = 'block';
	},
	off: function() {
		document.querySelector('#verification-error').style.display = 'none';
	}
};

async function debug() {
	toggleVerificationError.off();
	response = await postData('/reservations/confirm', { id: reservationId.value });
	if (response.result) location.href = `/reservations/confirm/success?id=${reservationId.value}`;
	else toggleVerificationError.on();
}

async function submitInfo() {
	toggleVerificationError.off();
	if (validateInfo([ firstName, lastName, address ])) {
		let response = await postData('/clients/verify', {
			firstName: firstName.value,
			lastName: lastName.value,
			address: address.value,
			newsletter: newsletter.checked,
			client: clientId.value
		});
		if (!response.result) toggleVerificationError.on();
		else {
			response = await postData('/reservations/confirm', { id: reservationId.value });
			console.log(response);
			if (response.result) {
				location.href = `/reservations/confirm/success?id=${reservationId.value}`;
			} else toggleVerificationError.on();
		}
	}
}

function validateInfo(inputs) {
	inputs.forEach((input) => {
		input.classList.remove('invalid');
	});
	let returnValue = true;
	inputs.forEach((input) => {
		if (!input.value.length) {
			input.classList.add('invalid');
			returnValue = false;
		}
	});
	return returnValue;
}
