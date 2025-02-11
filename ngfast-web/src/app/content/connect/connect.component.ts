import { CommonModule, NgFor } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatSnackBar, MatSnackBarModule } from '@angular/material/snack-bar';
import { GithubService } from '../../shared/services/github.service';

@Component({
  selector: 'app-connect',
  standalone: true,
  imports: [
    ReactiveFormsModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatIconModule,
    MatSnackBarModule,
    CommonModule
  ],
  templateUrl: './connect.component.html',
  styleUrls: ['./connect.component.scss']
})
export class ConnectComponent implements OnInit {
  contactForm: FormGroup;
  isSubmitting = false;
  socialLinks: { name: string; url: string; iconClass: string; }[] = [];

  constructor(
    private fb: FormBuilder,
    private snackBar: MatSnackBar,
    private githubService: GithubService
  ) {
    this.contactForm = this.fb.group({
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      message: ['', Validators.required]
    });
  }

  ngOnInit() {
    const githubConfig = this.githubService.getConfig();
    
    this.socialLinks = [
      {
        name: 'GitHub',
        url: githubConfig.profileUrl,
        iconClass: 'devicon-github-original'
      },
      {
        name: 'LinkedIn',
        url: 'https://linkedin.com/in/ssalmons',
        iconClass: 'devicon-linkedin-plain'
      }
    ];
  }

  onSubmit() {
    if (this.contactForm.valid && !this.isSubmitting) {
      this.isSubmitting = true;

      // Simulating an API call
      setTimeout(() => {
        try {
          // TODO: Replace with actual form submission logic
          console.log('Form submitted:', this.contactForm.value);
          
          this.snackBar.open('Message sent successfully!', 'Close', {
            duration: 5000,
            horizontalPosition: 'end',
            verticalPosition: 'top',
            panelClass: ['success-snackbar']
          });
          
          this.contactForm.reset();
          Object.keys(this.contactForm.controls).forEach(key => {
            this.contactForm.get(key)?.setErrors(null);
          });
        } catch (error) {
          this.snackBar.open('Failed to send message. Please try again.', 'Close', {
            duration: 5000,
            horizontalPosition: 'end',
            verticalPosition: 'top',
            panelClass: ['error-snackbar']
          });
        } finally {
          this.isSubmitting = false;
        }
      }, 1000); // Simulated delay
    }
  }
} 