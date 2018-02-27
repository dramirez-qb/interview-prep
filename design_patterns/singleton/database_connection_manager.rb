require 'singleton'

class DatabaseConnectionManager
  include Singleton

  def get_connection
    puts 'Get database connection'
  end
end
