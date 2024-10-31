// Este script utiliza la libreria brain.js para crear una red neuronal que clasifica flores en base a sus caracteristicas
// las caracteristicas son: largo del sepal, ancho del sepal, largo del petalo y ancho del petalo
// la red neuronal se entrena con datos de flores de la especie Setosa, Versicolor y Virginica
// y posteriormente se utiliza para clasificar flores en base a las caracteristicas ingresadas por el usuario

var network = new brain.NeuralNetwork(); // Inicializa una nueva red neuronal

// Normalizar los datos de entrada para que estén en un rango adecuado
function normalizeData(data) {
return data.map(item => ({
    input: {
      SepalLengthCm: item.input.SepalLengthCm / 10, // Normaliza el largo del sépalo
      SepalWidthCm: item.input.SepalWidthCm / 10,   // Normaliza el ancho del sépalo
      PetalLengthCm: item.input.PetalLengthCm / 10, // Normaliza el largo del pétalo
      PetalWidthCm: item.input.PetalWidthCm / 10    // Normaliza el ancho del pétalo
    },
    output: item.output // Mantiene la salida original
}));
}

// Datos de entrenamiento para la red neuronal
const trainingData = normalizeData([
    // Datos de flores de la especie Setosa
    {input: {SepalLengthCm: 0.51, SepalWidthCm: 0.35, PetalLengthCm: 0.14, PetalWidthCm: 0.02}, output: {setosa: 1, versicolor: 0, virginica:0}},
    // ... (más datos de entrenamiento)
    // Datos de flores de la especie Virginica
    {input: {SepalLengthCm: 0.65, SepalWidthCm: 0.30, PetalLengthCm: 0.58, PetalWidthCm: 0.22}, output: {setosa: 0, versicolor: 0, virginica:1}},
]);

// Entrenamiento de la red neuronal con los datos normalizados
network.train(trainingData);

// Función para clasificar la flor basada en las características ingresadas
function classifyFlower(sepalLength, sepalWidth, petalLength, petalWidth) {
var input = {
    SepalLengthCm: sepalLength / 10, // Normaliza el largo del sépalo
    SepalWidthCm: sepalWidth / 10,   // Normaliza el ancho del sépalo
    PetalLengthCm: petalLength / 10, // Normaliza el largo del pétalo
    PetalWidthCm: petalWidth / 10     // Normaliza el ancho del pétalo
};
  var result = network.run(input); // Ejecuta la red neuronal con los datos de entrada

  // Determina la especie de la flor con base en la salida de la red
let max = Math.max(result.setosa, result.versicolor || 0, result.virginica || 0);
if (max === result.setosa) return "Setosa";
if (max === result.versicolor) return "Versicolor";
return "Virginica";
}

// Manejo del evento de clasificación al hacer clic en el botón
document.getElementById('classifyBtn').addEventListener('click', function() {
  // Obtiene los valores ingresados por el usuario
var sepalLength = parseFloat(document.getElementById('sepalLength').value);
var sepalWidth = parseFloat(document.getElementById('sepalWidth').value);
var petalLength = parseFloat(document.getElementById('petalLength').value);
var petalWidth = parseFloat(document.getElementById('petalWidth').value);

  // Verifica si los valores son válidos
if (isNaN(sepalLength) || isNaN(sepalWidth) || isNaN(petalLength) || isNaN(petalWidth)) {
    alert("Por favor, ingresa valores numéricos válidos."); // Mensaje de error
    return;
}

  // Muestra el resultado de la clasificación en el div correspondiente
document.getElementById('result').innerText = "La flor clasificada es: " + classifyFlower(sepalLength, sepalWidth, petalLength, petalWidth);
});