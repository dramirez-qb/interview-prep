require_relative 'computer'
require_relative 'motherboard'

class LaptopComputer < Computer
	def initialize(motherboard=Motherboard.new, drives=[])
		super(:lcd, motherboard, drives)
	end

	# Lots of interesting laptop details omitted...
end
