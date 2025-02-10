import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatMenuModule } from '@angular/material/menu';

/**
 * Component that provides application settings controls
 */
@Component({
  selector: 'app-settings-button',
  standalone: true,
  imports: [MatButtonModule, MatIconModule, MatMenuModule],
  template: `
    <button mat-icon-button [matMenuTriggerFor]="settingsMenu">
      <mat-icon>settings</mat-icon>
    </button>
    <mat-menu #settingsMenu="matMenu" 
              xPosition="before"
              yPosition="below"
              [overlapTrigger]="false">
      <button mat-menu-item>
        <mat-icon>brightness_medium</mat-icon>
        <span>Theme</span>
      </button>
      <button mat-menu-item>
        <mat-icon>language</mat-icon>
        <span>Language</span>
      </button>
    </mat-menu>
  `
})
export class SettingsButtonComponent {
  constructor() {}
} 