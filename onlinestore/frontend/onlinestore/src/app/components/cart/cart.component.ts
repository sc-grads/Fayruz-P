
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ChangeDetectorRef } from '@angular/core';
import { Location } from '@angular/common';

interface CartItem {
  product_name: string;
  product_price: number;
  quantity: number;
  product_ID: number;
}

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css'],
})
export class CartComponent implements OnInit {
  items: CartItem[] = [];
  isLoggedIn: boolean = false; // Add this variable and set it based on user login status

  constructor(
    private http: HttpClient,
    private location: Location,
    private cdr: ChangeDetectorRef
  ) {}

  checkout() {
    this.http
      .post('http://localhost:5000/checkout', {})
      .subscribe((response) => {
        console.log(response);
        // Handle the response and perform necessary actions (e.g., redirect to payment page)
      });
  }

  ngOnInit(): void {
    this.http.get<any>('http://localhost:5000/check_session_status').subscribe((response) => {
      this.isLoggedIn = response; // Set the isLoggedIn variable based on the response
      if (this.isLoggedIn) {
        this.http.get<any>('http://localhost:5000/cart').subscribe((items) => {
          // Loop through the retrieved items and construct the image URLs
          for (const item of items) {
            item.imageSrc = 'http://localhost:5000/' + item.product_image; // Construct the image URL
          }
          this.items = items;
          console.log(items);
          this.cdr.detectChanges(); // Trigger change detection
        });
      }
    });
  }

  getUniqueItems(): CartItem[] {
    const uniqueItems: CartItem[] = [];
    const uniqueIds: number[] = [];

    for (const item of this.items) {
      if (!uniqueIds.includes(item.product_ID)) {
        uniqueIds.push(item.product_ID);
        uniqueItems.push(item);
      }
    }

    return uniqueItems;
  }

  getItemQuantity(item: CartItem): number {
    let quantity = 0;

    for (const cartItem of this.items) {
      if (cartItem.product_ID === item.product_ID) {
        quantity += cartItem.quantity;
      }
    }

    return quantity;
  }

  removeFromCart(itemId: number) {
    this.http
      .delete('http://localhost:5000/remove_from_cart/' + itemId)
      .subscribe((response) => {
        console.log(response);
        // Find index of item with specified itemId in local items array
        const index = this.items.findIndex(
          (item) => item.product_ID === itemId
        );
        if (index !== -1) {
          // Remove item from local items array
          this.items.splice(index, 1);
        }
        this.cdr.detectChanges(); // Trigger change detection
      });
  }

  getItemSubtotal(item: CartItem): number {
    return item.product_price * this.getItemQuantity(item);
  }

  getTotal(): number {
    return this.getUniqueItems().reduce(
      (total, item) => total + this.getItemSubtotal(item),
      0
    );
  }
}

