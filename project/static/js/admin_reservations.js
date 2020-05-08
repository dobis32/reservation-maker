console.log('admin reservations');
function applyFilter() {
	const notifyAdmin = document.querySelector('#notify-admin');
	// const cancelled = document.querySelector('#cancelled');
	const unconfirmed = document.querySelector('#unconfirmed');
	let filterURL = `/admin/reservations?`;
	filterURL += `notify_admin=${notifyAdmin.checked ? 'True' : 'False'}`;
	// filterURL += `&cancelled=${cancelled.checked ? 'True' : 'False'}`;
	filterURL += `&unconfirmed=${unconfirmed.checked ? 'True' : 'False'}`;
	location.href = filterURL;
}

async function dismissNotification(n) {
	let response = await putData('/admin/reservations/dismiss', { id: n });
	if (response.result) location.reload();
	else console.log(new Error('failed to dismiss notification'));
}

function review(resv_nonce) {
	location.href = `/reservations/review?reservation=${resv_nonce}`;
}
