#include <iostream>
#include <cstdlib>
#include <string>  // Required for std::string

using namespace std;

struct Product {
    int productID;
    string code;
    string name; 
    float price; 
    int quantity;
};


Product* getProducts();
Product getOneProduct(int productID);
Product addProduct(Product product);
Product updateProduct(int productID, Product product);
Product deleteProduct(int productID);

void displayProducts(Product *products);
Product inputProduct();

Product products[10];
int ProductCount = 0;

int main()
{
    char input;

    do {
        system("clear");
        cout << "1.     Show Products" << endl;
        cout << "2.     Add Product" << endl;
        cout << "3.     Update Product" << endl;
        cout << "4.     Delete Product" << endl;
    
        cout << "Enter your chice [1-4], 0 for Exit? ";
        cin >> input;
        
        switch (input) {
            case '1':
                displayProducts(products);
                break;
            case '2':
                Product product = inputProduct();
                addProduct(product);
                break;
        }
        
    } while (input!='0');
    
    return 0;
}

Product* getProducts() {
    return products;
}

Product getOneProduct(string code) {
    Product product;
    
    return product;
}

Product addProduct(Product product) {
    products[ProductCount].productID = ProductCount+1;
    products[ProductCount].code = product.code;
    products[ProductCount].name = product.name;
    products[ProductCount].price = product.price;
    products[ProductCount].quantity = product.quantity;
    
    ProductCount = ProductCount + 1;
    
    return products[ProductCount-1];
}

Product updateProduct(string code, Product product) {
    Product updatedProduct;
    
    return updatedProduct;
}

Product deleteProduct(string code) {
    Product deletedProduct;
    
    return deletedProduct;
}

void displayProducts(Product products[]) {
    system("clear");
    
    for (int i=0; i<ProductCount; i++) {
        cout << "Product Code: " << products[i].code << endl;
        cout << "Enter Product Name: " << products[i].name << endl;
        cout << "Enter Product Price: " << products[i].price << endl;
        cout << "Enter Product Quantity: " << products[i].quantity << endl << endl;
    }
    
    cout << "Press any key to continue...";
    cin.get();
    cin.get();
}

Product inputProduct() {
    Product product;
    
    system("clear");

    cout << "Enter Product Code: ";
    cin >> product.code;

    cout << "Enter Product Name: ";
    cin >> ws; // clear whitespace before getline
    getline(cin, product.name);

    cout << "Enter Product Price: ";
    cin >> product.price;

    cout << "Enter Product Quantity: ";
    cin >> product.quantity;

    return product; // return pointer to the product    
}

