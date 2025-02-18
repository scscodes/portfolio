import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

/**
 * Home component serving as the main landing page
 * Displays brand icons in a vertical layout
 */
@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="icon-container">
      <img src="assets/red-k.webp" alt="Red icon" class="icon">
      <img src="assets/green-s.webp" alt="Green icon" class="icon">
      <img src="assets/blue-a.webp" alt="Blue icon" class="icon">
    </div>
  `,
  styles: `
    .icon-container {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      align-items: center;
      padding: 1rem;
    }
    
    .icon {
      width: 48px;
      height: 48px;
    }
  `
})
export class HomeComponent {
  constructor() {
    console.log('HomeComponent');
  }
}
