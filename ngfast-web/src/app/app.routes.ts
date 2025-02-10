import { Routes } from '@angular/router';
import { HomeComponent } from './content/home.component';
import { NotFoundComponent } from './content/notfound.component';
import { AboutComponent } from './content/about/about.component';
import { PortfolioComponent } from './content/portfolio/portfolio.component';
import { ConnectComponent } from './content/connect/connect.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: 'portfolio', component: PortfolioComponent },
  { path: 'connect', component: ConnectComponent },
  { path: '**', component: NotFoundComponent },
];
