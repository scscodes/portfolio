import { Pipe, PipeTransform } from '@angular/core';

/**
 * Pipe to filter projects by type
 * Usage: *ngFor="let project of projects | filterProjects:'Web App'"
 */
@Pipe({
  name: 'filterProjects',
  standalone: true
})
export class FilterProjectsPipe implements PipeTransform {
  transform(projects: any[], type: string): any[] {
    if (!projects || !type) {
      return projects;
    }
    
    return projects.filter(project => project.type === type);
  }
} 