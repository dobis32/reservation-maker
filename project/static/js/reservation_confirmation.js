const id = document.querySelector('#reservation-id').value;
let animate = true;
postData('/reservations/confirm', { id }).then((response) => {
	console.log(response);
	if (response.result) {
		document.querySelector('#loading-message').style.display = 'none';
		animate = false;
		location.href = `/reservations/confirm/success?${id}`;
	} else {
		document.querySelector('#loading-message').style = 'display: none;';
		document.querySelector('#confirmation-failure').style = 'display: block;';
		animate = false;
	}
});
const loading = document.querySelector('#loading');
async function loadingAnimationNextFrame() {
	setTimeout(() => {
		let i = loading.innerHTML.length % 4;
		loading.innerHTML = '';
		while (loading.innerHTML.length <= i) loading.innerHTML += '.';
		if (animate) loadingAnimationNextFrame();
	}, 500);
}
loadingAnimationNextFrame();
