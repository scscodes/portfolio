import { DOCUMENT } from '@angular/common';
import { Component, Inject } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';
import { NgIf, AsyncPipe } from '@angular/common';

/**
 * Component that provides authentication controls via Auth0
 */
@Component({
  selector: 'app-auth-button',
  standalone: true,
  imports: [NgIf, AsyncPipe],
  template: `
  <ng-container *ngIf="auth.isAuthenticated$ | async; else loggedOut">
      <button (click)="auth.logout({ logoutParams: { returnTo: document.location.origin } })">
        Log out
      </button>
    </ng-container>

    <ng-template #loggedOut>
      <button (click)="auth.loginWithRedirect()">Log in</button>
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
