import { Component } from '@angular/core';
import {LoginComponentComponent} from "../login-component/login-component.component";
@Component({
  selector: 'app-dashboard-component',
  templateUrl: './dashboard-component.component.html',
  styleUrls: ['./dashboard-component.component.css']
})
export class DashboardComponentComponent {
  constructor(private loginComponent: LoginComponentComponent) { }

  onLogoutClick() {
    this.loginComponent.onlogout();
  }



}
