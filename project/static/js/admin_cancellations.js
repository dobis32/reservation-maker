console.log('admin cancellations');
async function dismissNotification(n) {
	let response = await putData('/admin/reservations/dismiss', { id: n });
	if (response.result) location.reload();
	else console.log(new Error('failed to dismiss notification'));
}
