import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home.component';
import { NotFoundComponent } from './pages/notfound.component';
export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: '**', component: NotFoundComponent },
];
