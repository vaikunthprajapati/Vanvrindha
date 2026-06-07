from master.Repository.Categoryrepo import CategoryRepo

class CategoryService:

    def __init__(self):
        self.repo = CategoryRepo()

    def getAll(self):
        return self.repo.getAll()