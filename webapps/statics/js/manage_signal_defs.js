$("#simulation_result_spin").hide()

function save_simulation_settings() {
    var formData = $('#simulation_settings').serializeArray();
    var data = $.param(formData);
	$.ajax({
		url: save_simulation_settings_api,
		type: 'POST',
		data: data,
		dataType: 'json',
		success: function(data){
			$("#simulation_result_spin").hide()
            console.log(data)
		},
		error: function(){
			alert('ajax error');
		}
	})
}

function get_signal_defs(file_name){
    $("#signal_def_name").text(file_name)
	$("#file_name").val(file_name)
	//$("#file_name").attr("disabled", "true")
    $("#simulation_result_spin").show()
    $.ajax({
		url: get_signal_defs_api,
		type: 'POST',
		data: {
			"file_name": file_name,
		},
		dataType: 'json',
		success: function(data){
			$("#simulation_result_spin").hide()
            console.log(data)
            $("#signal_defs").text(data)
		},
		error: function(){
			alert('ajax error');
		}
	})
}