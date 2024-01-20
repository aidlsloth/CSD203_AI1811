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

      while data != 0:
         a = data%2
         self.data.append(a)
         data = data // 2

      for j in range(self.__len__() - 1, -1, -1):
         print(self.data[j], end = '')


if __name__ == "__main__":
   stack = Stack()

   print(stack.is_empty())

   for i in range(1, 20, 3):
      stack.push(i)
   print('Stack Length: ', stack.__len__())

   for _ in range(1, 10, 3):
      stack.pop()

   print("Stack top: ", stack.top())
   print("Stack Length: ", stack.__len__())
   stack.traverse()
   stack.clear()
   stack.convertor(10)











