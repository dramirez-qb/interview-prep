require_relative 'all'
require_relative 'writable'
require_relative 'bigger'
require_relative 'filename'
require_relative 'not'
require_relative 'and'
require_relative 'or'

class Parser
	def initialize(text)
		@tokens = text.scan(/\(|\)|[\w\.\*]+/)
	end

	def next_token
		@tokens.shift
	end

	def expression
		token = next_token
		case token
		when nil
			nil
		when '('
			result = expression
			raise 'Expected )' unless next_token == ')'
			result
		when 'all'
			All.new
		when 'writable'
			Writable.new
		when 'bigger'
			Bigger.new(next_token.to_i)
		when 'filename'
			FileName.new(next_token)
		when 'not'
			Not.new(expression)
		when 'and'
			And.new(expression, expression)
		when 'or'
			Or.new(expression, expression)
		else
			raise "Unexpected token: #{token}"
		end
	end
end
