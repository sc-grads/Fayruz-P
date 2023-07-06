
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { DomSanitizer } from '@angular/platform-browser';

interface Product {
  product_name: string;
  product_price: number;
  product_size: string;
  product_ID: number;
  product_image: string;
}

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {
  products: Product[] = [];
  isLoggedIn: boolean = false; // New property to track login status
  constructor(private http: HttpClient, private sanitizer: DomSanitizer) { }

  ngOnInit(): void {
    this.http.get<any[]>('http://localhost:5000/shop').subscribe(data => {
      this.products = data;
    });
  }


  addToCart(productId: number) {
  this.http.post('http://localhost:5000/add_to_cart', { product_id: productId, quantity: 1 }).subscribe(
    (response: any) => {
      console.log(response);
      // Check if adding to cart was successful based on response
      if (response && response['status'] === 'success') {
        // Adding to cart was successful, show success alert
        alert('Item added to cart!');
      } else {
        // Adding to cart failed, show error alert with error message from backend
        alert('Failed to add item to cart. ' + response['message']);
      }
    },
    (error) => {
      console.error(error);
      alert('An error occurred while adding item to cart. Please try again later.');
    }
  );
}

checkSessionStatus(): void {
  this.http.get<boolean>('http://localhost:5000/check_session_status').subscribe(
    (isLoggedIn: boolean) => {
      this.isLoggedIn = isLoggedIn;
    },
    (error) => {
      console.error(error);
      // Handle the error appropriately, such as showing an error message to the user
    }
  );
}

  sanitizeUrl(url: string) {
    return this.sanitizer.bypassSecurityTrustUrl(url);
  }

}
