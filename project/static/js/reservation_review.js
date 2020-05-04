console.log('reservation review');

const dateBuffer = document.querySelector('#date-buffer');
const dateSpan = document.querySelector('#date-span');
dateSpan.innerHTML = dateBuffer.value.split('-').join('/');

const timeBuffer = document.querySelector('#time-buffer');
const timeSpan = document.querySelector('#time-span');
const timeTokens = timeBuffer.value.split('-');
timeSpan.innerHTML = `${timeTokens[0]}:${timeTokens[1]} ${timeTokens[2]}`;

const toggleErrorMessage = {
	on: function() {
		document.querySelector('#cancellation-error').style.display = 'block';
	},
	off: function() {
		document.querySelector('#cancellation-error').style.display = 'nonce';
	}
};

function cancellationSuccess() {
	document.querySelector('#cancellation-success').style.display = 'block';
	document.querySelector('#cancel-button').style.display = 'none';
}

async function cancelReservation() {
	if (confirm('Are you sure you want to cancel your reservation?')) {
		toggleErrorMessage.off();
		const nonce = document.querySelector('#nonce-buffer').value;
		const response = await deleteData('/reservations/review', { reservation: nonce });
		console.log(response);
		if (response.result) cancellationSuccess();
		else toggleErrorMessage.on();
	}
}
