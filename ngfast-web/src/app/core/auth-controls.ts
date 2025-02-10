import { DOCUMENT } from '@angular/common';
import { Component, Inject } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';
import { NgIf, AsyncPipe } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';

/**
 * Component that provides authentication controls via Auth0
 */
@Component({
  selector: 'app-auth-button',
  standalone: true,
  imports: [NgIf, AsyncPipe, MatButtonModule, MatIconModule],
  template: `
    <ng-container *ngIf="auth.isAuthenticated$ | async; else loggedOut">
      <button mat-stroked-button 
              color="warn"
              (click)="auth.logout({ logoutParams: { returnTo: document.location.origin } })">
        <mat-icon>logout</mat-icon>
        Log out
      </button>
    </ng-container>

    <ng-template #loggedOut>
      <button mat-stroked-button 
              color="primary"
              (click)="auth.loginWithRedirect()">
        <mat-icon>login</mat-icon>
        Log in
      </button>
    </ng-template>
  `
})
export class AuthButtonComponent {
    constructor(@Inject(DOCUMENT) public document: Document, public auth: AuthService) {}
  /**
   * Initiates Auth0 login flow with redirect
   */
  login(): void {
    this.auth.loginWithRedirect();
  }
}
