require_relative 'pref_reader'
require_relative 'pref_writer'
require_relative 'database_connection_manager'

class PreferenceManager
  def initialize
    @reader = PrefReader.new
    @writer = PrefWriter.new
    @preferences = { display_splash: false, background_color: :blue }
  end

  def save_preferences
    preferences = {}
    # Preferences are in
    @writer.write(DatabaseConnectionManager.instance, @preferences)
  end

  def get_preferences
    @preferences = @reader.read(DatabaseConnectionManager.instance)
  end
end
