from django.core.files.storage import FileSystemStorage

from master.Entity.product import Product
from master.Repository.Productrepo import productRepo


class ProductService:

    def __init__(self):
        self.repo = productRepo()

    def addProduct(self, request):

        product = Product()

        product.pname = request.POST["pname"]
        product.description = request.POST["description"]
        product.price = request.POST["price"]
        product.cid = request.POST["category"]
        product.plant_size = request.POST["plant_size"]
        product.plant_weight = request.POST["plant_weight"]
        product.soil_type = request.POST["soil_type"]

        # Validation
        if product.pname.strip() == "":
            return "Plant name required"

        try:
            if float(product.price) <= 0:
                return "Invalid price"
        except:
            return "Price must be numeric"

        image = request.FILES.get("image")
        if image:
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            product.image = filename

        else:
            product.image = "no-image.jpg"
        return self.repo.addProduct(product)

    def getAllProducts(self):
        return self.repo.getAllProducts()

    def getProductById(self, id):
        return self.repo.getProductById(id)

    def updateProduct(self, request, id):

        product = Product()

        product.id = id

        product.pname = request.POST["pname"]
        product.description = request.POST["description"]
        product.price = request.POST["price"]

        return self.repo.updateProduct(product)

    def deleteProduct(self, id):
        return self.repo.deleteProduct(id)
    
    def getAllProducts(self):
        return self.repo.getAllProducts()
    
    def getProductById(self, id):
        return self.repo.getProductById(id)
    
    def getProductsByIds(self, ids):

     return self.repo.getProductsByIds(ids)
 
    def searchProducts(self, keyword):

     return self.repo.searchProducts(keyword)
 
    def getProductsByCategory(self, category_id):

       return self.repo.getProductsByCategory(category_id)
   
    def searchProductsByCategory(self, keyword, category):

        return self.repo.searchProductsByCategory(keyword, category)