import { NgModule } from '@angular/core';
import {BrowserModule } from '@angular/platform-browser';
import {AppComponent } from './app.component';
import {FormsModule} from "@angular/forms";
import {LoginComponentComponent } from './components/login-component/login-component.component';
import {HttpClientModule} from "@angular/common/http";
import {RegisterComponentComponent } from './components/register-component/register-component.component';
import {Routes, RouterModule} from "@angular/router";





const routes: Routes = [
  { path: '', component: RegisterComponentComponent },
  { path: 'register', component: RegisterComponentComponent },
  { path: 'login', component: LoginComponentComponent },
];

@NgModule({
  declarations: [
    AppComponent,
    LoginComponentComponent,
    RegisterComponentComponent,

  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot(routes),


  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
