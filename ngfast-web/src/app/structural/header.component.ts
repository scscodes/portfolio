import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { AuthButtonComponent } from '../core/auth-controls';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';

/**
 * Header component providing navigation and authentication controls
 */

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [RouterLink, AuthButtonComponent, MatToolbarModule, MatButtonModule],
  template: `
    <mat-toolbar color="primary">
      <a mat-button routerLink="/">
        <span class="logo">NgFast</span>
      </a>
      <span class="spacer"></span>
      <div class="nav-controls">
        <app-auth-button></app-auth-button>
      </div>
    </mat-toolbar>
  `,
  styles: `
    .spacer {
      flex: 1 1 auto;
    }
    .logo {
      font-size: 1.2rem;
      font-weight: 500;
    }
  `
})
export class HeaderComponent {
  constructor() {}
}
