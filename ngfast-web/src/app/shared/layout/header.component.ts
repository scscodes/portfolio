import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { CommonModule } from '@angular/common';

/**
 * Header component providing navigation for the portfolio SPA
 */
@Component({
  selector: 'app-header',
  standalone: true,
  imports: [
    CommonModule,
    RouterLink,
    RouterLinkActive,
    MatToolbarModule,
    MatButtonModule,
    MatIconModule
  ],
  template: `
    <mat-toolbar color="primary" class="header">
      <div class="header__logo">
        <a routerLink="/" class="header__title">Steven Salmons</a>
      </div>
      
      <div class="header__spacer"></div>
      
      <nav class="header__nav">
        <a mat-button routerLink="/about" routerLinkActive="header__nav-item--active" class="header__nav-item">
          <mat-icon>person</mat-icon>
          About
        </a>
        <a mat-button routerLink="/portfolio" routerLinkActive="header__nav-item--active" class="header__nav-item">
          <mat-icon>work</mat-icon>
          Portfolio
        </a>
      </nav>
    </mat-toolbar>
  `,
  styles: `
    .header {
      position: sticky;
      top: 0;
      z-index: 1000;
      
      &__logo {
        display: flex;
        align-items: center;
      }
      
      &__title {
        text-decoration: none;
        color: white;
        font-size: 1.5rem;
        font-weight: 500;
      }
      
      &__spacer {
        flex: 1 1 auto;
      }
      
      &__nav {
        display: flex;
        gap: 8px;
        
        &-item {
          display: flex;
          align-items: center;
          
          mat-icon {
            margin-right: 4px;
          }
          
          &--active {
            background-color: rgba(255, 255, 255, 0.15);
          }
        }
      }
    }
  `
})
export class HeaderComponent {} 