require_relative 'simple_writer'

if __FILE__ == $0
  w = SimpleWriter.new('out')

  class << w
    alias old_write_line write_line

    def write_line(line)
      old_write_line("#{Time.new}: #{line}")
    end
  end
end
