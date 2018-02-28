class Object
  def self.readable_attribute(name)
    code = %Q{
      def #{name}
        @#{name}
      end
    }

    class_eval(code)
  end
end
