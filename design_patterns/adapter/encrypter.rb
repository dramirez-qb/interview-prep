class Encrypter
	def initialize(key)
		@key = key
	end

	def encrypt(reader, writer)
		key_index = 0
		while not reader.eof?
			clear_char = reader.getc
			encrypted_char = clear_char.unpack('C*').zip(@key[key_index].unpack('C*')).map{ |a,b| a ^ b }.pack('C*')
			writer.putc(encrypted_char)
			key_index = (key_index + 1) % @key.size
		end
	end
end
