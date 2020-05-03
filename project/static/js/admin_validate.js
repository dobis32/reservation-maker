console.log('admin validate');
async function validateToken() {
	try {
		const token = sessionStorage.getItem('adminToken@resv_maker');
		if (!token) throw new Error('No token available.');
		let response = await postData('/admin/validate', { token });
		console.log(response);
		if (!response.result || !response.token) throw new Error('Token validation failed.');
		else sessionStorage.setItem('adminToken@resv_maker', response.token);
	} catch (error) {
		console.log(error);
		sessionStorage.removeItem('adminToken@resv_maker');
		location.href = '/admin/login';
	}
}
validateToken();
