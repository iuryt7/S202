from database import Database
from personModel import BookModel
from cli import BookCLI
from writeAJson import writeAJson
db = Database(database="relatorio5", collection="Livros")
bookModel = BookModel(database=db)


personCLI = BookCLI(bookModel)
personCLI.run()