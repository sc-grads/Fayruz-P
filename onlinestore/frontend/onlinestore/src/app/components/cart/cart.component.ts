import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {ChangeDetectorRef} from "@angular/core";
import {Location} from "@angular/common";

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

  constructor(private http: HttpClient, private location: Location) { }

 ngOnInit(): void {
    this.http.get<any>('http://localhost:5000/cart').subscribe((items) => {

    this.items = items;
    console.log(items);
  })

}



removeFromCart(itemId: number) {

  this.http.delete('http://localhost:5000/remove_from_cart/' + itemId).subscribe(response => {
    console.log(response);
    // Find index of item with specified itemId in local items array
    const index = this.items.findIndex(item => item.product_ID === itemId);
    if (index !== -1) {
      // Remove item from local items array
      this.items.splice(index, 1);
      // Trigger change detection to update the view
      window.location.reload();
    }
  });
}


  getTotal() {
    return this.items.reduce((total, item) => total + item.product_price * item.quantity, 0);
  }

}
