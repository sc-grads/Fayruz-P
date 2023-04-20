import { Component } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Router} from "@angular/router";
@Component({
  selector: 'app-login-component',
  templateUrl: './login-component.component.html',
  styleUrls: ['./login-component.component.css']
})
export class LoginComponentComponent {

constructor(private http:HttpClient, private router: Router){}

isLoggedIn: boolean = false;
username: string = '';
password: string = '';

navigatetoDashboard(){
  this.router.navigate(['/dashboard']).then(r => console.debug("redirected"));
}


onlogin() {
      console.debug(`${this.username} ${this.password}`);
  this.http.post('http://localhost:5000/login',
    {username:this.username, password:this.password}).subscribe(
        (response: any) => {
          console.debug(`${this.username} ${this.password}${response}`);
          console.debug(response);

          // Check if registration was successful based on response
          if (response && response['status'] === 'success') {
            // Registration was successful, show success alert
            alert('Login successful!');
            this.navigatetoDashboard();
            this.isLoggedIn = true;
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

 onlogout() {
  this.http.post('http://localhost:5000/logout', {}).subscribe(
    (response: any) => {
      console.log(response);
      alert('Logout successful!');
      this.router.navigate(['/login']).then(r => console.debug("redirected"));
       this.isLoggedIn = false;
    },
    error => {
      console.error(error);
      alert('An error occurred. Please try again later.');
    }
  );
}


}
