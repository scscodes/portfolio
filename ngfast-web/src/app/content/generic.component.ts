import { Component } from '@angular/core';

/**
 * Generic component demonstrating responsive design patterns
 * and typography system usage
 */
@Component({
  selector: 'app-generic',
  template: `
    <div class="container">
      <!-- Typography showcase -->
      <h1>Main Heading</h1>
      <p class="lead">This is a lead paragraph that scales responsively across breakpoints.</p>
      
      <div class="content-section">
        <h2>Section Title</h2>
        <p>Regular paragraph text that demonstrates our base typography settings. 
           The font size and spacing will adjust automatically based on screen size.</p>
        
        <!-- Pills showcase -->
        <div class="pill-container">
          <span class="pill primary">Primary</span>
          <span class="pill success outline">Success</span>
          <span class="pill typescript">TypeScript</span>
          <span class="pill scss outline">SCSS</span>
        </div>
      </div>

      <!-- Responsive grid example -->
      <div class="responsive-grid">
        <div class="grid-item">
          <h3>Card 1</h3>
          <p class="small">Small text example</p>
        </div>
        <div class="grid-item">
          <h3>Card 2</h3>
          <p class="text-muted">Muted text example</p>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .content-section {
      margin: 2rem 0;
    }

    .pill-container {
      margin: 1rem 0;
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .responsive-grid {
      display: grid;
      gap: var(--spacing-unit);
      grid-template-columns: 1fr;
      margin: 2rem 0;

      @media (min-width: 768px) {
        grid-template-columns: repeat(2, 1fr);
      }

      @media (min-width: 992px) {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    .grid-item {
      padding: var(--spacing-unit);
      background: #f5f5f5;
      border-radius: 8px;
      
      h3 {
        margin-bottom: 0.5rem;
      }
    }
  `]
})
export class GenericComponent {
  constructor() {}
}
