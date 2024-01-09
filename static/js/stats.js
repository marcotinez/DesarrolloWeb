Highcharts.chart('container_hinchas', {
    colors: ['#10487F', '#406D99', '#668AAD', '#85A1BD', '#C1CFDD'],
    chart: {
      type: 'pie'
    },
    title: {
      text: 'Cantidad de hinchas por deporte.'
    },
    subtitle: {
      text:
      'Source: LocalHost DB'
    },
    plotOptions: {
      pie: {
        allowPointSelect: true,
        cursor: 'pointer',
        dataLabels: {
          enabled: true,
          format: '{point.name}: {point.percentage:.1f}%'
        },
        showInLegend: true
      }
    },
    series: [
      {
        name: 'Cantidad',
        colorByPoint: true,
        data: []
      }
    ]
  });

fetch("http://localhost:5000/stats/hinchas")
  .then(response => response.json())
  .then((data) =>{
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container_hinchas"
    );
    //actualizamos la data del grafico
    chart.update({
      series: [
        {
          data: data,
        },
      ],
    });
  })
  .catch((error) => console.error("Error:", error));


Highcharts.chart('container_artesanos', {
    colors: ['#10487F', '#406D99', '#668AAD', '#85A1BD', '#C1CFDD'],
    chart: {
      type: 'pie'
    },
    title: {
      text: 'Cantidad de artesanos por artesanía.'
    },
    subtitle: {
      text:
      'Source: LocalHost DB'
    },
    plotOptions: {
      pie: {
        allowPointSelect: true,
        cursor: 'pointer',
        dataLabels: {
          enabled: true,
          format: '{point.name}: {point.percentage:.1f}%'
        },
        showInLegend: true
      }
    },
    series: [
      {
        name: 'Cantidad',
        colorByPoint: true,
        data: []
      }
    ]
  });

fetch("http://localhost:5000/stats/artesanos")
  .then(response => response.json())
  .then((data) =>{
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container_artesanos"
    );
    //actualizamos la data del grafico
    chart.update({
      series: [
        {
          data: data,
        },
      ],
    });
  })
  .catch((error) => console.error("Error:", error));