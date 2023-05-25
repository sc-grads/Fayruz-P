import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { FormsModule } from "@angular/forms";
import { HttpClientModule, HttpClientXsrfModule } from "@angular/common/http";
import { LoginComponentComponent } from './components/login-component/login-component.component';
import { RegisterComponentComponent } from './components/register-component/register-component.component';
import { Routes, RouterModule } from "@angular/router";
import { DashboardComponentComponent } from './components/dashboard-component/dashboard-component.component';
import { ProductListComponent } from './components/product-list/product-list.component';
import { CartComponent } from './components/cart/cart.component';
import { AdminDashboardComponent } from './components/admin-dashboard/admin-dashboard.component';
import { AdminLoginComponent } from './components/admin-login/admin-login.component';
import { OrderManagementComponent } from './components/order-management/order-management.component';
import { ProductManagementComponent } from './components/product-management/product-management.component';



const routes: Routes = [
  { path: '', component: ProductListComponent },
  { path: 'register', component: RegisterComponentComponent },
  { path: 'login', component: LoginComponentComponent },
  { path: 'dashboard', component: DashboardComponentComponent },
  { path: 'cart', component: CartComponent },
  { path: 'adminlogin', component: AdminLoginComponent },
  { path: 'admindashboard', component: AdminDashboardComponent },
  { path: 'order-management', component: OrderManagementComponent },
  { path: 'product-management', component: ProductManagementComponent },

];

@NgModule({
  declarations: [
    AppComponent,
    LoginComponentComponent,
    RegisterComponentComponent,
    DashboardComponentComponent,
    ProductListComponent,
    CartComponent,
    AdminDashboardComponent,
    AdminLoginComponent,
    OrderManagementComponent,
    ProductManagementComponent,


  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot(routes),
    HttpClientXsrfModule,
  ],
  providers: [LoginComponentComponent], // add LoginComponentComponent to providers array
  bootstrap: [AppComponent]
})
export class AppModule { }
