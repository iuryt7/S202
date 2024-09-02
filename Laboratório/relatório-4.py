from pymongo import MongoClient
from datetime import datetime

class ProductAnalyzer:
    def __init__(self, db_name, collection_name):
        # Conectar ao MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        self.db = client[db_name]
        self.collection = self.db[collection_name]
    
    def total_sales_per_day(self):
        # Retorna o total de vendas por dia
        pipeline = [
            {"$group": {"_id": {"day": {"$dayOfMonth": "$date"}, "month": {"$month": "$date"}, "year": {"$year": "$date"}}, "total_sales": {"$sum": "$total"}}},
            {"$sort": {"_id.year": 1, "_id.month": 1, "_id.day": 1}}
        ]
        return list(self.collection.aggregate(pipeline))
    
    def most_sold_product(self):
        # Retorna o produto mais vendido em todas as compras
        pipeline = [
            {"$unwind": "$items"},
            {"$group": {"_id": "$items.product", "total_sold": {"$sum": "$items.quantity"}}},
            {"$sort": {"total_sold": -1}},
            {"$limit": 1}
        ]
        return self.collection.aggregate(pipeline).next()["_id"]
    
    def customer_spent_most_in_single_purchase(self):
        # Encontra o cliente que mais gastou em uma única compra
        pipeline = [
            {"$group": {"_id": "$customer_id", "max_spent": {"$max": "$total"}}},
            {"$sort": {"max_spent": -1}},
            {"$limit": 1}
        ]
        return self.collection.aggregate(pipeline).next()["_id"]
    
    def products_sold_more_than_one(self):
        # Lista todos os produtos que tiveram uma quantidade vendida acima de 1 unidades
        pipeline = [
            {"$unwind": "$items"},
            {"$group": {"_id": "$items.product", "total_quantity": {"$sum": "$items.quantity"}}},
            {"$match": {"total_quantity": {"$gt": 1}}}
        ]
        return list(self.collection.aggregate(pipeline))

# Exemplo de uso
if __name__ == "__main__":
    analyzer = ProductAnalyzer('nome_do_banco', 'nome_da_colecao')
    
    print("Total de vendas por dia:")
    print(analyzer.total_sales_per_day())
    
    print("\nProduto mais vendido:")
    print(analyzer.most_sold_product())
    
    print("\nCliente que mais gastou em uma única compra:")
    print(analyzer.customer_spent_most_in_single_purchase())
    
    print("\nProdutos vendidos mais de 1 unidade:")
    print(analyzer.products_sold_more_than_one())
