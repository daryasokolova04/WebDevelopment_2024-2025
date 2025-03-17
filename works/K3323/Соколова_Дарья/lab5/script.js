const color1 = 'rgba(17, 17, 17, 0.765)'
const color2 = 'rgba(125, 128, 189, 0.765)'

function showAlert() {
	alert("Вы нажали на треугольник!");
}

function changeColor() {
	const h1 = document.querySelector('h1')
	const titleColor = 	h1.style.color
	h1.style.color = titleColor === color2 ? color1 : color2
}