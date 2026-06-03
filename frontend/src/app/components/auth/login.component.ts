import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-login',
  template: `
    <div class="auth-page">
      <div class="auth-card">
        <h2>Iniciar sesión</h2>
        <form (ngSubmit)="onLogin()">
          <input type="email" [(ngModel)]="email" name="email" placeholder="Email" required />
          <input type="password" [(ngModel)]="password" name="password" placeholder="Contraseña" required />
          <button type="submit" class="btn-primary" [disabled]="loading">
            {{ loading ? 'Entrando...' : 'Entrar' }}
          </button>
          <p *ngIf="error" class="error">{{ error }}</p>
        </form>
        <p>¿No tienes cuenta? <a routerLink="/registro">Regístrate</a></p>
      </div>
    </div>
  `,
})
export class LoginComponent {
  email = ''; password = ''; loading = false; error = '';

  constructor(private authService: AuthService, private router: Router) {}

  onLogin() {
    this.loading = true; this.error = '';
    this.authService.login(this.email, this.password).subscribe({
      next: () => this.router.navigate(['/']),
      error: () => { this.error = 'Email o contraseña incorrectos'; this.loading = false; },
    });
  }
}
