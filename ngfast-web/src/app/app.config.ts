import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { provideHttpClient } from '@angular/common/http';

import { provideAuth0 } from '@auth0/auth0-angular';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';

export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),
    provideHttpClient(),
    provideAuth0({
      domain: 'dev-9jhx2vm6.us.auth0.com',
      clientId: 'atdUY3OJN3qO9AxeXJ26rwQcW7vd4naH',
      authorizationParams: {
        redirect_uri: 'http://localhost:4200',
      },
    }), provideAnimationsAsync('noop'),

  ]
};
