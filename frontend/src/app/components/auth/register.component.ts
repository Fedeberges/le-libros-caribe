import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-register',
  template: `
    <div class="auth-page">
      <div class="auth-card">
        <h2>Crear cuenta</h2>
        <form (ngSubmit)="onRegister()">
          <input type="text" [(ngModel)]="fullName" name="fullName" placeholder="Nombre completo" />
          <input type="email" [(ngModel)]="email" name="email" placeholder="Email" required />
          <input type="password" [(ngModel)]="password" name="password" placeholder="Contraseña (min. 8 caracteres)" required />
          <button type="submit" class="btn-primary" [disabled]="loading">
            {{ loading ? 'Creando cuenta...' : 'Registrarse' }}
          </button>
          <p *ngIf="error" class="error">{{ error }}</p>
        </form>
        <p>¿Ya tienes cuenta? <a routerLink="/login">Inicia sesión</a></p>
      </div>
    </div>
  `,
})
export class RegisterComponent {
  fullName = ''; email = ''; password = ''; loading = false; error = '';

  constructor(private authService: AuthService, private router: Router) {}

  onRegister() {
    this.loading = true; this.error = '';
    this.authService.register(this.email, this.password, this.fullName).subscribe({
      next: () => this.router.navigate(['/login']),
      error: (err) => { this.error = err.error?.detail || 'Error al registrarse'; this.loading = false; },
    });
  }
}
