import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

interface Product {
  product_name: string;
  product_price: number;
  product_weight: string;
  product_ID: number;
  product_image: string;
}

interface NewProduct {
  product_name: string;
  product_price: number;
  product_weight: string;
  product_image: string;
}

@Component({
  selector: 'app-product-management',
  templateUrl: './product-management.component.html',
  styleUrls: ['./product-management.component.css']
})
export class ProductManagementComponent implements OnInit {
  products: Product[] = [];
  newProduct: NewProduct = {
    product_name: '',
    product_price: 0,
    product_weight: '',
    product_image: ''
  };
  showAddProductForm: boolean = false;
  showEditProductForm: boolean = false;
  selectedProduct: Product | null = null;
  isAdminLoggedIn: boolean = false;


  constructor(private http: HttpClient, private router: Router) {}

  ngOnInit(): void {
    this.checkAdminLoginStatus();
    this.loadProducts();
  }

  checkAdminLoginStatus() {
    this.http.get('http://localhost:5000/checkadminlogin').subscribe(
      (response: any) => {
        if (response && response['status'] === 'success') {
          // Admin is logged in
          this.isAdminLoggedIn = true;
        } else {
          // Admin is not logged in
          this.isAdminLoggedIn = false;
        }
      },
      error => {
        console.error(error);
        // Set the flag to false in case of an error
        this.isAdminLoggedIn = false;
      }
    );
  }

 loadProducts(): void {
  if (!this.isAdminLoggedIn) {
    alert('Please log in as an admin to view and manage products.');
    return;
  }

  this.http.get<Product[]>('http://localhost:5000/shop').subscribe(
    data => {
      this.products = data;
    },
    error => {
      console.error(error);
      alert('An error occurred while loading products. Please try again later.');
    }
  );
}


deleteProduct(productId: number): void {
  if (!this.isAdminLoggedIn) {
    alert('Please log in as an admin to delete products.');
    return;
  }

  if (confirm('Are you sure you want to delete this product?')) {
    this.http.delete(`http://localhost:5000/product/${productId}`).subscribe(
      () => {
        alert('Product deleted successfully');
        this.loadProducts();
      },
      error => {
        console.error(error);
        alert('An error occurred while deleting the product. Please try again later.');
      }
    );
  }
}


addNewProduct(): void {
  if (!this.isAdminLoggedIn) {
    alert('Please log in as an admin to add products.');
    return;
  }

  this.showAddProductForm = true;
}


  submitNewProduct(): void {
    if ( !this.isAdminLoggedIn){
      alert('Please log in as an admin to add products.');
      return;
    }
    // Send a request to add the new product to the database
    console.log('New Product:', this.newProduct);
    this.http.post('http://localhost:5000/product', this.newProduct).subscribe(
      (response: any) => {
        console.log('Response:', response);
        if (response.status === 'success') {
          alert('Product added successfully');
          this.showAddProductForm = false;
          this.clearNewProductFields();
          this.loadProducts();
        } else {
          alert('Failed to add product. Check the database connection and verify the data.');
        }
      },
      error => {
        console.error(error);
        alert('An error occurred while adding the product. Please try again later.');
      }
    );
  }

editProduct(productId: number): void {
  if (!this.isAdminLoggedIn) {
    alert('Please log in as an admin to edit products.');
    return;
  }

  const product = this.products.find(p => p.product_ID === productId);
  if (product) {
    this.selectedProduct = { ...product }; // Create a copy of the product object
    this.showEditProductForm = true;
  }
}


  submitEditedProduct(): void {
    if (this.selectedProduct) {
      this.http.put(`http://localhost:5000/product/${this.selectedProduct.product_ID}`, this.selectedProduct)
        .subscribe(
          (response: any) => {
            console.log('Response:', response);
            if (response.status === 'success') {
              alert('Product updated successfully');
              this.showEditProductForm = false;
              this.clearSelectedProduct();
              this.loadProducts();
            } else {
              alert('Failed to update product. Check the database connection and verify the data.');
            }
          },
          error => {
            console.error(error);
            alert('An error occurred while updating the product. Please try again later.');
          }
        );
    }
  }

  clearSelectedProduct(): void {
    this.selectedProduct = null;
  }

  clearNewProductFields(): void {
    this.newProduct.product_name = '';
    this.newProduct.product_price = 0;
    this.newProduct.product_weight = '';
    this.newProduct.product_image = '';
  }


cancelAddProduct(): void {
  this.showAddProductForm = false;
  this.clearNewProductFields();
}

cancelEditProduct(): void {
  this.showEditProductForm = false;
  this.clearSelectedProduct();
}
}
