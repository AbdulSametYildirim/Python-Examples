def countUniqeInArray(array):
  count = 0
  element=""
  farkli = 1

  myRealArray = []
  toplamFarkli=0
  temporaryArray = array
  keys = [0] * (len(array)-1)
  for i in range(1,len(temporaryArray)):
       keys[i-1] = temporaryArray[i][-1]
       #print(keys)

  for i in range(0,len(keys)):
    if(keys[i] != None):
      for j in range(i+1,len(keys)):
        if(keys[i] == keys[j] and keys[j] != None):
          #print(keys[i] + keys[j])
          farkli = farkli+1
          keys[j] = None
      if farkli != 1:
        myRealArray.append([keys[i],farkli])
        toplamFarkli= toplamFarkli+1
        farkli = 1
      else:
        myRealArray.append([keys[i], farkli])
        toplamFarkli = toplamFarkli + 1
        farkli = 1
  print(myRealArray)
  print(toplamFarkli)
  print(len(keys))


  #print(keys)
  """
     match_found = False
     for j in range(1, len(self.temporaryArray)):
       birinci = self.temporaryArray[i][-1]
       ikinci = self.temporaryArray[j][-1]
       if(birinci == ikinci and i != j ):
         match_found = True
         element = self.temporaryArray[i][-1]
         self.temporaryArray.pop(j)

     if(match_found):
       count = count+1
       for i in range(1, len(self.temporaryArray)):
        for j in self.temporaryArray[i][-1]:
          if j == element:
            self.temporaryArray.pop(i)



       match_found = False
  return count
"""
class IG:
  def __init__(self, array):
    self.array = array
    self.difference=0
    #print(array[-1])

  def Entropy(self):
    self.temporaryArray = []
    """ 
    for i in reversed(range(1,len(self.array))):
      print(self.array[i][-1])
    """
    countUniqeInArray(self.array)









