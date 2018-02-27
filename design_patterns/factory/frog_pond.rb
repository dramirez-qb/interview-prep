require_relative 'pond_v2'
require_relative 'frog'

class FrogPond < Pond
  def new_animal(name)
    Frog.new(name)
  end
end
