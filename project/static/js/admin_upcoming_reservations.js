console.log('admin upcoming reservations');

function getDateNDaysAway(n) {
	let calendar = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ];
	const d = new Date();
	if (d.getFullYear() % 4 == 0) calendar[1] + 1; // account for leap year if necessary

	let nextMonth = d.getMonth() + 1;
	let nextDate = d.getDate() + n;
	let nextYear = d.getFullYear() - 2000;
	if (nextDate > calendar[nextMonth - 1]) {
		// if necessary, adjust to next month
		nextDate -= calendar[nextMonth - 1];
		nextMonth++;
	}
	if (nextMonth > 12) {
		// if next month went past December
		nextMonth -= 12;
		nextYear++;
	}
	nextMonth = nextMonth < 10 ? '0' + nextMonth.toString() : nextMonth; // pad leading 0
	nextdate = nextDate < 10 ? '0' + nextDate.toString() : nextDate;
	return `${nextMonth}-${nextdate}-${nextYear}`;
}

function navigate(where) {
	let today = getDateNDaysAway(0);
	switch (where) {
		case 'today':
			console.log(today);
			location.href = `/admin/reservations/upcoming?start=${today}&end=${today}`;
			break;
		case '7days':
			let sevenDaysFromToday = getDateNDaysAway(7);
			console.log(sevenDaysFromToday);
			location.href = `/admin/reservations/upcoming?start=${today}&end=${sevenDaysFromToday}`;
			break;
		case '30days':
			let thirtyDaysFromToday = getDateNDaysAway(30);
			console.log(thirtyDaysFromToday);
			location.href = `/admin/reservations/upcoming?start=${today}&end=${thirtyDaysFromToday}`;
			break;
		default:
			console.log('invalid location');
	}
}
