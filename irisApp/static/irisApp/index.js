document.addEventListener("DOMContentLoaded", function () {

	const queryFlowerLink = document.querySelector("#queryFlower");
	const flowersLink = document.querySelector("#flowers")

	queryFlowerLink.addEventListener("click",composeFlower);
	flowersLink.addEventListener("click", () => loadIndexPage('Iris Flowers'));

	document.querySelector("#form-control").addEventListener("submit", () => {
		postFlower();
	});


	// by default load Flower Page
	loadIndexPage('Iris Flowers');

	function loadIndexPage(page){
		document.querySelector("#body-div").style.display = 'block';
		document.querySelector("#compose-div").style.display = 'none';

		document.querySelector('#body-div').innerHTML = `<h1 class='heading-page'>${page.charAt(0).toUpperCase() + page.slice(1)}</h1>`;

		fetch(`/flowers/${encodeURIComponent(page)}`)
		.then(response => response.json())
		.then(data => {
			console.log(data);
			const tableData = document.createElement("table");
			tableData.className = "tableData";
			tableData.innerHTML = "\
				 <tr>\
				<th>User</th>\
				<th>Flower Id</th>\
				<th>Sepal Length (cm) </th>\
				<th>Sepal Width (cm) </th>\
				<th>Petal Length (cm) </th>\
				<th>Petal Width (cm) </th>\
				<th>Prediction (Iris Class)</th>\
			</tr>";
			data.forEach(element => {
				tableData.innerHTML += `	
					<tr>
						<td>${element.user.charAt(0).toUpperCase() + element.user.slice(1)}</td>
						<td>${element.id}</td>
						<td>${element.sepal_length}</td>
						<td>${element.sepal_width}</td>
						<td>${element.petal_length}</td>
						<td>${element.petal_width}</td>
						<td>${element.prediction.charAt(0).toUpperCase() + element.prediction.slice(1)}</td>
					</tr>
				`;

				document.querySelector("#body-div").appendChild(tableData);
			});
		})
		.catch(error => {
			console.error(" error ", error)
		})
	}

	function composeFlower(){
		document.querySelector("#body-div").style.display = 'none';
		document.querySelector("#compose-div").style.display = 'block';

		document.querySelector("#sepal_length").value = '';
		document.querySelector("#sepal_width").value = '';
		document.querySelector("#petal_length").value = '';
		document.querySelector("#petal_width").value = '';
	}

	function postFlower(){

		const sepal_length = document.querySelector("#sepal_length").value;
		const sepal_width = document.querySelector("#sepal_width").value;
		const petal_length = document.querySelector("#petal_length").value;
		const petal_width = document.querySelector("#petal_width").value;

		const data = {
			sepal_length, sepal_width , petal_length , petal_width
		};

		const options = {
			method: "POST",
			body: JSON.stringify(data),
			headers: {
				"Content-Type": "application/json"
			}
		};

		fetch("/flowers", options)
			.then(response => response.json())
			.then(data => {
				console.log("Response Data:", data);
				console.log("Flower Data Posted SuccessFully");
			})
			.catch(error => {
				console.error("Error Passing Flower Data , Following Error was direct cause" , error)
			})

		return false;
	}

});