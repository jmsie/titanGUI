function send_command(command_list, call_back){
    command = command_list.shift()
    if (command == undefined) {
        return
    }else{
        console.log(command)
        $.ajax({
            url: console_send_command_api,
            type: 'POST',
            data: {
                "command": command,
            },
            dataType: 'json',
            success: function(data){
                console.log(command + "...success")
                if (call_back != undefined && command_list.length == 0)
                    call_back(data)
                send_command(command_list, call_back)
            },
            error: function(){
                alert('ajax error');
            }
        })
     }
}