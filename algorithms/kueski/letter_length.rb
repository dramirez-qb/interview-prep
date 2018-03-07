def letter_length(s)
	return false if s.empty?
	indices_per_letter = get_indices_per_letter(s)
	build_letter_length(indices_per_letter)
end

def get_indices_per_letter(s)
	indices_per_letter = Hash.new { |h, k| h[k] = [] }

	s.each_char.with_index do |letter, index|
		if indices_per_letter.has_key? letter
			indices_per_letter[letter][1] = index
		else
			indices_per_letter[letter] << index
		end
		indices_per_letter[letter]
	end

	indices_per_letter
end

def build_letter_length(indices_per_letter)
	letters = ('a'..'z')
	result = []
	offset = 'a'.ord
	(0..25).each { |i| result[i] = 0 }

	letters.each do |letter|
		if indices_per_letter.has_key? letter
			result[letter.ord - offset] = (indices_per_letter[letter].last - indices_per_letter[letter].first) + 1
		end
	end

	result
end

s = "abacabazzxxzz"
p "#{letter_length(s)}"
