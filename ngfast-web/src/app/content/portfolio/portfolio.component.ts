import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatChipsModule } from '@angular/material/chips';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatDividerModule } from '@angular/material/divider';
import { trigger, state, style, transition, animate } from '@angular/animations';
import { GithubService } from '../../shared/services/github.service';
import { Project } from '../../shared/models/github.types';
import { PROJECTS } from '../../shared/config/projects.config';

@Component({
  selector: 'app-portfolio',
  standalone: true,
  imports: [
    CommonModule,
    MatChipsModule,
    MatIconModule,
    MatCardModule,
    MatDividerModule
  ],
  templateUrl: './portfolio.component.html',
  styleUrls: ['./portfolio.component.scss'],
  animations: [
    trigger('expandCollapse', [
      transition(':enter', [
        style({ height: '0', opacity: 0 }),
        animate('200ms ease-out', style({ height: '*', opacity: 1 }))
      ]),
      transition(':leave', [
        animate('200ms ease-in', style({ height: '0', opacity: 0 }))
      ])
    ])
  ]
})
export class PortfolioComponent implements OnInit {
  projects: Project[] = PROJECTS;

  constructor(private githubService: GithubService) {}

  ngOnInit() {
    // Load repository data for each project
    this.projects.forEach(project => {
      this.githubService.getProject(project.id).subscribe(updatedProject => {
        // Merge existing gists with updated project data
        Object.assign(project, updatedProject, { gists: project.gists });
      });
    });
  }

  /**
   * Gets GitHub URL for a project
   */
  getGithubUrl(project: Project): string | undefined {
    return project.repository?.html_url;
  }

  /**
   * Toggles project expansion state
   */
  toggleProject(project: Project) {
    project.isExpanded = !project.isExpanded;
  }

  /**
   * Loads gist content for a specific project
   */
  loadGist(project: Project, gistId: string) {
    this.githubService.getGistContent(gistId).subscribe(files => {
      project.selectedGistContent = files;
    });
  }

  /**
   * Get languages for a project
   */
  getLanguages(project: Project): string[] {
    if (!project.repository?.languages) {
      return [];
    }
    return Object.keys(project.repository.languages);
  }

  /**
   * Get color for language tag
   */
  getLanguageColor(language: string): string {
    // Common language colors, can be expanded
    const colors: { [key: string]: string } = {
      typescript: '#3178C6',
      javascript: '#F7DF1E',
      html: '#E34F26',
      css: '#1572B6',
      scss: '#CC6699',
      python: '#3572A5',
      'jupyter notebook': '#F37626',
      // Add more as needed
    };
    return colors[language.toLowerCase()] || '#6e7681';
  }

  /**
   * Get the updated date string from repository
   */
  getUpdatedAt(project: Project): string {
    if (!project.repository?.updated_at) return '';
    return project.repository.updated_at;
  }
} 