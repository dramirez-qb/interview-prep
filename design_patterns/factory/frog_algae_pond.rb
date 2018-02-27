require_relative 'pond_v2'
require_relative 'algae'
require_relative 'frog'

class FrogAlgaePond < Pond
	def new_animal(name)
		Frog.new(name)
	end

	def new_plant(name)
		Algae.new(name)
	end
end
