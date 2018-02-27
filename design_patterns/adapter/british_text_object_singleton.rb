require_relative 'british_text_object'

bto = BritishTextObject.new('hello', 50.8, :blue)

class << bto
	def color
		colour
	end

	def text
		string
	end

	def size_inches
		size_mm / 25.4
	end
end
