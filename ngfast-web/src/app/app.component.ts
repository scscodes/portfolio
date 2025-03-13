import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MatIconModule } from '@angular/material/icon';
import { MatMenuModule } from '@angular/material/menu';
import { MatButtonModule } from '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { HeaderComponent } from './shared/layout/header.component';

/**
 * Root component for the portfolio application
 */
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    HeaderComponent,
    MatListModule,
    MatSidenavModule,
    MatIconModule,
    MatButtonModule,
    MatMenuModule,
    MatToolbarModule
  ],
  template: `
    <div class="app">
      <app-header></app-header>
      <main class="app__content">
        <router-outlet></router-outlet>
      </main>
      <footer class="app__footer">
        <div class="container">
          <p class="app__copyright">© 2023 Steven Salmons. All rights reserved.</p>
          <div class="app__social">
            <a href="https://github.com/scscodes" target="_blank" aria-label="GitHub">
              <mat-icon>code</mat-icon>
            </a>
            <a href="https://linkedin.com/in/ssalmons" target="_blank" aria-label="LinkedIn">
              <mat-icon>link</mat-icon>
            </a>
          </div>
        </div>
      </footer>
    </div>
  `,
  styles: `
    .app {
      display: flex;
      flex-direction: column;
      min-height: 100vh;
      
      &__content {
        flex: 1;
      }
      
      &__footer {
        background-color: #333;
        color: white;
        padding: 1.5rem 0;
        margin-top: 2rem;
        
        .container {
          display: flex;
          justify-content: space-between;
          align-items: center;
          
          @media (max-width: 576px) {
            flex-direction: column;
            gap: 1rem;
          }
        }
      }
      
      &__copyright {
        margin: 0;
      }
      
      &__social {
        display: flex;
        gap: 1rem;
        
        a {
          color: white;
          display: flex;
          align-items: center;
          justify-content: center;
          width: 36px;
          height: 36px;
          border-radius: 50%;
          background-color: rgba(255, 255, 255, 0.1);
          transition: background-color 0.3s ease;
          
          &:hover {
            background-color: rgba(255, 255, 255, 0.2);
          }
        }
      }
    }
  `
})
export class AppComponent {
  title = 'Portfolio';
}
