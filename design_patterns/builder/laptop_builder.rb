require_relative 'computer_builder_v2'
require_relative 'laptop_computer'
require_relative 'laptop_drive'

class LaptopBuilder < ComputerBuilder
	def initialize
		@computer = LaptopComputer.new
	end

	def display=(display)
		raise "Laptop display must be lcd" unless display == :lcd
	end

	def add_cd(writer=false)
		@computer.drives << LaptopDrive.new(:cd, 760, writer)
	end

	def add_dvd(writer=false)
		@computer.drives << LaptopDrive.new(:dvd, 4000, writer)
	end

	def add_hard_disk(size_in_mb)
		@computer.drives << LaptopDrive.new(:hard_disk, size_in_mb, true)
	end

	def reset
		@computer = LaptopComputer.new
	end
end
