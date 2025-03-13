import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';

/**
 * Home component serving as the landing page for the portfolio
 */
@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    RouterLink,
    MatButtonModule,
    MatCardModule,
    MatIconModule
  ],
  template: `
    <div class="home">
      <section class="home__hero">
        <h1 class="home__title">Steven Salmons</h1>
        <p class="home__subtitle">Software Engineer with expertise in Python, JavaScript, and AWS</p>
        
        <div class="home__actions">
          <a mat-raised-button color="primary" routerLink="/about">
            <mat-icon>person</mat-icon>
            About Me
          </a>
          <a mat-raised-button color="accent" routerLink="/portfolio">
            <mat-icon>work</mat-icon>
            View My Work
          </a>
        </div>
      </section>
      
      <section class="home__featured">
        <h2 class="home__section-title">Featured Projects</h2>
        
        <div class="home__cards">
          <mat-card class="home__card">
            <mat-card-header>
              <mat-card-title>Project One</mat-card-title>
              <mat-card-subtitle>Web Application</mat-card-subtitle>
            </mat-card-header>
            <mat-card-content>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget felis eget urna ultrices accumsan.</p>
            </mat-card-content>
            <mat-card-actions>
              <a mat-button color="primary" routerLink="/portfolio/project-one">
                <mat-icon>visibility</mat-icon>
                View Details
              </a>
            </mat-card-actions>
          </mat-card>
          
          <mat-card class="home__card">
            <mat-card-header>
              <mat-card-title>Project Two</mat-card-title>
              <mat-card-subtitle>Mobile App</mat-card-subtitle>
            </mat-card-header>
            <mat-card-content>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget felis eget urna ultrices accumsan.</p>
            </mat-card-content>
            <mat-card-actions>
              <a mat-button color="primary" routerLink="/portfolio/project-two">
                <mat-icon>visibility</mat-icon>
                View Details
              </a>
            </mat-card-actions>
          </mat-card>
        </div>
      </section>
    </div>
  `,
  styles: `
    .home {
      max-width: 1200px;
      margin: 0 auto;
      padding: 2rem 1rem;
      
      &__hero {
        text-align: center;
        margin-bottom: 4rem;
        padding: 4rem 1rem;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 8px;
      }
      
      &__title {
        font-size: 3rem;
        margin-bottom: 1rem;
        color: #333;
      }
      
      &__subtitle {
        font-size: 1.5rem;
        margin-bottom: 2rem;
        color: #666;
      }
      
      &__actions {
        display: flex;
        gap: 1rem;
        justify-content: center;
        
        a {
          display: flex;
          align-items: center;
          
          mat-icon {
            margin-right: 0.5rem;
          }
        }
      }
      
      &__section-title {
        font-size: 2rem;
        margin-bottom: 2rem;
        text-align: center;
        color: #333;
      }
      
      &__cards {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 2rem;
      }
      
      &__card {
        height: 100%;
        display: flex;
        flex-direction: column;
        
        mat-card-content {
          flex-grow: 1;
        }
        
        mat-card-actions {
          display: flex;
          justify-content: flex-end;
        }
      }
      
      @media (max-width: 768px) {
        &__title {
          font-size: 2rem;
        }
        
        &__subtitle {
          font-size: 1.2rem;
        }
        
        &__cards {
          grid-template-columns: 1fr;
        }
      }
    }
  `
})
export class HomeComponent {} 