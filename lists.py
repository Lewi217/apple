#list slicing

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

#matrix-a way to describe 2d list

matrix = [
    [1,0,1],
    [0,1,0],
    [1,0,1]
    ]