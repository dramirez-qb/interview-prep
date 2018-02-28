require_relative 'parser'

# using parser
puts 'Interpreter pattern using parser'
puts 'Syntax: and(and(bigger 10) (filename *.rb) writable)'
parser = Parser.new('and (and (bigger 10) (filename *.rb)) writable')
ast = parser.expression
puts ast.evaluate('.')
puts

# parser-less interpreter
puts 'Interpreter pattern without a parser'
puts "Syntax: bigger(10) & name('*.rb') & writable"
ast = bigger(10) & name('*.rb') & writable
puts ast.evaluate('.')
