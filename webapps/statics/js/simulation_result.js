/*
Template Name: Color Admin - Responsive Admin Dashboard Template build with Twitter Bootstrap 4
Version: 4.2.0
Author: Sean Ngu
Website: http://www.seantheme.com/color-admin-v4.2/admin/
*/

$("#simulation_result_spin").hide()
$("#simulation_result_download").hide()


function get_simulation_result (seq_name) {
    $("#seq_name").text(seq_name)
    $("#interactive-chart").hide()
	$("#simulation_result_download").hide()
	$("#simulation_result_spin").show()
	$.ajax({
	url: get_simulation_result_api,
	type: 'POST',
	data: {
		"seq_name": seq_name,
	},
	dataType: 'json',
	success: function(data){
        handle_simulation_finish(data)
	},
	error: function(){
		alert('ajax error');
	}
})
}

function handle_simulation_finish(data) {
    $("#simulation_result_spin").hide()
    seq_name = $("#seq_name").text()
	$("#interactive-chart").show()
	$("#simulation_result_download").show()
    handle_simulation_result(data)
}

function handle_simulation_result(data){
	console.log(data);
	handleInteractiveChart(
		data.in_sample_profits,
		data.in_sample_profits,
		data.time_line,
		data.max_profit,
		data.min_profit,
	)
}


function prepare_code(){
	$.ajax({
		url: cg_write_api,
		type: 'POST',
		data: {
			"seq_name": $("#seq_name").text(),
		},
		dataType: 'json',
		success: function(data){
			console.log(command + "...success")
            download_code(data)
		},
		error: function(){
			alert('ajax error');
		}
	})
}

function download_code(data) {
	console.log(data.path)
    fetch(static_url + data.path).then(res => res.blob().then(blob => {
        var a = document.createElement('a');
        var url = window.URL.createObjectURL(blob);
        var filename = data.file_name;
        a.href = url;
        a.download = filename;
        a.click();
        window.URL.revokeObjectURL(url);
    }))
}

function handleInteractiveChart(profits, base_index, time_line, max_profit, min_profit) {
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

