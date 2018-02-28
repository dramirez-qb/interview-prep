require_relative 'dynamic_jungle'
require_relative 'bank_account'

# Create dynamic plant
puts 'Creating dynamic plants'
plant_1 = new_plant(:fleshy, :broad)
plant_2 = new_plant(:woody, :needle)

puts "Plant 1's stem: #{plant_1.stem} leaf: #{plant_1.leaf}"
puts "Plant 2's stem: #{plant_2.stem} leaf: #{plant_2.leaf}"

# attr_reader copy
puts 'Creating bank account'
bank_account = BankAccount.new(1000)
puts "bank_account balance: #{bank_account.balance}"
