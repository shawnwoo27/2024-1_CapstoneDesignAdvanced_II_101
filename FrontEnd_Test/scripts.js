// function checkLettuceSize() {
//     var lettuceSize = 400;

//     if (lettuceSize > 500) {
//         alert('상추가 수확 크기에 도달했습니다! 수확을 고려하세요.');
//     }
// }
// checkLettuceSize();

// function fetchData() {
//     fetch('/sensor_data')
//     .then(response => response.json())
//     .then(data => {
//         updateStatus(data);
//     })
//     .catch(error => console.error('Error fetching data:', error));
// }

// function updateStatus(data) {
//     document.getElementById('temperature').textContent = data.temperature + '°C';
//     document.getElementById('light').textContent = data.light + ' lux';
//     document.getElementById('humidity').textContent = data.humidity + '%';
//     document.getElementById('waterLevel').textContent = data.waterLevel + ' cm';

//     updateCondition(data.temperature, 18, 22, 15, 24, 'temp-status');
//     updateCondition(data.light, 15000, 25000, 10000, 30000, 'light-status');
//     updateCondition(data.humidity, 50, 60, 40, 70, 'humidity-status');
// }

// function updateCondition(value, idealMin, idealMax, min, max, elementId) {
//     var statusElement = document.getElementById(elementId);
//     if (value >= idealMin && value <= idealMax) {
//         statusElement.textContent = '좋아요';
//         statusElement.className = 'status good';
//     } else if (value >= min && value <= max) {
//         statusElement.textContent = '적당해요';
//         statusElement.className = 'status moderate';
//     } else {
//         statusElement.textContent = '나빠요';
//         statusElement.className = 'status bad';
//     }
// }

// setInterval(fetchData, 1000);

window.addEventListener('scroll', function() {
    var header = document.querySelector('.header');
    if (window.scrollY > 0) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});
