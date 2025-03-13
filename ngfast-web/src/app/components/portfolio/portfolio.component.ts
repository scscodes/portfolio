import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatChipsModule } from '@angular/material/chips';
import { MatTabsModule } from '@angular/material/tabs';
import { MatDividerModule } from '@angular/material/divider';
import { FilterProjectsPipe } from '../../shared/pipes/filter-projects.pipe';
import { ProjectService } from '../../shared/services/project.service';
import { Project } from '../../shared/models/project.model';

/**
 * Portfolio component to showcase projects
 */
@Component({
  selector: 'app-portfolio',
  standalone: true,
  imports: [
    CommonModule,
    RouterLink,
    MatCardModule,
    MatButtonModule,
    MatIconModule,
    MatChipsModule,
    MatTabsModule,
    MatDividerModule,
    FilterProjectsPipe
  ],
  template: `
    <div class="portfolio">
      <h1 class="portfolio__title">My Portfolio</h1>
      <p class="portfolio__subtitle">A collection of my recent projects</p>
      
      <mat-tab-group animationDuration="0ms" class="portfolio__tabs">
        <mat-tab label="All Projects">
          <div class="portfolio__grid">
            <mat-card class="portfolio__card" *ngFor="let project of projects">
              <div class="portfolio__card-image">
                <!-- Placeholder for project image -->
                <div class="portfolio__placeholder">
                  <mat-icon>code</mat-icon>
                </div>
              </div>
              
              <mat-card-content>
                <h2 class="portfolio__card-title">{{ project.title }}</h2>
                <p class="portfolio__card-description">{{ project.description }}</p>
                
                <div class="portfolio__card-tech">
                  <mat-chip-set>
                    <mat-chip *ngFor="let tech of project.technologies">{{ tech }}</mat-chip>
                  </mat-chip-set>
                </div>
              </mat-card-content>
              
              <mat-card-actions class="portfolio__card-actions">
                <a mat-button color="primary" [routerLink]="['/portfolio', project.id]">
                  <mat-icon>visibility</mat-icon>
                  View Details
                </a>
                <a mat-button *ngIf="project.github" [href]="project.github" target="_blank">
                  <mat-icon>code</mat-icon>
                  GitHub
                </a>
                <a mat-button *ngIf="project.demo" [href]="project.demo" target="_blank">
                  <mat-icon>launch</mat-icon>
                  Live Demo
                </a>
              </mat-card-actions>
            </mat-card>
          </div>
        </mat-tab>
        
        <mat-tab label="Web Apps">
          <div class="portfolio__grid">
            <mat-card class="portfolio__card" *ngFor="let project of projects | filterProjects:'Web App'">
              <!-- Same content as above, but filtered -->
              <div class="portfolio__card-image">
                <div class="portfolio__placeholder">
                  <mat-icon>code</mat-icon>
                </div>
              </div>
              
              <mat-card-content>
                <h2 class="portfolio__card-title">{{ project.title }}</h2>
                <p class="portfolio__card-description">{{ project.description }}</p>
                
                <div class="portfolio__card-tech">
                  <mat-chip-set>
                    <mat-chip *ngFor="let tech of project.technologies">{{ tech }}</mat-chip>
                  </mat-chip-set>
                </div>
              </mat-card-content>
              
              <mat-card-actions class="portfolio__card-actions">
                <a mat-button color="primary" [routerLink]="['/portfolio', project.id]">
                  <mat-icon>visibility</mat-icon>
                  View Details
                </a>
                <a mat-button *ngIf="project.github" [href]="project.github" target="_blank">
                  <mat-icon>code</mat-icon>
                  GitHub
                </a>
                <a mat-button *ngIf="project.demo" [href]="project.demo" target="_blank">
                  <mat-icon>launch</mat-icon>
                  Live Demo
                </a>
              </mat-card-actions>
            </mat-card>
          </div>
        </mat-tab>
        
        <mat-tab label="DevOps Tools">
          <div class="portfolio__grid">
            <mat-card class="portfolio__card" *ngFor="let project of projects | filterProjects:'DevOps Tool'">
              <!-- Same content as above, but filtered -->
              <div class="portfolio__card-image">
                <div class="portfolio__placeholder">
                  <mat-icon>code</mat-icon>
                </div>
              </div>
              
              <mat-card-content>
                <h2 class="portfolio__card-title">{{ project.title }}</h2>
                <p class="portfolio__card-description">{{ project.description }}</p>
                
                <div class="portfolio__card-tech">
                  <mat-chip-set>
                    <mat-chip *ngFor="let tech of project.technologies">{{ tech }}</mat-chip>
                  </mat-chip-set>
                </div>
              </mat-card-content>
              
              <mat-card-actions class="portfolio__card-actions">
                <a mat-button color="primary" [routerLink]="['/portfolio', project.id]">
                  <mat-icon>visibility</mat-icon>
                  View Details
                </a>
                <a mat-button *ngIf="project.github" [href]="project.github" target="_blank">
                  <mat-icon>code</mat-icon>
                  GitHub
                </a>
                <a mat-button *ngIf="project.demo" [href]="project.demo" target="_blank">
                  <mat-icon>launch</mat-icon>
                  Live Demo
                </a>
              </mat-card-actions>
            </mat-card>
          </div>
        </mat-tab>
        
        <mat-tab label="Infrastructure">
          <div class="portfolio__grid">
            <mat-card class="portfolio__card" *ngFor="let project of projects | filterProjects:'Infrastructure'">
              <!-- Same content as above, but filtered -->
              <div class="portfolio__card-image">
                <div class="portfolio__placeholder">
                  <mat-icon>code</mat-icon>
                </div>
              </div>
              
              <mat-card-content>
                <h2 class="portfolio__card-title">{{ project.title }}</h2>
                <p class="portfolio__card-description">{{ project.description }}</p>
                
                <div class="portfolio__card-tech">
                  <mat-chip-set>
                    <mat-chip *ngFor="let tech of project.technologies">{{ tech }}</mat-chip>
                  </mat-chip-set>
                </div>
              </mat-card-content>
              
              <mat-card-actions class="portfolio__card-actions">
                <a mat-button color="primary" [routerLink]="['/portfolio', project.id]">
                  <mat-icon>visibility</mat-icon>
                  View Details
                </a>
                <a mat-button *ngIf="project.github" [href]="project.github" target="_blank">
                  <mat-icon>code</mat-icon>
                  GitHub
                </a>
                <a mat-button *ngIf="project.demo" [href]="project.demo" target="_blank">
                  <mat-icon>launch</mat-icon>
                  Live Demo
                </a>
              </mat-card-actions>
            </mat-card>
          </div>
        </mat-tab>
      </mat-tab-group>
    </div>
  `,
  styles: `
    .portfolio {
      max-width: 1200px;
      margin: 0 auto;
      padding: 2rem 1rem;
      
      &__title {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        color: #333;
        text-align: center;
      }
      
      &__subtitle {
        font-size: 1.2rem;
        margin-bottom: 2rem;
        color: #666;
        text-align: center;
      }
      
      &__tabs {
        margin-bottom: 2rem;
      }
      
      &__grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
        gap: 2rem;
        padding: 2rem 0;
        
        @media (max-width: 768px) {
          grid-template-columns: 1fr;
        }
      }
      
      &__card {
        height: 100%;
        display: flex;
        flex-direction: column;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        
        &:hover {
          transform: translateY(-5px);
          box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }
        
        &-image {
          height: 200px;
          overflow: hidden;
        }
        
        &-title {
          font-size: 1.5rem;
          margin: 1rem 0 0.5rem;
        }
        
        &-description {
          color: #666;
          margin-bottom: 1rem;
          flex-grow: 1;
        }
        
        &-tech {
          margin: 1rem 0;
        }
        
        &-actions {
          display: flex;
          flex-wrap: wrap;
          gap: 0.5rem;
          padding: 0.5rem 1rem 1rem;
          
          a {
            display: flex;
            align-items: center;
            
            mat-icon {
              margin-right: 0.25rem;
            }
          }
        }
      }
      
      &__placeholder {
        height: 100%;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        display: flex;
        justify-content: center;
        align-items: center;
        
        mat-icon {
          font-size: 48px;
          width: 48px;
          height: 48px;
          color: #555;
        }
      }
    }
  `
})
export class PortfolioComponent implements OnInit {
  /**
   * Array of projects
   */
  projects: Project[] = [];
  
  /**
   * Constructor
   * @param projectService Project service for fetching project data
   */
  constructor(private projectService: ProjectService) {}
  
  /**
   * Initialize component
   */
  ngOnInit(): void {
    this.projects = this.projectService.getProjects();
  }
} 