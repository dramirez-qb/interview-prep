require_relative 'british_text_object'

class BritishTextObject
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
