const todayDate = new Date();

function clientRequestInput(event) {
	document.querySelector('#requests-length').innerHTML = event.target.value.length;
}

async function initPage() {
	initDateControls();
	let response = await getReservationData();
	console.log(response);
	handleFetchedReservationData(response);
}
initPage();

function initDateControls() {
	let month = document.querySelector('#month');
	month.selectedIndex = todayDate.getMonth() + 1;
	let year = document.querySelector('#year');
	year.value = todayDate.getFullYear();
	monthChange({ target: { value: month.value, selectedIndex: month.selectedIndex } });
}

async function getReservationData() {
	let date = getDateControlValuesAsString();
	let locationKey = document.querySelector('#location').value;
	return await getData(`/reservations?date=${date}&location=${locationKey}`);
}

function getDateControlValuesAsString() {
	let currentMonth = todayDate.getMonth() + 1;
	let todayCalendarDate = todayDate.getDate();
	let currentYear = todayDate.getFullYear().toString().substring(2);
	let date = `${currentMonth < 10 ? '0' + currentMonth.toString() : currentMonth}-`; // pad a zero, just in case
	date += `${todayCalendarDate < 10 ? '0' + todayCalendarDate.toString() : todayCalendarDate}-`; // pad a zero, just in case
	date += `${currentYear}`; // is a substring; will already be padded
	return date;
}

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
	let formattedDate = getDateControlValuesAsString();
	let locationKey = document.querySelector('#location').value;
	let response = await getData(`/reservations?date=${formattedDate}&location=${locationKey}`);
	handleFetchedReservationData(response);
}

function ValidateEmail(inputText) {
	var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	if (inputText.match(mailformat)) {
		return true;
	} else {
		return false;
	}
}

const toggleEmailWarning = {
	off: function() {
		document.querySelector('#email').style.border = '1px solid #000';
		document.querySelector('#invalid-email-warning').style.display = 'none';
	},
	on: function() {
		document.querySelector('#invalid-email-warning').style.display = 'inline';
		document.querySelector('#email').style.border = '1px solid #f00';
	}
};

const toggleReservationError = {
	off: function() {
		document.querySelector('#reservation-error').style.display = 'none';
	},
	on: function() {
		document.querySelector('#reservation-error').style.display = 'block';
	}
};

async function scheduleReservation() {
	toggleEmailWarning.off();
	toggleReservationError.off();
	const email = document.querySelector('#email').value;
	if (ValidateEmail(email)) {
		const clientRequests = document.querySelector('#requests').value;
		const date = document.querySelector('#date-buffer').value;
		const time = document.querySelector('#time-buffer').value;
		const location = document.querySelector('#location').value;
		let response = await postData(`/reservations`, { date, time, location, email, requests: clientRequests });
		console.log(response);
		if (response.result) goToScheduledSuccessPage();
		else toggleReservationError.on();
	} else {
		toggleEmailWarning.on();
	}
}

function goToScheduledSuccessPage() {
	location.href = '/reservations/scheduled';
}

function setModalBuffers(event) {
	if (event.target.classList.contains('available')) {
		let month = document.querySelector('#month');
		let dateValue = document.querySelector('#date').value;
		let yearValue = document.querySelector('#year').value - 2000;
		document.querySelector('#reservation-date').innerHTML = `${month.value} ${dateValue} ${yearValue}`;
		document.querySelector('#date-buffer').value = getDateControlValuesAsString();
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
