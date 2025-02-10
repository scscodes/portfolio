import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

/**
 * Component displayed when a route is not found
 * Provides a link back to the home page
 */
@Component({
  selector: 'app-not-found',
  standalone: true,
  imports: [RouterLink],
  template: `
    <div class="not-found">
      <h1>404 - Page Not Found</h1>
      <p>The page you are looking for does not exist.</p>
      <a routerLink="/">Return to Home</a>
    </div>
  `,
  styles: `
  `
})
export class NotFoundComponent {}
