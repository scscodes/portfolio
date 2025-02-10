import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map, forkJoin, switchMap } from 'rxjs';

export interface GithubConfig {
  username: string;
  profileUrl: string;
  repositories: string[]; // Now just a list of repo IDs
}

export interface GistFile {
  filename: string;
  content: string;
}

export interface Repository {
  id: string;
  name: string;
  description: string;
  html_url: string;
  languages_url: string;
  updated_at: string;
  languages?: { [key: string]: number };  // Add languages property
}

@Injectable({
  providedIn: 'root'
})
export class GithubService {
  private readonly config: GithubConfig = {
    username: 'scscodes',
    profileUrl: 'https://github.com/scscodes',
    repositories: [
      'ngfast-reports',
      '3m-pipeline'
    ]
  };

  private readonly apiBase = 'https://api.github.com';
  private cachedRepos: Map<string, Repository> = new Map();

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
        // Fetch languages after getting repo data
        console.log(repo);
        return this.http.get<{ [key: string]: number }>(repo.languages_url).pipe(
          map(languages => {
            repo.languages = languages;
            console.log('Repository languages:', repo.name, languages);
            this.cachedRepos.set(repoId, repo);
            return repo;
          })
        );
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