$(function () {

    'use strict';
    /**************** PIE CHART *******************/
    var piedata = [
        {label: "Гуманитарные науки", shortlabel: '', data: [[1, 10]], color: '#38649f'},
        {label: "Здравохранение и медицинские науки", shortlabel: '', data: [[1, 30]], color: '#389f99'},
        {label: "Инженерное дело и технические науки", shortlabel: '', data: [[1, 90]], color: '#689f38'},
        {label: "Искусство и культура", shortlabel: '', data: [[1, 40]], color: '#ff8f00'},
        {label: "Математические и естественные науки", shortlabel: '', data: [[1, 15]], color: '#ee1044'},
        {label: "Науки об обществе", shortlabel: '', data: [[1, 9]], color: '#eee767'},
        {label: "Образование и педагогические науки", shortlabel: '', data: [[1, 33]], color: '#84ee3d'},
        {label: "Сельско-хозяйственные науки", shortlabel: '', data: [[1, 75]], color: '#ee22aa'},
    ];

    $.plot('#flotPie2', piedata, {
        series: {
            pie: {
                show: true,
                radius: 1,
                innerRadius: 0.5,
                label: {
                    show: true,
                    radius: 2 / 3,
                    formatter: labelFormatter,
                    threshold: 0.1
                }
            }
        },
        grid: {
            hoverable: true,
            clickable: true
        }
    });
    function labelFormatter(shortlabel, series) {
        return "<div style='font-size:8pt; text-align:center; padding:2px; color:white;'>" + shortlabel + "<br/>" + Math.round(series.percent) + "%</div>";
    }


    var options = {
        chart: {
            height: 350,
            type: 'line',
            shadow: {
                enabled: true,
                color: '#000',
                top: 18,
                left: 7,
                blur: 10,
                opacity: 1
            },
            toolbar: {
                show: false
            }
        },
        colors: ['#ee1044', '#38649f'],
        dataLabels: {
            enabled: true,
        },
        stroke: {
            curve: 'smooth'
        },
        series: [{
            name: "Выпускники",
            data: [280, 299, 330, 360, 320, 327, 330]
        },
            {
                name: "Требуемые кадры",
                data: [330, 298, 290, 274, 274, 256, 264]
            }
        ],
        grid: {
            borderColor: '#e7e7e7',
            row: {
                colors: ['#f3f3f3', 'transparent'],
                opacity: 0.5
            },
        },
        markers: {

            size: 6
        },
        xaxis: {
            categories: ['2013', '2014', '2015', '2016', '2017', '2018', '2019'],
            title: {
                text: 'Года'
            }
        },
        yaxis: {
            title: {
                text: 'Востребованность, тыс'
            },
            min: 230,
            max: 360
        },
        legend: {
            position: 'top',
            horizontalAlign: 'right',
            floating: true,
        }
    }

    var chart = new ApexCharts(
        document.querySelector("#uni-attendance"),
        options
    );

    chart.render();
})