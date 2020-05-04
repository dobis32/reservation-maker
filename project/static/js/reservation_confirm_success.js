console.log('reservation confirm success');
const dateBuffer = document.querySelector('#date-buffer');
const dateSpan = document.querySelector('#date-span');
dateSpan.innerHTML = dateBuffer.value.split('-').join('/');

const timeBuffer = document.querySelector('#time-buffer');
const timeSpan = document.querySelector('#time-span');
const timeTokens = timeBuffer.value.split('-');
timeSpan.innerHTML = `${timeTokens[0]}:${timeTokens[1]} ${timeTokens[2]}`;
