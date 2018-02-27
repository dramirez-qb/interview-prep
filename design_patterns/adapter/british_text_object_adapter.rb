class BritishTextObjectAdapter < TextObject
	def initialize(bto)
		@bto = bto
	end

	def text
		@bto.string
	end

	def size_inches
		return @bto.size_mm / 25.4
	end

	def color
		@bto.colour
	end
end
