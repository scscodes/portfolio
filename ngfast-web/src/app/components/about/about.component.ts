import { Component } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { MatTabsModule } from '@angular/material/tabs';
import { MatIconModule } from '@angular/material/icon';
import { MatDividerModule } from '@angular/material/divider';
import { MatListModule } from '@angular/material/list';
import { MatChipsModule } from '@angular/material/chips';
import { MatButtonModule } from '@angular/material/button';
import { CommonModule } from '@angular/common';

/**
 * About component displaying resume and personal information
 */
@Component({
  selector: 'app-about',
  standalone: true,
  imports: [
    CommonModule,
    MatCardModule,
    MatTabsModule,
    MatIconModule,
    MatDividerModule,
    MatListModule,
    MatChipsModule,
    MatButtonModule
  ],
  template: `
    <div class="about">
      <h1 class="about__title">About Me</h1>
      
      <div class="about__content">
        <mat-card class="about__profile">
          <div class="about__profile-header">
            <div class="about__avatar">
              <!-- Placeholder for profile image -->
              <mat-icon class="about__avatar-icon">account_circle</mat-icon>
            </div>
            <div class="about__profile-info">
              <h2 class="about__name">Steven Salmons</h2>
              <p class="about__position">Software Engineer</p>
              <div class="about__contact">
                <div class="about__contact-item">
                  <mat-icon>email</mat-icon>
                  <span>stevencsalmons&#64;gmail.com</span>
                </div>
                <div class="about__contact-item">
                  <mat-icon>location_on</mat-icon>
                  <span>Columbus, Ohio</span>
                </div>
              </div>
            </div>
          </div>
          
          <mat-divider></mat-divider>
          
          <div class="about__bio">
            <h3>Summary</h3>
            <p>
              Experienced Software Engineer with over 10 years of expertise in software development, automation, and systems engineering. Proven track record in delivering scalable solutions, optimizing processes, and leading teams in hybrid cloud environments. Skilled in Python, JavaScript, and AWS with a focus on automation, data integration, and CI/CD pipelines.
            </p>
          </div>
          
          <div class="about__social">
            <a mat-icon-button href="https://github.com/scscodes" target="_blank" aria-label="GitHub" class="about__social-github">
              <img src="assets/images/GitHub_Invertocat_Dark.png" alt="GitHub" class="about__social-icon">
            </a>
            <a mat-icon-button href="https://linkedin.com/in/ssalmons" target="_blank" aria-label="LinkedIn" class="about__social-linkedin">
              <img src="assets/images/LI-In-Bug.png" alt="LinkedIn" class="about__social-icon">
            </a>
          </div>
        </mat-card>
        
        <mat-card class="about__resume">
          <mat-tab-group animationDuration="0ms">
            <mat-tab label="Experience">
              <div class="about__section">
                <div class="about__experience">
                  <div class="about__experience-header">
                    <div class="about__experience-logo">
                      <mat-icon class="about__company-icon">business</mat-icon>
                    </div>
                    <div>
                      <h3 class="about__experience-title">Software Engineer III</h3>
                      <p class="about__experience-company">JPMorgan Chase</p>
                      <p class="about__experience-period">06/2020 - Present</p>
                    </div>
                  </div>
                  <ul class="about__experience-duties">
                    <li>Led Agile feature teams of 3-10 engineers, managing lifecycles, priorities, and deliverables.</li>
                    <li>Streamlined self-service compliance tools, consolidating domain and vendor data into customized reports, reducing overhead by 95%.</li>
                    <li>Developed global automations, returning up to 70% of resource hours by case.</li>
                    <li>Design, develop and deploy in hybrid cloud environment, private/public cloud databases, APIs and web interfaces with Python and Angular.</li>
                    <li>Tenured mentor, formally recognized by leadership, helping 8 engineers develop technical proficiency and build professional skills.</li>
                  </ul>
                </div>
                
                <mat-divider></mat-divider>
                
                <div class="about__experience">
                  <div class="about__experience-header">
                    <div class="about__experience-logo">
                      <mat-icon class="about__company-icon">business</mat-icon>
                    </div>
                    <div>
                      <h3 class="about__experience-title">Systems Engineer</h3>
                      <p class="about__experience-company">Designer Brands Inc.</p>
                      <p class="about__experience-period">01/2017 - 06/2020</p>
                    </div>
                  </div>
                  <ul class="about__experience-duties">
                    <li>Patching automations with PowerShell reduced process time by 80%.</li>
                    <li>Created audit and compliance reports, improving delivery times by 90%.</li>
                  </ul>
                </div>
                
                <mat-divider></mat-divider>
                
                <div class="about__experience">
                  <div class="about__experience-header">
                    <div class="about__experience-logo">
                      <mat-icon class="about__company-icon">business</mat-icon>
                    </div>
                    <div>
                      <h3 class="about__experience-title">Systems Engineer</h3>
                      <p class="about__experience-company">JBT Inc.</p>
                      <p class="about__experience-period">02/2015 - 12/2016</p>
                    </div>
                  </div>
                  <ul class="about__experience-duties">
                    <li>Virtualized legacy server racks, reducing physical footprint by 45%.</li>
                  </ul>
                </div>
                
                <mat-divider></mat-divider>
                
                <div class="about__experience">
                  <div class="about__experience-header">
                    <div class="about__experience-logo">
                      <mat-icon class="about__company-icon">military_tech</mat-icon>
                    </div>
                    <div>
                      <h3 class="about__experience-title">Systems Administrator</h3>
                      <p class="about__experience-company">U.S. Navy</p>
                      <p class="about__experience-period">12/2010 - 12/2014</p>
                    </div>
                  </div>
                  <ul class="about__experience-duties">
                    <li>Team lead, achieving +90% score during red team assessment.</li>
                  </ul>
                </div>
              </div>
            </mat-tab>
            
            <mat-tab label="Education">
              <div class="about__section">
                <div class="about__education">
                  <div class="about__education-header">
                    <div class="about__education-logo">
                      <mat-icon class="about__education-icon">school</mat-icon>
                    </div>
                    <div>
                      <h3 class="about__education-degree">Data Science Certificate</h3>
                      <p class="about__education-school">Chegg University</p>
                      <p class="about__education-period">01/2025</p>
                    </div>
                  </div>
                </div>
                
                <mat-divider></mat-divider>
                
                <div class="about__education">
                  <div class="about__education-header">
                    <div class="about__education-logo">
                      <mat-icon class="about__education-icon">school</mat-icon>
                    </div>
                    <div>
                      <h3 class="about__education-degree">B.A. Business Technology, Cum Laude</h3>
                      <p class="about__education-school">University of Toledo</p>
                      <p class="about__education-period">12/2020</p>
                    </div>
                  </div>
                </div>
              </div>
            </mat-tab>
            
            <mat-tab label="Skills">
              <div class="about__section">
                <h3>Programming</h3>
                <div class="about__skills">
                  <mat-chip-set>
                    <mat-chip>Python</mat-chip>
                    <mat-chip>Flask</mat-chip>
                    <mat-chip>JavaScript</mat-chip>
                    <mat-chip>TypeScript</mat-chip>
                    <mat-chip>Angular</mat-chip>
                    <mat-chip>React</mat-chip>
                    <mat-chip>Node.js</mat-chip>
                  </mat-chip-set>
                </div>
                
                <h3>Data Science</h3>
                <div class="about__skills">
                  <mat-chip-set>
                    <mat-chip>Regression</mat-chip>
                    <mat-chip>Classifiers</mat-chip>
                    <mat-chip>Clustering</mat-chip>
                    <mat-chip>Supervised Learning</mat-chip>
                    <mat-chip>Unsupervised Learning</mat-chip>
                  </mat-chip-set>
                </div>
                
                <h3>Databases</h3>
                <div class="about__skills">
                  <mat-chip-set>
                    <mat-chip>MySQL</mat-chip>
                    <mat-chip>Oracle</mat-chip>
                    <mat-chip>PostgreSQL</mat-chip>
                    <mat-chip>AWS Aurora</mat-chip>
                  </mat-chip-set>
                </div>
                
                <h3>DevOps</h3>
                <div class="about__skills">
                  <mat-chip-set>
                    <mat-chip>Azure DevOps</mat-chip>
                    <mat-chip>Git</mat-chip>
                    <mat-chip>Jenkins</mat-chip>
                    <mat-chip>Cloud Foundry</mat-chip>
                    <mat-chip>Docker</mat-chip>
                    <mat-chip>AWS</mat-chip>
                  </mat-chip-set>
                </div>
                
                <h3>Testing</h3>
                <div class="about__skills">
                  <mat-chip-set>
                    <mat-chip>Jasmine</mat-chip>
                    <mat-chip>Karma</mat-chip>
                    <mat-chip>Pytest</mat-chip>
                    <mat-chip>SonarQube</mat-chip>
                  </mat-chip-set>
                </div>
                
                <h3>Agile</h3>
                <div class="about__skills">
                  <mat-chip-set>
                    <mat-chip>Jira</mat-chip>
                    <mat-chip>Confluence</mat-chip>
                    <mat-chip>Kanban</mat-chip>
                  </mat-chip-set>
                </div>
              </div>
            </mat-tab>
          </mat-tab-group>
        </mat-card>
      </div>
    </div>
  `,
  styles: `
    .about {
      max-width: 1200px;
      margin: 0 auto;
      padding: 2rem 1rem;
      
      &__title {
        font-size: 2.5rem;
        margin-bottom: 2rem;
        color: #333;
        text-align: center;
      }
      
      &__content {
        display: grid;
        grid-template-columns: 1fr 2fr;
        gap: 2rem;
        
        @media (max-width: 992px) {
          grid-template-columns: 1fr;
        }
      }
      
      &__profile {
        padding: 1.5rem;
        
        &-header {
          display: flex;
          margin-bottom: 1.5rem;
          
          @media (max-width: 576px) {
            flex-direction: column;
            align-items: center;
            text-align: center;
          }
        }
        
        &-info {
          margin-left: 1.5rem;
          
          @media (max-width: 576px) {
            margin-left: 0;
            margin-top: 1rem;
          }
        }
      }
      
      &__avatar {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        background-color: #e0e0e0;
        display: flex;
        justify-content: center;
        align-items: center;
        
        &-icon {
          font-size: 64px;
          width: 64px;
          height: 64px;
        }
      }
      
      &__name {
        font-size: 1.8rem;
        margin: 0 0 0.5rem;
      }
      
      &__position {
        font-size: 1.2rem;
        color: #666;
        margin: 0 0 1rem;
      }
      
      &__contact {
        &-item {
          display: flex;
          align-items: center;
          margin-bottom: 0.5rem;
          
          mat-icon {
            margin-right: 0.5rem;
            font-size: 18px;
            width: 18px;
            height: 18px;
          }
        }
      }
      
      &__bio {
        margin: 1.5rem 0;
        
        h3 {
          margin-bottom: 0.5rem;
        }
        
        p {
          line-height: 1.6;
        }
      }
      
      &__social {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 1.5rem;
        
        &-icon {
          width: 24px;
          height: 24px;
        }
        
        &-github, &-linkedin {
          display: flex;
          align-items: center;
          justify-content: center;
        }
      }
      
      &__resume {
        padding: 0;
        
        ::ng-deep .mat-mdc-tab-body-wrapper {
          padding: 1.5rem;
        }
      }
      
      &__section {
        padding: 1rem 0;
      }
      
      &__experience, &__education {
        margin-bottom: 1.5rem;
        
        &-header {
          display: flex;
          align-items: center;
          margin-bottom: 1rem;
        }
        
        &-logo {
          width: 50px;
          height: 50px;
          margin-right: 1rem;
          display: flex;
          align-items: center;
          justify-content: center;
        }
        
        &-title, &-degree {
          font-size: 1.3rem;
          margin: 0 0 0.5rem;
        }
        
        &-company, &-school {
          font-weight: 500;
          margin: 0 0 0.25rem;
        }
        
        &-period {
          color: #666;
          font-style: italic;
          margin: 0 0 0.5rem;
        }
        
        &-duties {
          padding-left: 1.5rem;
          
          li {
            margin-bottom: 0.25rem;
          }
        }
      }
      
      &__company-icon, &__education-icon {
        font-size: 36px;
        width: 36px;
        height: 36px;
        color: #555;
      }
      
      &__education {
        &-header {
          display: flex;
          align-items: center;
          margin-bottom: 1rem;
        }
        
        &-logo {
          width: 50px;
          height: 50px;
          margin-right: 1rem;
          display: flex;
          align-items: center;
          justify-content: center;
        }
      }
      
      &__skills {
        margin-bottom: 1.5rem;
        
        mat-chip-set {
          display: flex;
          flex-wrap: wrap;
          gap: 0.5rem;
        }
      }
      
      mat-divider {
        margin: 1.5rem 0;
      }
    }
  `
})
export class AboutComponent {} 