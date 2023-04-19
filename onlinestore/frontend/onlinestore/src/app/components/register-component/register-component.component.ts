import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register-component',
  templateUrl: './register-component.component.html',
  styleUrls: ['./register-component.component.css']
})
export class RegisterComponentComponent {

  constructor(private http: HttpClient, private router: Router) {}

  fname: string = '';
  lname: string = '';
  email: string = '';
  password: string = '';
  number: string = '';
  address: string = '';

  navigatetoLogin() {
    this.router.navigate(['/login']).then(r => console.debug('redirected'));
  }


onRegister() {
  const emailInput = document.getElementById('email') as HTMLInputElement;
  const emailRegExp = new RegExp('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}(\\.[a-zA-Z]{2,})?$');
  if (!emailRegExp.test(emailInput.value)) {
    alert('Please enter a valid email address');
    return;
  }

  console.debug(`${this.fname}${this.lname}${this.email} ${this.password}${this.number}${this.address}`);

  this.http.post('http://localhost:5000/register', {fname: this.fname, lname: this.lname, email: this.email, password: this.password, number: this.number, address: this.address})
    .subscribe((response: any) => {
      console.debug(`${this.fname}${this.lname}${this.email} ${this.password}${this.number}${this.address}${response}`);
      console.debug(response);

      // Check if registration was successful based on response
      if (response && response['status'] === 'success') {
        // Registration was successful, show success alert
        alert('Registration successful!');
        this.navigatetoLogin();
      } else {
        // Registration failed, show error alert with error message from backend
        alert('Registration failed. ' + response['message']);
      }
    },
    error => {
      // Handle error from HTTP POST request, show error alert
      console.error(error);
      alert('An error occurred. Please try again later.');
    });
}


}
