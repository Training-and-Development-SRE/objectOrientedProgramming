import product
import store

if __name__ == "__main__":
    shoe = product.Product("tennis shoe", 30, 5, "Nike")
    walmart = store.Store([shoe],"Chicago","Chris Poche")
    walmart.inventory()
    ## product.shoe2.display() -- doesn't work because of namespace check