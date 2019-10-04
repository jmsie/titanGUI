$("#simulation_result_spin").hide()

function get_simulation_settings(file_name){
    $("#setting_name").text(file_name + ".setting.yml")
    $("#simulation_result_spin").show()
    $.ajax({
		url: get_simulation_settings_api,
		type: 'POST',
		data: {
			"file_name": file_name,
		},
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