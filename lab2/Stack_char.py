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
      lis = list(data)
      for i in range(len(lis)-1, -1, -1):
        self.data.append(lis[i])
   
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

    stack.push("string")
    stack.traverse()