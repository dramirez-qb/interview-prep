require 'singleton'

class Manager
  include Singleton

  def manage_resources
    puts 'I am managing my resources'
  end
end
