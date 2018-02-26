require_relative 'task'

class AddLiquidsTask < Task
  def initialize
    super('Add liquids')
  end

  def get_time_required
    1.0 # 1 minute to add liquids
  end
end
