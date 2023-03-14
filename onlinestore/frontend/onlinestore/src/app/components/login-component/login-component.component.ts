import { Component } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-login-component',
  templateUrl: './login-component.component.html',
  styleUrls: ['./login-component.component.css']
})
export class LoginComponentComponent {

constructor(private http:HttpClient){}

username: string = '';
password: string = '';


onlogin(){

  console.debug(`${this.username} ${this.password}`);
  this.http.post('http://localhost:5000/login',
    {username:this.username, password:this.password}).subscribe(
      response=> {console.debug(`${this.username} ${response}${this.password}`);
  console.debug(response)});
}



}
