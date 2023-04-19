
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { DomSanitizer } from '@angular/platform-browser';

interface Product {
  product_name: string;
  product_price: number;
  product_size: string;
  product_ID: number;
  product_image: any;
}

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {
  products: Product[] = [];

  constructor(private http: HttpClient, private sanitizer: DomSanitizer) { }

  // ngOnInit(): void {
  //   this.http.get<any[]>('http://localhost:5000/shop').subscribe(data => {
  //     this.products = data;
  //   });
  // }

  ngOnInit(): void {
  this.http.get<any[]>('http://localhost:5000/shop').subscribe(data => {
    this.products = data;
    this.products.forEach(product => {
      const reader = new FileReader();
      reader.onload = (e: any) => {
        product.product_image = e.target.result;
      };
      reader.readAsDataURL(new Blob([product.product_image]));
    });
  });
}


  addToCart(productId: number) {
    this.http.post('http://localhost:5000/add_to_cart', { product_id: productId, quantity: 1 }).subscribe(response => {
      console.log(response);
    });
  }

  sanitizeUrl(url: string) {
    return this.sanitizer.bypassSecurityTrustUrl(url);
  }

}
