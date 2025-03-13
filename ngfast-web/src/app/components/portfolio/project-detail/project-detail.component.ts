import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatChipsModule } from '@angular/material/chips';
import { MatDividerModule } from '@angular/material/divider';
import { MatTabsModule } from '@angular/material/tabs';
import { ProjectService } from '../../../shared/services/project.service';
import { Project } from '../../../shared/models/project.model';

/**
 * Project detail component to display detailed information about a project
 */
@Component({
  selector: 'app-project-detail',
  standalone: true,
  imports: [
    CommonModule,
    RouterLink,
    MatCardModule,
    MatButtonModule,
    MatIconModule,
    MatChipsModule,
    MatDividerModule,
    MatTabsModule
  ],
  template: `
    <div class="project-detail" *ngIf="project">
      <div class="project-detail__header">
        <a mat-button routerLink="/portfolio" class="project-detail__back">
          <mat-icon>arrow_back</mat-icon>
          Back to Portfolio
        </a>
        <h1 class="project-detail__title">{{ project.title }}</h1>
        <p class="project-detail__type">{{ project.type }}</p>
      </div>
      
      <div class="project-detail__content">
        <div class="project-detail__image">
          <!-- Placeholder for project image -->
          <div class="project-detail__placeholder">
            <mat-icon>code</mat-icon>
          </div>
        </div>
        
        <div class="project-detail__info">
          <mat-card>
            <mat-card-content>
              <h2>Project Overview</h2>
              <p class="project-detail__description">{{ project.description }}</p>
              
              <mat-divider></mat-divider>
              
              <h2>Technologies Used</h2>
              <div class="project-detail__technologies">
                <mat-chip-set>
                  <mat-chip *ngFor="let tech of project.technologies">{{ tech }}</mat-chip>
                </mat-chip-set>
              </div>
              
              <mat-divider></mat-divider>
              
              <h2>Project Details</h2>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget felis eget urna ultrices accumsan. 
                Vivamus auctor, nisl eget ultricies lacinia, nisl nisl aliquam nisl, eget aliquam nisl nisl eget nisl.
              </p>
              <p>
                Vivamus auctor, nisl eget ultricies lacinia, nisl nisl aliquam nisl, eget aliquam nisl nisl eget nisl.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget felis eget urna ultrices accumsan.
              </p>
              
              <mat-divider></mat-divider>
              
              <h2>Features</h2>
              <ul class="project-detail__features">
                <li>Feature one with detailed explanation</li>
                <li>Feature two with implementation details</li>
                <li>Feature three showcasing technical expertise</li>
                <li>Feature four demonstrating problem-solving</li>
              </ul>
              
              <div class="project-detail__actions">
                <a mat-raised-button color="primary" *ngIf="project.github" [href]="project.github" target="_blank">
                  <mat-icon>code</mat-icon>
                  View on GitHub
                </a>
                <a mat-raised-button color="accent" *ngIf="project.demo" [href]="project.demo" target="_blank">
                  <mat-icon>launch</mat-icon>
                  Live Demo
                </a>
              </div>
            </mat-card-content>
          </mat-card>
        </div>
      </div>
      
      <mat-card class="project-detail__additional">
        <mat-tab-group animationDuration="0ms">
          <mat-tab label="Implementation">
            <div class="project-detail__tab-content">
              <h3>Implementation Details</h3>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget felis eget urna ultrices accumsan. 
                Vivamus auctor, nisl eget ultricies lacinia, nisl nisl aliquam nisl, eget aliquam nisl nisl eget nisl.
              </p>
              <p>
                Vivamus auctor, nisl eget ultricies lacinia, nisl nisl aliquam nisl, eget aliquam nisl nisl eget nisl.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget felis eget urna ultrices accumsan.
              </p>
              
              <h4>Architecture</h4>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget felis eget urna ultrices accumsan. 
                Vivamus auctor, nisl eget ultricies lacinia, nisl nisl aliquam nisl, eget aliquam nisl nisl eget nisl.
              </p>
            </div>
          </mat-tab>
          
          <mat-tab label="Challenges">
            <div class="project-detail__tab-content">
              <h3>Challenges & Solutions</h3>
              <div class="project-detail__challenge">
                <h4>Challenge 1: Performance Optimization</h4>
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget felis eget urna ultrices accumsan. 
                  Vivamus auctor, nisl eget ultricies lacinia, nisl nisl aliquam nisl.
                </p>
                <h5>Solution:</h5>
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget felis eget urna ultrices accumsan. 
                  Vivamus auctor, nisl eget ultricies lacinia, nisl nisl aliquam nisl.
                </p>
              </div>
              
              <div class="project-detail__challenge">
                <h4>Challenge 2: Data Management</h4>
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget felis eget urna ultrices accumsan. 
                  Vivamus auctor, nisl eget ultricies lacinia, nisl nisl aliquam nisl.
                </p>
                <h5>Solution:</h5>
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget felis eget urna ultrices accumsan. 
                  Vivamus auctor, nisl eget ultricies lacinia, nisl nisl aliquam nisl.
                </p>
              </div>
            </div>
          </mat-tab>
          
          <mat-tab label="Learnings">
            <div class="project-detail__tab-content">
              <h3>Key Learnings</h3>
              <ul>
                <li>
                  <strong>Technical Learning 1:</strong> Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                </li>
                <li>
                  <strong>Technical Learning 2:</strong> Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                </li>
                <li>
                  <strong>Process Learning:</strong> Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                </li>
                <li>
                  <strong>Collaboration Learning:</strong> Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                </li>
              </ul>
              
              <h4>Future Improvements</h4>
              <ul>
                <li>Potential enhancement one with explanation</li>
                <li>Potential enhancement two with explanation</li>
                <li>Potential enhancement three with explanation</li>
              </ul>
            </div>
          </mat-tab>
        </mat-tab-group>
      </mat-card>
    </div>
    
    <div class="project-detail__not-found" *ngIf="!project">
      <h2>Project Not Found</h2>
      <p>The project you're looking for doesn't exist or has been removed.</p>
      <a mat-raised-button color="primary" routerLink="/portfolio">
        <mat-icon>arrow_back</mat-icon>
        Back to Portfolio
      </a>
    </div>
  `,
  styles: `
    .project-detail {
      max-width: 1200px;
      margin: 0 auto;
      padding: 2rem 1rem;
      
      &__header {
        margin-bottom: 2rem;
        text-align: center;
      }
      
      &__back {
        position: absolute;
        left: 1rem;
        top: 5rem;
        display: flex;
        align-items: center;
        
        mat-icon {
          margin-right: 0.5rem;
        }
      }
      
      &__title {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        color: #333;
      }
      
      &__type {
        font-size: 1.2rem;
        color: #666;
      }
      
      &__content {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 2rem;
        margin-bottom: 2rem;
        
        @media (max-width: 992px) {
          grid-template-columns: 1fr;
        }
      }
      
      &__image {
        height: 400px;
        overflow: hidden;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      }
      
      &__placeholder {
        height: 100%;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        display: flex;
        justify-content: center;
        align-items: center;
        
        mat-icon {
          font-size: 96px;
          width: 96px;
          height: 96px;
          color: #555;
        }
      }
      
      &__description {
        font-size: 1.1rem;
        line-height: 1.6;
        margin-bottom: 1.5rem;
      }
      
      &__technologies {
        margin: 1rem 0 1.5rem;
      }
      
      &__features {
        padding-left: 1.5rem;
        margin-bottom: 1.5rem;
        
        li {
          margin-bottom: 0.5rem;
        }
      }
      
      &__actions {
        display: flex;
        gap: 1rem;
        margin-top: 2rem;
        
        a {
          display: flex;
          align-items: center;
          
          mat-icon {
            margin-right: 0.5rem;
          }
        }
      }
      
      &__additional {
        margin-bottom: 2rem;
      }
      
      &__tab-content {
        padding: 1.5rem;
        
        h3 {
          font-size: 1.5rem;
          margin-bottom: 1rem;
        }
        
        h4 {
          font-size: 1.2rem;
          margin: 1.5rem 0 0.5rem;
        }
        
        h5 {
          font-size: 1.1rem;
          margin: 1rem 0 0.5rem;
        }
        
        p {
          margin-bottom: 1rem;
          line-height: 1.6;
        }
        
        ul {
          padding-left: 1.5rem;
          
          li {
            margin-bottom: 0.5rem;
          }
        }
      }
      
      &__challenge {
        margin-bottom: 2rem;
      }
      
      &__not-found {
        max-width: 600px;
        margin: 4rem auto;
        text-align: center;
        
        h2 {
          font-size: 2rem;
          margin-bottom: 1rem;
        }
        
        p {
          margin-bottom: 2rem;
          color: #666;
        }
      }
      
      mat-divider {
        margin: 1.5rem 0;
      }
    }
  `
})
export class ProjectDetailComponent implements OnInit {
  /**
   * Current project
   */
  project?: Project;
  
  /**
   * Constructor
   * @param route Activated route for getting route parameters
   * @param router Router for navigation
   * @param projectService Project service for fetching project data
   */
  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private projectService: ProjectService
  ) {}
  
  /**
   * Initialize component
   */
  ngOnInit(): void {
    const projectId = this.route.snapshot.paramMap.get('id');
    
    if (projectId) {
      this.project = this.projectService.getProjectById(projectId);
      
      if (!this.project) {
        console.error(`Project with ID ${projectId} not found`);
      }
    }
  }
} 