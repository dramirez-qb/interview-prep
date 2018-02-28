require_relative 'carnivore'
require_relative 'herbivore'

def new_plant(stem_type, leaf_type)
  plant = Object.new

  if stem_type == :fleshy
    def plant.stem
      'fleshy'
    end
  else
    def plant.stem
      'woody'
    end
  end

  if leaf_type == :broad
    def plant.leaf
      'broad'
    end
  else
    def plant.leaf
      'needle'
    end
  end

  plant
end

def new_animal(diet, awake)
  animal = Object.new

  if diet == :meat
    animal.extend(Carnivore)
  else
    animal.extend(Herbivore)
  end

  if awake == :day
    animal.extend(Diurnal)
  else
    animal.extend(Nocturnal)
  end
end
