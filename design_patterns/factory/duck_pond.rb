require_relative 'pond_v2'
require_relative 'duck'

class DuckPond < Pond
  def new_animal(name)
    Duck.new(name)
  end
end
