/*
Template Name: Color Admin - Responsive Admin Dashboard Template build with Twitter Bootstrap 4
Version: 4.2.0
Author: Sean Ngu
Website: http://www.seantheme.com/color-admin-v4.2/admin/
*/


var handleInteractiveChart = function () {
	"use strict";
	function showTooltip(x, y, contents) {
		$('<div id="tooltip" class="flot-tooltip">' + contents + '</div>').css( {
			top: y - 45,
			left: x - 55
		}).appendTo("body").fadeIn(200);
	}
	if ($('#interactive-chart').length !== 0) {
	
		var data1 = [ 
			[1, 40], [2, 50], [3, 60], [4, 60], [5, 60], [6, 65], [7, 75], [8, 90], [9, 100], [10, 105], 
			[11, 110], [12, 110], [13, 120], [14, 130], [15, 135],[16, 145], [17, 132], [18, 123], [19, 135], [20, 150] 
		];
		var data2 = [
			[1, 10],  [2, 6], [3, 10], [4, 12], [5, 18], [6, 20], [7, 25], [8, 23], [9, 24], [10, 25], 
			[11, 18], [12, 30], [13, 25], [14, 25], [15, 30], [16, 27], [17, 20], [18, 18], [19, 31], [20, 23]
		];
		var xLabel = [
			[1,''],[2,''],[3,'May&nbsp;15'],[4,''],[5,''],[6,'May&nbsp;19'],[7,''],[8,''],[9,'May&nbsp;22'],[10,''],
			[11,''],[12,'May&nbsp;25'],[13,''],[14,''],[15,'May&nbsp;28'],[16,''],[17,''],[18,'May&nbsp;31'],[19,''],[20,'']
		];
		$.plot($("#interactive-chart"), [{
				data: data1, 
				label: "Page Views", 
				color: COLOR_BLUE,
				lines: { show: true, fill:false, lineWidth: 2 },
				points: { show: true, radius: 3, fillColor: COLOR_WHITE },
				shadowSize: 0
			}, {
				data: data2,
				label: 'Visitors',
				color: COLOR_GREEN,
				lines: { show: true, fill:false, lineWidth: 2 },
				points: { show: true, radius: 3, fillColor: COLOR_WHITE },
				shadowSize: 0
			}], {
				xaxis: {  ticks:xLabel, tickDecimals: 0, tickColor: COLOR_BLACK_TRANSPARENT_2 },
				yaxis: {  ticks: 10, tickColor: COLOR_BLACK_TRANSPARENT_2, min: 0, max: 200 },
				grid: { 
				hoverable: true, 
				clickable: true,
				tickColor: COLOR_BLACK_TRANSPARENT_2,
				borderWidth: 1,
				backgroundColor: 'transparent',
				borderColor: COLOR_BLACK_TRANSPARENT_2
			},
			legend: {
				labelBoxBorderColor: COLOR_BLACK_TRANSPARENT_2,
				margin: 10,
				noColumns: 1,
				show: true
			}
		});
		var previousPoint = null;
		$("#interactive-chart").bind("plothover", function (event, pos, item) {
			$("#x").text(pos.x.toFixed(2));
			$("#y").text(pos.y.toFixed(2));
			if (item) {
				if (previousPoint !== item.dataIndex) {
					previousPoint = item.dataIndex;
					$("#tooltip").remove();
					var y = item.datapoint[1].toFixed(2);

					var content = item.series.label + " " + y;
					showTooltip(item.pageX, item.pageY, content);
				}
			} else {
				$("#tooltip").remove();
				previousPoint = null;            
			}
			event.preventDefault();
		});
	}
};


var Dashboard = function () {
	"use strict";
	return {
		//main function
		init: function () {
			handleInteractiveChart();
		}
	};
}();
