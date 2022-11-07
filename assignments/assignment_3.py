### HOW to sort a list based on dictionary values.
cells=list()
cells.append({'name':'Iphone','price':1000})
cells.append({'name':'Samsung','price':998})
cells.append({'name':'Blackberry','price':300})
cells.append({'name':'Mottorla','price':430})
print('Sorted list by price value in cell list')
fn=lambda x: x['price']
cells.sort(key= fn)
print(cells)
## or you can create a lambda inside sort and reverse the order!!
cells.sort(key=lambda item:item['price'],reverse=True)
print(cells)

