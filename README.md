# Steven Salmons - Portfolio

A modern, responsive portfolio Single Page Application built with Angular and Angular Material, showcasing Steven Salmons' professional experience, skills, and projects.

## Features

- **Modern Design**: Clean, responsive design with Angular Material components
- **Portfolio Showcase**: Display of software engineering and DevOps projects with filtering by type
- **Detailed Project Pages**: Showcase project details, technologies, and challenges
- **About/Resume Section**: Presents professional experience, education, and skills
- **Responsive Layout**: Optimized for all device sizes

## Technologies Used

- Angular 19
- Angular Material
- TypeScript
- SCSS with BEM methodology
- RxJS

## Project Structure

```
src/
├── app/
│   ├── components/
│   │   ├── about/
│   │   ├── home/
│   │   └── portfolio/
│   │       └── project-detail/
│   ├── shared/
│   │   ├── layout/
│   │   ├── models/
│   │   ├── pipes/
│   │   └── services/
│   ├── app.component.ts
│   ├── app.config.ts
│   └── app.routes.ts
├── assets/
│   └── images/
└── styles.scss
```

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- npm (v9 or higher)

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/scscodes/portfolio.git
   cd portfolio
   ```

2. Install dependencies
   ```bash
   npm install
   ```

3. Start the development server
   ```bash
   npm start
   ```

4. Open your browser and navigate to `http://localhost:4200`

## Deployment to GitHub Pages

### Manual Deployment

1. Build the application with the GitHub Pages base href
   ```bash
   npm run build
   ```

2. Deploy to GitHub Pages
   ```bash
   npm run deploy
   ```

### Automated Deployment

This project is configured with a GitHub Actions workflow that automatically deploys to GitHub Pages when changes are pushed to the main branch.

1. Push your changes to the main branch
   ```bash
   git push origin main
   ```

2. GitHub Actions will automatically build and deploy the application to GitHub Pages.

3. Your site will be available at `https://[your-github-username].github.io/portfolio/`

## Contact

- GitHub: [github.com/scscodes](https://github.com/scscodes)
- LinkedIn: [linkedin.com/in/ssalmons](https://linkedin.com/in/ssalmons)
- Email: stevencsalmons@gmail.com

## License

This project is licensed under the MIT License - see the LICENSE file for details.
