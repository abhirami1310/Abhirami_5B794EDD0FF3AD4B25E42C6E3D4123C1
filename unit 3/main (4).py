def linearSearchProduct(productList,targetProduct):
  indices=[]

  for index,product in enumerate(productList):
   if product==targetProduct:
    indices.append(index)

  return indices



Products=["shoes","sandal","shoes"]
target="shoes"
result=linearSearchProduct(Products,target)
print(result)