import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { AuthButtonComponent } from '../../core/auth-controls';
import { SettingsButtonComponent } from '../../core/settings-controls';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatMenuModule } from '@angular/material/menu';
import { CommonModule } from '@angular/common';
import { MatDividerModule } from '@angular/material/divider';
/**
 * Header component providing navigation and authentication controls
 */

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [
    CommonModule,
    RouterLink, 
    AuthButtonComponent,
    SettingsButtonComponent,
    MatToolbarModule, 
    MatButtonModule,
    MatIconModule,
    MatMenuModule,
    MatDividerModule,
  ],
  template: `
    <mat-toolbar color="primary">
      <a mat-button routerLink="/">
        <span class="logo">NgFast</span>
      </a>
      <span class="spacer"></span>
      
      <!-- Desktop Navigation -->
      <div class="nav-links desktop-only">
        <a mat-button routerLink="/about">About</a>
        <a mat-button routerLink="/portfolio">Portfolio</a>
        <a mat-button routerLink="/connect">Connect</a>
        <a mat-button routerLink="/generic">Generic</a>
      </div>

      <span class="spacer"></span>
      
      <!-- Mobile Menu Button -->
      <button mat-icon-button 
              [matMenuTriggerFor]="menu" 
              class="mobile-only menu-button">
        <mat-icon>menu</mat-icon>
      </button>

      <!-- Mobile Menu -->
      <mat-menu #menu="matMenu">
        <a mat-menu-item routerLink="/about">About</a>
        <a mat-menu-item routerLink="/portfolio">Portfolio</a>
        <a mat-menu-item routerLink="/connect">Connect</a>
        <a mat-menu-item routerLink="/generic">Generic</a>
        <mat-divider></mat-divider>
        <div class="menu-controls">
          <app-settings-button></app-settings-button>
          <app-auth-button></app-auth-button>
        </div>
      </mat-menu>

      <!-- Desktop Controls -->
      <div class="nav-controls desktop-only">
        <app-settings-button></app-settings-button>
        <app-auth-button></app-auth-button>
      </div>
    </mat-toolbar>
  `,
  styles: [`
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

    .menu-controls {
      display: flex;
      justify-content: space-around;
      padding: 8px 16px;
    }

    /* Mobile-first approach */
    .desktop-only {
      display: none;
    }

    .mobile-only {
      display: flex;
    }

    /* Tablet and up */
    @media (min-width: 768px) {
      .desktop-only {
        display: flex;
      }

      .mobile-only {
        display: none;
      }
    }

    /* Ensure menu items are properly styled */
    ::ng-deep .mat-mdc-menu-panel {
      max-width: none !important;
      
      .mat-mdc-menu-item {
        display: flex;
        align-items: center;
        gap: 8px;
      }
    }
  `]
})
export class HeaderComponent {
  constructor() {}
}
