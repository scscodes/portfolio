import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map, forkJoin, switchMap } from 'rxjs';
import {
  Repository,
  GistFile,
  Project,
  GithubConfig
} from '../models/github.types';
import { PROJECTS } from '../config/projects.config';

@Injectable({
  providedIn: 'root'
})
export class GithubService {
  private readonly config: GithubConfig = {
    username: 'scscodes',
    profileUrl: 'https://github.com/scscodes',
    repositories: PROJECTS.map(p => p.id)
  };

  private readonly apiBase = 'https://api.github.com';
  private cachedRepos: Map<string, Repository> = new Map();
  private cachedProjects: Map<string, Project> = new Map();

  constructor(private http: HttpClient) {}

  /**
   * Get GitHub configuration
   */
  getConfig(): GithubConfig {
    return this.config;
  }

  /**
   * Fetch repository details from GitHub API
   */
  getRepository(repoId: string): Observable<Repository> {
    const cached = this.cachedRepos.get(repoId);
    if (cached) {
      return new Observable(observer => {
        observer.next(cached);
        observer.complete();
      });
    }

    const url = `${this.apiBase}/repos/${this.config.username}/${repoId}`;
    return this.http.get<Repository>(url).pipe(
      switchMap(repo => {
        return this.http.get<{ [key: string]: number }>(repo.languages_url).pipe(
          map(languages => {
            repo.languages = languages;
            this.cachedRepos.set(repoId, repo);
            return repo;
          })
        );
      })
    );
  }

  /**
   * Get or create a project by ID
   */
  getProject(projectId: string): Observable<Project> {
    const cached = this.cachedProjects.get(projectId);
    if (cached) {
      return new Observable(observer => {
        observer.next(cached);
        observer.complete();
      });
    }

    return this.getRepository(projectId).pipe(
      map(repo => {
        const baseProject = PROJECTS.find(p => p.id === projectId);
        if (!baseProject) {
          throw new Error(`Project configuration not found for ID: ${projectId}`);
        }

        const project: Project = {
          ...baseProject,
          title: repo.name,
          subtitle: repo.description,
          repository: repo,
          isExpanded: false
        };
        
        this.cachedProjects.set(projectId, project);
        return project;
      })
    );
  }

  /**
   * Fetch all configured repositories
   */
  getAllRepositories(): Observable<Repository[]> {
    const repoRequests = this.config.repositories.map(repoId => 
      this.getRepository(repoId)
    );
    return forkJoin(repoRequests);
  }

  /**
   * Get all projects with repository data
   */
  getAllProjects(): Observable<Project[]> {
    const projectRequests = this.config.repositories.map(repoId => 
      this.getProject(repoId)
    );
    return forkJoin(projectRequests);
  }

  /**
   * Get repository URL by key
   */
  getRepositoryUrl(repoId: string): Observable<string | undefined> {
    return this.getRepository(repoId).pipe(
      map(repo => repo.html_url)
    );
  }

  /**
   * Fetch gist content by ID
   */
  getGistContent(gistId: string): Observable<GistFile[]> {
    const gistUrl = `${this.apiBase}/gists/${gistId}`;
    
    return this.http.get<any>(gistUrl).pipe(
      map(response => {
        const files: GistFile[] = [];
        for (const filename in response.files) {
          files.push({
            filename,
            content: response.files[filename].content
          });
        }
        return files;
      })
    );
  }
} 