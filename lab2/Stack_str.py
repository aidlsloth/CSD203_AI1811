class Stack:
   def __init__(self):
      self.data = []

   def __len__(self):
      return len(self.data)
   
   def is_empty(self):
      return self.__len__() == 0
   
   def clear(self):
      self.data = []

   def push(self, data):
      return self.data.append(data)
   
   def pop(self):
      if self.is_empty is True:
         raise Exception
      return self.data.pop()
   
   def top(self):
      if self.is_empty is True:
         raise Exception
      return self.data[-1]
   
   def traverse(self):
      for i in range(self.__len__() - 1, -1, -1):
         print(self.data[i], end = ' ')

   def convertor(self, data):
      data = int(data)
      while data != 0:
         a = data%2
         self.data.append(a)
         data = data // 2

      for j in range(self.__len__() - 1, -1, -1):
         print(self.data[j], end = '')


if __name__ == "__main__":
    stack = Stack()

    print(stack.is_empty())

    stack.push("str1")
    stack.push("str2")
    stack.push("str3")

    stack.pop()

    print(stack.__len__())

    print(stack.top())

    print(stack.traverse())

    stack.clear()
    print(stack.is_empty())
    stack.convertor(10)