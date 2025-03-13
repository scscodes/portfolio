/**
 * Project model interface
 */
export interface Project {
  /** Unique identifier for the project */
  id: string;
  
  /** Project title */
  title: string;
  
  /** Project type (e.g., 'Web App', 'DevOps Tool') */
  type: string;
  
  /** Project description */
  description: string;
  
  /** Technologies used in the project */
  technologies: string[];
  
  /** GitHub repository URL (optional) */
  github?: string | null;
  
  /** Demo URL (optional) */
  demo?: string | null;
  
  /** Image path (optional) */
  image?: string;
} 