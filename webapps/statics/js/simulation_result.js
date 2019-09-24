/*
Template Name: Color Admin - Responsive Admin Dashboard Template build with Twitter Bootstrap 4
Version: 4.2.0
Author: Sean Ngu
Website: http://www.seantheme.com/color-admin-v4.2/admin/
*/

$("#simulation_result_spin").hide()


function get_simulation_result (seq_name) {
    $("#seq_name").text(seq_name)
    $("#interactive-chart").hide()
	$("#simulation_result_spin").show()
    send_command(["parse_sequence -sequence " + seq_name])
	send_command(['run_simulation'], handle_simulation_finish)
}

function handle_simulation_result(data){
	console.log(data);
	obj = JSON.parse(data.message)
	trades = obj.list
	profits = []
	base_index = []
	time_line = []
	total_profit = 0
	max_profit = -Number.MAX_VALUE
	min_profit = Number.MAX_VALUE
	for (var i = 0; i < trades.length; i++){
		total_profit += trades[i][0][5]
		profits.push([i, total_profit])
		base_index.push([i, total_profit])
		time_line.push([i, ""])
		max_profit = Math.max(max_profit,  total_profit)
		min_profit = Math.min(min_profit, total_profit)
	}
	handleInteractiveChart(profits, base_index, time_line, max_profit, min_profit)

}

function handle_simulation_finish(data) {
	console.log(data)
    $("#simulation_result_spin").hide()
    seq_name = $("#seq_name").text()
	$("#interactive-chart").show()
	send_command(["_gui_show_list_of_trades -sequence " + seq_name], handle_simulation_result)
}


function handleInteractiveChart(profits, base_index, time_line, max_profit) {
	"use strict";
	function showTooltip(x, y, contents) {
		$('<div id="tooltip" class="flot-tooltip">' + contents + '</div>').css( {
			top: y - 45,
			left: x - 55
		}).appendTo("body").fadeIn(200);
	}
	if ($('#interactive-chart').length !== 0) {
		$.plot($("#interactive-chart"), [{
				data: profits,
				label: "Profit",
				color: COLOR_BLUE,
				lines: { show: true, fill:false, lineWidth: 1 },
				points: { show: true, radius: 1, fillColor: COLOR_WHITE },
				shadowSize: 0
			}, {
				data: base_index,
				label: 'Base index',
				color: COLOR_GREEN,
				lines: { show: true, fill:false, lineWidth: 1 },
				points: { show: true, radius: 1, fillColor: COLOR_WHITE },
				shadowSize: 0
			}], {
				xaxis: {  ticks:time_line, tickDecimals: 0, tickColor: COLOR_BLACK_TRANSPARENT_2 },
				yaxis: {  ticks: 10, tickColor: COLOR_BLACK_TRANSPARENT_2, min: min_profit, max: max_profit },
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

