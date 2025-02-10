import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatChipsModule } from '@angular/material/chips';
import { MatIconModule } from '@angular/material/icon';
import { trigger, state, style, transition, animate } from '@angular/animations';
import { GithubService, GistFile, Repository } from '../../shared/services/github.service';

interface Project {
  id: string;
  title?: string;
  icon: string;
  subtitle?: string;
  repository?: Repository;
  gists: {
    description: string;
    id: string;
  }[];
  selectedGistContent?: GistFile[];
  isExpanded?: boolean;
}

@Component({
  selector: 'app-portfolio',
  standalone: true,
  imports: [
    CommonModule,
    MatChipsModule,
    MatIconModule
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
  readmeIcon = '📄';
  projects: Project[] = [
    {
      id: 'ngfast-reports',

      icon: '🚀',
      gists: [
        { description: 'Performance Optimizations', id: 'gist1id' },
        { description: 'Build Configuration', id: 'gist2id' }
      ]
    },
    {
      id: '3m-pipeline',
      icon: '📊',
      gists: [
        { description: 'Chart Components', id: 'gist3id' },
        { description: 'Real-time Updates', id: 'gist4id' }
      ]
    }
  ];

  constructor(private githubService: GithubService) {}

  ngOnInit() {
    // Load repository data for each project
    this.projects.forEach(project => {
      this.githubService.getRepository(project.id).subscribe(repo => {
        project.repository = repo;
        project.title = repo.name;
        project.subtitle = repo.description;
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
      console.log('No languages for project:', project.id);
      return [];
    }
    return Object.keys(project.repository.languages);
  }

  /**
   * Get color for language tag
   */
  getLanguageColor(language: string): string {
    console.log('Getting color for language:', language);
    // Common language colors, can be expanded
    const colors: { [key: string]: string } = {
      TypeScript: '#3178c6',
      JavaScript: '#f1e05a',
      HTML: '#e34c26',
      CSS: '#563d7c',
      SCSS: '#c6538c',
      Python: '#3572A5',
      Java: '#b07219',
      // Add more as needed
    };
    return colors[language] || '#6e7681';
  }

  /**
   * Get the updated date string from repository
   */
  getUpdatedAt(project: Project): string {
    if (!project.repository?.updated_at) return '';
    return project.repository.updated_at;
  }
} 