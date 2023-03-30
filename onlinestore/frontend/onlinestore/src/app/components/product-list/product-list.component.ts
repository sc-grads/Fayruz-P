import { Component, OnInit } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";

interface Product {

  product_name: string;
  product_price: number;
  product_size: string;
  product_ID: number;


}
@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit{

  products: Product[] = [];

  constructor(private http: HttpClient) { }

  // ngOnInit(): void {
  //   const header = new HttpHeaders({'Content-Type': 'products/json','Access-Control-Allow-Origin':'*'})
  //   this.http.get('http://localhost:5000/shop', {headers:header}).subscribe((products) => {
  //     console.log(products);
  //   });
  // }

  ngOnInit(): void {
    this.http.get<any[]>('http://localhost:5000/shop').subscribe(data => {
      this.products = data;
    });
  }

  addToCart(productId: number) {
    this.http.post('http://localhost:5000/add_to_cart', { product_id: productId, quantity: 1 }).subscribe(response => {
      console.log(response);
    });
  }
}
