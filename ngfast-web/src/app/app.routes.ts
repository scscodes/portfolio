import { Routes } from '@angular/router';
import { HomeComponent } from './content/static/home.component';
import { NotFoundComponent } from './content/static/notfound.component';
import { AboutComponent } from './content/about/about.component';
import { PortfolioComponent } from './content/portfolio/portfolio.component';
import { ConnectComponent } from './content/connect/connect.component';
import { GenericComponent } from './content/generic.component';
export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: 'portfolio', component: PortfolioComponent },
  { path: 'connect', component: ConnectComponent },
  { path: 'generic', component: GenericComponent },
  { path: '**', component: NotFoundComponent },
];
