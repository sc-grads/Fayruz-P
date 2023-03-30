import { Component } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Router} from "@angular/router";
@Component({
  selector: 'app-register-component',
  templateUrl: './register-component.component.html',
  styleUrls: ['./register-component.component.css']
})
export class RegisterComponentComponent {

  constructor(private http:HttpClient,  private router: Router){}

fname: string = '';
lname: string = '';
email: string = '';
password: string = '';
number: string = '';
address: string = '';
navigatetoLogin(){
  this.router.navigate(['/login']).then(r => console.debug("redirected"));
}
onRegister(){

  console.debug(`${this.fname}${this.lname}${this.email} ${this.password}${this.number}${this.address}`);
  this.http.post('http://localhost:5000/register',
    {fname:this.fname, lname:this.lname,email:this.email,password:this.password,number:this.number,address:this.address}).subscribe(
      response=> {console.debug(`${this.fname}${this.lname}${this.email} ${this.password}${this.number}${this.address}${response}`);
  console.debug(response)});
  this.navigatetoLogin();

}




}
