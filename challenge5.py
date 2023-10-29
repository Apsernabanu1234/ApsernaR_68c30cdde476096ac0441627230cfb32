Def linearSearchProduct (productList, targetProduct):
  Indices = []

  For index, product in enumerate(productList): 
    If product == targetProduct:
     Indices.append(index)

  Return indices


# Example usage:
Products = [“shoes”, “boot”, “loafer”, “shoes”, “sandal”,”shoes”]
Target = shoes
Result = linearSearchProduct(products, target)
Print(result)
