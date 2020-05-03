document.querySelectorAll('li').forEach((li) => {
	li.addEventListener('click', (event) => {
		location.href = event.target.getAttribute('href');
	});
});

// const today = new Date();
// let month = today.getMonth() + 1; // JS months go from 0-11; py dates go from 1-12
// let calendarDate = today.getDate();
// let year = today.getFullYear();

// const upcomingReservationBadge = document.querySelector('#upcoming-reservations-badge');
// const newReservationBadge = document.querySelector('#new-reservations-badge');
// const cancelledReservationBadge = document.querySelector('#cancelled-reservations-badge');
// let date = `${month}-`;
// date += `${calendarDate < 10 ? '0' + calendarDate.toString() : calendarDate}-`;
// date += `${year - 2000}`;
// postDataWAdmin('/admin/dashboard', { date })
// 	.then((response) => {
// 		console.log(response);
// 		if (response.result) {
// 			upcomingReservationBadge.innerHTML =
// 				upcomingReservationBadge.innerHTML.split(' ')[0] + ` ${response.reservations.upcoming}`;
// 			newReservationBadge.innerHTML = `${response.reservations.new}`;
// 			cancelledReservationBadge.innerHTML = `${response.reservations.cancelled}`;
// 		} else throw Error('Could not retrieve dashboard data', response.message);
// 	})
// 	.catch((error) => {
// 		console.log('Failed to get notification data', error);
// 	});
