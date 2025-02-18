import { Project } from '../github/github.types';

/**
 * Project configuration data
 * Defines initial project structure and gist mappings
 */
export const PROJECTS: Project[] = [
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