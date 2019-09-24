function send_command(command_list, call_back){
    command = command_list.shift()
    if (command == undefined) {
        return
    }else{
        console.log(command)
        $.ajax({
            url: api_url,
            type: 'POST',
            data: {
                "command": command,
            },
            dataType: 'json',
            success: function(data){
                console.log(command + "...success")
                if (call_back != undefined)
                    call_back(data)
                send_command(command_list)
            },
            error: function(){
                alert('ajax error');
            }
        })
     }
}