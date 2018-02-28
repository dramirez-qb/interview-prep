require_relative 'computer_builder_v2'
require_relative 'desktop_computer'

class DesktopBuilder < ComputerBuilder
	def initialize
		@computer = DesktopComputer.new
	end

	def display=(display)
		@display = display
	end

	def add_cd(writer=false)
		@computer.drives << Drive.new(:cd, 760, writer)
	end

	def add_dvd(writer=false)
		@computer.drives << Drive.new(:dvd, 4000, writer)
	end

	def add_hard_disk(size_in_mb)
		@computer.drives << Drive.new(:hard_disk, size_in_mb, true)
	end

	def computer
		raise 'Not enough memory' if @computer.motherboard.memory_size < 250
		raise 'Too many drives' if @computer.drives.size > 4
		hard_disk = @computer.drives.find { |drive| drive.type == :hard_disk }
		if not hard_disk
			raise 'No room to add hard disk' if @computer.drives.size >= 4
			add_hard_disk(10000)
		end
		@computer
	end
end
