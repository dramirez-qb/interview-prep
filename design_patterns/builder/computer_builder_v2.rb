require_relative 'computer'
require_relative 'motherboard'
require_relative 'turbo_cpu'

class ComputerBuilder
	attr_reader :computer

	def turbo(has_turbo_cpu=true)
		@computer.motherboard.cpu = TurboCPU.new
	end

	def memory_in_size=(size_in_mb)
		@computer.motherboard.memory_size = size_in_mb
	end

	def method_missing(name, *args)
		words = name.to_s.split('_')
		return super(name, *args) unless words.shift == 'add'
		words.each do |word|
			next if word == 'and'
			add_cd if word == 'cd'
			add_dvd if word == 'dvd'
			add_hard_disk(100000) if word == 'harddisk'
			turbo if word == 'turbo'
		end
	end
end
