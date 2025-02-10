import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { AuthButtonComponent } from '../../core/auth-controls';
import { SettingsButtonComponent } from '../../core/settings-controls';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';


/**
 * Header component providing navigation and authentication controls
 */

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [
    RouterLink, 
    AuthButtonComponent,
    SettingsButtonComponent,
    MatToolbarModule, 
    MatButtonModule
  ],
  template: `
    <mat-toolbar color="primary">
      <a mat-button routerLink="/">
        <span class="logo">NgFast</span>
      </a>
      <span class="spacer"></span>
      
      <div class="nav-links">
        <a mat-button routerLink="/about">About</a>
        <a mat-button routerLink="/portfolio">Portfolio</a>
        <a mat-button routerLink="/connect">Connect</a>
      </div>

      <span class="spacer"></span>
      <div class="nav-controls">
        <app-settings-button></app-settings-button>
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
    .nav-links {
      display: flex;
      gap: 1rem;
      align-items: center;
    }
    .nav-controls {
      display: flex;
      gap: 0.5rem;
      align-items: center;
    }
  `
})
export class HeaderComponent {
  constructor() {}
}
