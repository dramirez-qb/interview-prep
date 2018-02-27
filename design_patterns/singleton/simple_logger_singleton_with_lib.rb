require_relative 'simple_logger'
require 'singleton'

class SimpleLogger
  include Singleton
end

if __FILE__ == $0
  logger1 = SimpleLogger.instance # Returns the logger
  logger2 = SimpleLogger.instance # Returns exactly the same logger
  puts "#{logger1}"
  puts "#{logger2}"

  SimpleLogger.instance.info('Computer wins chess game.')
  SimpleLogger.instance.warning('AE-35 hardware failure predicted.')
  SimpleLogger.instance.error('HAL-9000 malfunction, take emergency action!')
end
