const todayDate = new Date();

function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = cookies[i].trim();
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === name + '=') {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

async function postData(url = '', data = {}, headers = { 'Content-Type': 'application/json' }) {
	// Default options are marked with *
	const response = await fetch(url, {
		method: 'POST', // *GET, POST, PUT, DELETE, etc.
		mode: 'cors', // no-cors, *cors, same-origin
		cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
		credentials: 'same-origin', // include, *same-origin, omit
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': getCookie('csrftoken')
		},
		redirect: 'follow', // manual, *follow, error
		referrerPolicy: 'no-referrer', // no-referrer, *client
		body: JSON.stringify(data) // body data type must match "Content-Type" header
	});
	return await response.json();
}

async function getData(url = '') {
	// Default options are marked with *
	const response = await fetch(url, {
		method: 'GET', // *GET, POST, PUT, DELETE, etc.
		mode: 'cors', // no-cors, *cors, same-origin
		cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
		credentials: 'same-origin', // include, *same-origin, omit
		// headers: {
		// 	'Content-Type': 'application/json'
		// 	// 'Content-Type': 'application/x-www-form-urlencoded',
		// },
		redirect: 'follow', // manual, *follow, error
		referrerPolicy: 'no-referrer' // no-referrer, *client
	});
	return await response.json();
}

async function initPage() {
	let month = document.querySelector('#month');
	month.selectedIndex = todayDate.getMonth() + 1;
	let year = document.querySelector('#year');
	year.value = todayDate.getFullYear();
	monthChange({ target: { value: month.value, selectedIndex: month.selectedIndex } });
	let date = `${todayDate.getMonth() + 1}-${todayDate.getDate()}-${todayDate.getFullYear().toString().substring(2)}`;
	let locationKey = document.querySelector('#location').value;
	let response = await getData(`/reservations?date=${date}&location=${locationKey}`);
	handleFetchedReservationData(response);
}
initPage();

function generateAvailability(reservations) {
	document.querySelectorAll('.timeslot h1').forEach((timeslot) => {
		timeslot.classList.remove('unavailable');
		timeslot.classList.add('available');
		timeslot.setAttribute('data-toggle', 'modal');
		timeslot.setAttribute('data-target', '#schedule-reservation-modal');
	});

	reservations.forEach((reservation) => {
		let timeslot = document.querySelector(`#T${reservation.time} h1`);
		timeslot.classList.remove('available');
		timeslot.classList.add('unavailable');
		timeslot.removeAttribute('data-toggle');
		timeslot.removeAttribute('data-target');
	});
}

function updateReservationModalInfo(location) {
	document.querySelector('#location-name').innerHTML = location.name;
	document.querySelector('#location-address').innerHTML = location.address;
	document.querySelector('#location-contact').innerHTML = location.contact;
}

function handleFetchedReservationData(response) {
	generateAvailability(response.reservations);
	updateReservationModalInfo(response.location);
}

async function dateChosen() {
	let month = document.querySelector('#month').selectedIndex;
	let day = document.querySelector('#date').value;
	let year = document.querySelector('#year').value - 2000;
	let formattedDate = `${month}-${day}-${year}`;
	let locationKey = document.querySelector('#location').value;
	let response = await getData(`/reservations?date=${formattedDate}&location=${locationKey}`);
	handleFetchedReservationData(response);
}

async function scheduleReservation() {
	console.log('schedule appointment');
	// parse date
	const date = document.querySelector('#date-buffer').value;
	// parse time
	const time = document.querySelector('#time-buffer').value;
	// POST to backend
	let response = await postData(`/reservations`, { date, time });
	// refresh page/redirect to confirmation page
	console.log(response);
}

function setModalBuffers(event) {
	if (event.target.classList.contains('available')) {
		let month = document.querySelector('#month');
		let dateValue = document.querySelector('#date').value;
		let yearValue = document.querySelector('#year').value - 2000;
		document.querySelector('#reservation-date').innerHTML = `${month.value} ${dateValue} ${yearValue}`;
		document.querySelector('#date-buffer').value = `${month.selectedIndex}-${dateValue}-${yearValue}`;
		let time = event.target.id.substring(1, event.target.id.length);
		document.querySelector('#time-buffer').value = time;
		let timeTokens = time.split('-');
		document.querySelector('#reservation-time').innerHTML = `${timeTokens[0]}:${timeTokens[1]} ${timeTokens[2]}`;
	}
}

function removeElementChildren(element) {
	while (element.firstChild) {
		element.removeChild(element.firstChild);
	}
}

function adjustDays(n, isFullMonth) {
	const date = document.querySelector('#date');
	removeElementChildren(date);
	for (let i = 1; i <= n; i++) {
		if (i >= todayDate.getDate() || isFullMonth) {
			const day = document.createElement('option');
			day.value = i;
			day.innerHTML = `${i}`;
			date.appendChild(day);
		}
	}
}

function monthChange(event) {
	const month = event.target.value;
	const isFullMonth = todayDate.getMonth() != event.target.selectedIndex - 1;
	switch (month) {
		case 'JANUARY':
			adjustDays(31, isFullMonth);
			break;
		case 'FEBRUARY':
			adjustDays(28, isFullMonth);
			break;
		case 'MARCH':
			adjustDays(31, isFullMonth);
			break;
		case 'APRIL':
			adjustDays(30, isFullMonth);
			break;
		case 'MAY':
			adjustDays(31, isFullMonth);
			break;
		case 'JUNE':
			adjustDays(30, isFullMonth);
			break;
		case 'JULY':
			adjustDays(31, isFullMonth);
			break;
		case 'AUGUST':
			adjustDays(31, isFullMonth);
			break;
		case 'SEPTEMBER':
			adjustDays(30, isFullMonth);
			break;
		case 'OCTOBER':
			adjustDays(31, isFullMonth);
			break;
		case 'NOVEMBER':
			adjustDays(30, isFullMonth);
			break;
		case 'DECEMBER':
			adjustDays(31, isFullMonth);
			break;
		default:
			console.log(`Invalid month: ${month}`);
			break;
	}
}
