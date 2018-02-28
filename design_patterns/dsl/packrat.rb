require_relative 'singleton'

class PackRat
  include Singleton

  def initialize
    @backups = []
  end

  def register_backup(backup)
    @backups << backup
  end

  def run
    threads = []
    @backups.each do |backup|
      threads << Thread.new { backup.run }
    end

    threads.each { |t| t.join }
  end
end

eval(File.read('./backup.pr'))
Backup.instance.run
