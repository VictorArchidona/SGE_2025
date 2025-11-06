//Inicializar red neuronal
var network = new brain.NeuralNetwork();

network.train([
    // Iris-Setosa
    {input: {SepalLength: 3.8, SepalWidth: 1.9, PetalLength: 4.6, PetalWidth: 2.7}, output: {setosa: 1}},
    {input: {SepalLength: 2.3, SepalWidth: 4.8, PetalLength: 1.6, PetalWidth: 3.9}, output: {setosa: 1}},
    {input: {SepalLength: 4.2, SepalWidth: 2.7, PetalLength: 3.1, PetalWidth: 4.3}, output: {setosa: 1}},
    {input: {SepalLength: 1.9, SepalWidth: 3.4, PetalLength: 2.8, PetalWidth: 1.3}, output: {setosa: 1}},
    {input: {SepalLength: 4.7, SepalWidth: 1.8, PetalLength: 2.1, PetalWidth: 3.5}, output: {setosa: 1}},

    // Iris-Versicolor 
    {input: {SepalLength: 2.5, SepalWidth: 4.4, PetalLength: 3.9, PetalWidth: 1.2}, output: {versicolor: 1}},
    {input: {SepalLength: 3.6, SepalWidth: 1.4, PetalLength: 2.9, PetalWidth: 4.5}, output: {versicolor: 1}},
    {input: {SepalLength: 1.7, SepalWidth: 3.5, PetalLength: 4.4, PetalWidth: 2.2}, output: {versicolor: 1}},
    {input: {SepalLength: 4.8, SepalWidth: 2.6, PetalLength: 3.2, PetalWidth: 1.9}, output: {versicolor: 1}},
    {input: {SepalLength: 2.9, SepalWidth: 1.3, PetalLength: 1.6, PetalWidth: 4.8}, output: {versicolor: 1}},

    // Iris-Virginica
    {input: {SepalLength: 4.1, SepalWidth: 3.7, PetalLength: 1.5, PetalWidth: 2.8}, output: {virginica: 1}},
    {input: {SepalLength: 2.2, SepalWidth: 4.9, PetalLength: 3.4, PetalWidth: 1.7}, output: {virginica: 1}},
    {input: {SepalLength: 3.3, SepalWidth: 2.1, PetalLength: 4.6, PetalWidth: 3.8}, output: {virginica: 1}},
    {input: {SepalLength: 4.4, SepalWidth: 3.2, PetalLength: 1.8, PetalWidth: 2.6}, output: {virginica: 1}},
    {input: {SepalLength: 1.6, SepalWidth: 4.5, PetalLength: 2.7, PetalWidth: 3.1}, output: {virginica: 1}},
])


function update() {
  
  var SepalLength = parseFloat(document.getElementById("SepalLength").value);
  var SepalWidth = parseFloat(document.getElementById("SepalWidth").value);
  var PetalLength = parseFloat(document.getElementById("PetalLength").value);
  var PetalWidth = parseFloat(document.getElementById("PetalWidth").value);

  var dicc = {SepalLength, SepalWidth, PetalLength, PetalWidth};

  var resultado = network.run(dicc);

  console.log(resultado);

  var especie = "";
  var maxProb = 0;

  for (var key in resultado) {
    if (resultado[key] > maxProb) {
      maxProb = resultado[key];
      especie = key;
    }
  }

  var texto = document.getElementById("resultado");

  texto.textContent = `Resultado: ${especie}`;
}

update();