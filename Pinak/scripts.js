// const ctx1 = document.getElementById('chart1').getContext('2d');
// const ctx2 = document.getElementById('chart2').getContext('2d');
// const ctx3 = document.getElementById('chart3').getContext('2d');

// const chart1 = new Chart(ctx1, {
//     type: 'bar',
//     data: {
//         labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
//         datasets: [{
//             label: 'Projections',
//             data: [120000, 90000, 140000, 100000, 130000, 110000, 90000, 95000, 120000, 130000, 140000, 150000],
//             backgroundColor: '#7986CB',
//         }, {
//             label: 'Actuals',
//             data: [110000, 85000, 120000, 95000, 125000, 105000, 85000, 90000, 115000, 120000, 130000, 140000],
//             backgroundColor: '#4DB6AC',
//         }]
//     }
// });

// const chart2 = new Chart(ctx2, {
//     type: 'line',
//     data: {
//         labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
//         datasets: [{
//             label: 'Earnings',
//             data: [2000, 3000, 2500, 4000, 3500, 3000, 4500],
//             borderColor: '#4CAF50',
//             fill: false,
//         }, {
//             label: 'Expenses',
//             data: [1800, 2800, 2200, 3800, 3300, 2900, 4200],
//             borderColor: '#FF5722',
//             fill: false,
//         }]
//     }
// });

// const chart3 = new Chart(ctx3, {
//     type: 'doughnut',
//     data: {
//         labels: ['Product A', 'Product B', 'Product C', 'Product D'],
//         datasets: [{
//             data: [30, 40, 20, 10],
//             backgroundColor: ['#FFCE56', '#36A2EB', '#FF6384', '#4CAF50']
//         }]
//     }
// });




// Initialize the first chart
// Initialize the first chart
const ctx1 = document.getElementById('chart1').getContext('2d');
const chart1 = new Chart(ctx1, {
    type: 'bar',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            label: 'Projections',
            data: [30000, 50000, 70000, 90000, 110000, 130000, 150000, 170000, 140000, 120000, 130000, 140000],
            backgroundColor: '#4DB6AC',
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
    }
});

// Initialize the second chart
const ctx2 = document.getElementById('chart2').getContext('2d');
const chart2 = new Chart(ctx2, {
    type: 'line',
    data: {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        datasets: [{
            label: 'Earnings',
            data: [2000, 3000, 2500, 4000, 3500, 3000, 4500],
            borderColor: '#4CAF50',
            fill: false,
        }, {
            label: 'Expenses',
            data: [1800, 2800, 2200, 3800, 3300, 2900, 4200],
            borderColor: '#FF5722',
            fill: false,
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
    }
});

// Initialize the third chart
const ctx3 = document.getElementById('chart3').getContext('2d');
const chart3 = new Chart(ctx3, {
    type: 'doughnut',
    data: {
        labels: ['Product A', 'Product B', 'Product C', 'Product D'],
        datasets: [{
            data: [30, 40, 20, 10],
            backgroundColor: ['#FFCE56', '#36A2EB', '#FF6384', '#4CAF50']
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
    }
});

// Initialize the India map
var map = L.map('indiaMap').setView([20.5937, 78.9629], 5); // Coordinates for the center of India

// Add the tile layer to the map (this is the actual map background)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '© OpenStreetMap'
}).addTo(map);

// Example marker
L.marker([28.6139, 77.2090]).addTo(map) // New Delhi Coordinates
    .bindPopup('New Delhi')
    .openPopup();
