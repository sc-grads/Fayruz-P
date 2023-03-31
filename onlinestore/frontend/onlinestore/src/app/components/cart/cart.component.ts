import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface CartItem {
  product_name: string;
  product_price: number;
  quantity: number;
  product_ID: number;
}

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent implements OnInit {

  items: CartItem[] = [];

  constructor(private http: HttpClient) { }

 ngOnInit(): void {
  this.http.get<any>('http://localhost:5000/cart').subscribe((items) => {
    console.log(items)
    this.items = items;
    console.log(items);
  });
}








  removeFromCart(itemId: number) {
    this.http.post('http://localhost:5000/remove_from_cart', { product_ID: itemId }).subscribe(response => {
      console.log(response);
    });
  }

  getTotal() {
    return this.items.reduce((total, item) => total + item.product_price * item.quantity, 0);
  }

}
