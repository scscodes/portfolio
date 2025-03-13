import { Injectable } from '@angular/core';
import { Project } from '../models/project.model';

/**
 * Service for managing project data
 */
@Injectable({
  providedIn: 'root'
})
export class ProjectService {
  /**
   * Get all projects
   * @returns Array of projects
   */
  getProjects(): Project[] {
    return [
      {
        id: 'compliance-automation',
        title: 'Compliance Automation Platform',
        type: 'Web App',
        description: 'A self-service compliance tool that consolidates domain and vendor data into customized reports, reducing overhead by 95%.',
        technologies: ['Python', 'Flask', 'Angular', 'AWS', 'PostgreSQL'],
        github: 'https://github.com/scscodes/compliance-automation',
        demo: null,
        image: 'assets/images/project1.jpg'
      },
      {
        id: 'resource-optimization',
        title: 'Resource Optimization System',
        type: 'Web App',
        description: 'Global automation system that returns up to 70% of resource hours by case through intelligent workflow management and task automation.',
        technologies: ['Python', 'React', 'Node.js', 'AWS Aurora', 'Docker'],
        github: 'https://github.com/scscodes/resource-optimization',
        demo: null,
        image: 'assets/images/project2.jpg'
      },
      {
        id: 'hybrid-cloud-api',
        title: 'Hybrid Cloud API Gateway',
        type: 'Web App',
        description: 'API gateway designed for hybrid cloud environments, connecting private and public cloud databases with secure interfaces.',
        technologies: ['Python', 'TypeScript', 'Angular', 'AWS', 'Cloud Foundry'],
        github: 'https://github.com/scscodes/hybrid-cloud-api',
        demo: null,
        image: 'assets/images/project3.jpg'
      },
      {
        id: 'patching-automation',
        title: 'PowerShell Patching Automation',
        type: 'DevOps Tool',
        description: 'Automated patching system using PowerShell that reduced process time by 80% while improving security compliance.',
        technologies: ['PowerShell', 'Windows Server', 'Azure DevOps'],
        github: 'https://github.com/scscodes/patching-automation',
        demo: null,
        image: 'assets/images/project4.jpg'
      },
      {
        id: 'audit-reporting',
        title: 'Audit & Compliance Reporting',
        type: 'DevOps Tool',
        description: 'Automated audit and compliance reporting system that improved delivery times by 90% while ensuring regulatory compliance.',
        technologies: ['Python', 'SQL', 'Jenkins', 'Docker'],
        github: 'https://github.com/scscodes/audit-reporting',
        demo: null,
        image: 'assets/images/project5.jpg'
      },
      {
        id: 'server-virtualization',
        title: 'Server Virtualization Project',
        type: 'Infrastructure',
        description: 'Virtualization of legacy server racks, reducing physical footprint by 45% while improving performance and reliability.',
        technologies: ['VMware', 'Windows Server', 'Linux', 'PowerShell'],
        github: 'https://github.com/scscodes/server-virtualization',
        demo: null,
        image: 'assets/images/project6.jpg'
      }
    ];
  }

  /**
   * Get a project by ID
   * @param id Project ID
   * @returns Project or undefined if not found
   */
  getProjectById(id: string): Project | undefined {
    return this.getProjects().find(project => project.id === id);
  }

  /**
   * Get projects by type
   * @param type Project type
   * @returns Array of projects of the specified type
   */
  getProjectsByType(type: string): Project[] {
    return this.getProjects().filter(project => project.type === type);
  }
} 