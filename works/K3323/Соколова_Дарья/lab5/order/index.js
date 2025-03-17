function handleSubmit(event) {
	event.preventDefault();
	
	const firstName = document.getElementById('firstName').value;
	const lastName = document.getElementById('lastName').value;
	const email = document.getElementById('email').value;
	const feedback = document.getElementById('feedback').value;
	const gender = document.querySelector('input[name="gender"]:checked')?.value;
	const options = Array.from(document.querySelectorAll('input[name="options[]"]:checked')).map(option => option.value).join(', ');

	const output = `
			<h2>Обратная связь:</h2>
			<p><strong>Имя:</strong> ${firstName}</p>
			<p><strong>Фамилия:</strong> ${lastName}</p>
			<p><strong>Email:</strong> ${email}</p>
			<p><strong>Обратная связь:</strong> ${feedback}</p>
			<p><strong>Пол:</strong> ${gender}</p>
			<p><strong>Выборы:</strong> ${options}</p>
	`;

	document.getElementsByClassName('container')[0].innerHTML = output;
}
