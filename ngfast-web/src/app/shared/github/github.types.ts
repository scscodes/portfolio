/**
 * GitHub repository interface matching API response
 */
export interface Repository {
  id: string;
  name: string;
  description: string;
  html_url: string;
  languages_url: string;
  updated_at: string;
  languages?: { [key: string]: number };
}

/**
 * Gist file structure from GitHub API
 */
export interface GistFile {
  filename: string;
  content: string;
}

/**
 * Project configuration combining repository and gist data
 */
export interface Project {
  id: string;
  title?: string;
  icon?: string;
  subtitle?: string;
  repository?: Repository;
  gists: ProjectGist[];
  selectedGistContent?: GistFile[];
  isExpanded?: boolean;
}

/**
 * Gist reference structure
 */
export interface ProjectGist {
  description: string;
  id: string;
}

/**
 * GitHub service configuration
 */
export interface GithubConfig {
  username: string;
  profileUrl: string;
  repositories: string[];
} 