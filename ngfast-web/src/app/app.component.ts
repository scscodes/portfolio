import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { MatIconModule } from '@angular/material/icon';
import { MatMenuModule } from '@angular/material/menu';
import { MatButtonModule } from '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,
    RouterLink,
    MatToolbarModule,
    MatButtonModule,
    MatIconModule,
    MatMenuModule,
    MatSidenavModule,
    MatListModule],
  templateUrl: './app.component.html',
  styles: `
// todo consolidate this into sidenav styles
  .sidenav-container {
  height: calc(100vh - 64px);
}

mat-sidenav {
  width: 250px;
}

  `

})
export class AppComponent {
  title = 'ngfast-web';

  constructor() {
    console.log('AppComponent');
  }
}
