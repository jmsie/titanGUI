class Titan_command_builder():
  def create_population(self, context):
    command = 'create_population -settings #simulation_setting_file -signal_def #signal_def_file -range #range -instrument #instrument -seqdef #seq_def #population_name -strategy #strategy'
    for key, value in context.items():
      command = command.replace(key, value)
    return command