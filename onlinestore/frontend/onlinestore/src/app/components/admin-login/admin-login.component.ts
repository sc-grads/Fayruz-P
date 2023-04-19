import { Component } from '@angular/core';
import {Router} from "@angular/router";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-admin-login',
  templateUrl: './admin-login.component.html',
  styleUrls: ['./admin-login.component.css']
})
export class AdminLoginComponent {

  constructor(private http:HttpClient, private router: Router){}

  adminusername: string = ''
  adminpassword: string = ''

  onadminlogin() {
      console.debug(`${this.adminusername} ${this.adminpassword}`);
  this.http.post('http://localhost:5000/adminlogin',
    {username:this.adminusername, password:this.adminpassword}).subscribe(
        (response: any) => {
          console.debug(`${this.adminusername} ${this.adminpassword}${response}`);
          console.debug(response);

          // Check if registration was successful based on response
          if (response && response['status'] === 'success') {
            // Registration was successful, show success alert
            alert('Login successful!');
           // this.navigatetoDashboard();
          } else {
            // Registration failed, show error alert with error message from backend
            alert('Login failed. ' + response['message']);
          }
        },
        error => {
          // Handle error from HTTP POST request, show error alert
          console.error(error);
          alert('An error occurred. Please try again later.');
        }
      );
  }
}
