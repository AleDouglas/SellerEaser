function singleBarChart(element_id, title, labels, data, bar='bar') {
    var ctx = document.getElementById(element_id).getContext('2d');
    var myChart = new Chart(ctx, {
        type: bar,
        data: {
            labels: labels,
            datasets: [{
                label: title,
                data: data,
                borderWidth: 1
            }]
        },
        options: {
            maintainAspectRatio: false,
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function doubleBarChart(element_id, title, labels, data1, data2, bar='bar') {
    var ctx = document.getElementById(element_id).getContext('2d');
    var myChart = new Chart(ctx, {
        type: bar,
        data: {
            labels: labels,
            datasets: [{
                label: title[0],
                data: data1,
                borderWidth: 1,
            }, {
                label: title[1],
                data: data2,
                borderWidth: 1,
            }]
        },
        options: {
            maintainAspectRatio: false,
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

