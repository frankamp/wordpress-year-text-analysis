var data = {
    labels: %s,
    datasets: [
        {
            label: "Primary",
            fillColor: "rgba(220,220,220,0.2)",
            strokeColor: "rgba(220,220,220,1)",
            pointColor: "rgba(220,220,220,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(220,220,220,1)",
            data: %s
        },
        {
            label: "Secondary",
            fillColor: "rgba(151,187,205,0.2)",
            strokeColor: "rgba(151,187,205,1)",
            pointColor: "rgba(151,187,205,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(151,187,205,1)",
            data: %s
        },
        {
            label: "Emotion",
            fillColor: "rgba(205,183,158,0.2)",
            strokeColor: "rgba(205,183,158,1)",
            pointColor: "rgba(205,183,158,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(205,183,158,1)",
            data: %s
        }
    ]
};

var context = document.getElementById('skills').getContext('2d');
var skillsChart = new Chart(context).Radar(data, {
    pointDot: false,
    bezierCurve : true,
    scaleShowLine: true,
    angleShowLineOut: false
});