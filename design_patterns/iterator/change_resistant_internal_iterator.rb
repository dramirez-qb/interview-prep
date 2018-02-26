def change_resistant_for_each_element(array)
  copy = Array.new(array)
  i = 0
  while i < copy.length
    yield(copy[i])
    i += 1
  end
end
