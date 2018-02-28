require_relative 'readable_attribute'

class BankAccount
  readable_attribute :balance
  
  def initialize(balance)
    @balance = balance
  end
end
