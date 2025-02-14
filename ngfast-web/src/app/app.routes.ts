import { Routes } from '@angular/router';
import { HomeComponent } from './content/static/home.component';
import { NotFoundComponent } from './content/static/notfound.component';
import { GenericComponent } from './content/generic.component';


export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'home', redirectTo: '' },
  { path: 'generic', component: GenericComponent },
  { path: '**', component: NotFoundComponent },
];
