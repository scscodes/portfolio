import { Component } from '@angular/core';
import { AuthButtonComponent } from '../core/auth-controls';

/**
 * Home component serving as the main landing page
 */
@Component({
  selector: 'app-home',
  standalone: true,
  imports: [],
  template: ``,
  styles: ``
})
export class HomeComponent {
  constructor() {
    console.log('HomeComponent');
  }
}
