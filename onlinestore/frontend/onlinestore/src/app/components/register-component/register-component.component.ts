import { Component } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-register-component',
  templateUrl: './register-component.component.html',
  styleUrls: ['./register-component.component.css']
})
export class RegisterComponentComponent {

  constructor(private http:HttpClient){}

fname: string = '';
lname: string = '';
username: string = '';
email: string = '';
password: string = '';
number: string = '';
address: string = '';

onRegister(){

  console.debug(`${this.fname}${this.lname}${this.username}${this.email} ${this.password}${this.number}${this.address}`);
  this.http.post('http://localhost:5000/login',
    {username:this.username, password:this.password}).subscribe(
      response=> {console.debug(`${this.username} ${response}${this.password}`);
  console.debug(response)});
}




}
