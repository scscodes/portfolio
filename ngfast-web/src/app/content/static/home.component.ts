import { Component } from '@angular/core';

/**
 * Home component serving as the main landing page
 */
@Component({
  selector: 'app-home',
  standalone: true,
  imports: [],
  template: `home!`,
  styles: ``
})
export class HomeComponent {
  constructor() {
    console.log('HomeComponent');
  }
}
