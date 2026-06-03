import { Component } from '@angular/core';
import { BooksService } from '../../services/books.service';

@Component({
  selector: 'app-subscription',
  template: `
    <div class="subscription-page">
      <h1>Le Libros Caribe Premium</h1>
      <div class="plans">
        <div class="plan free">
          <h2>Gratis</h2>
          <p class="price">$0 / mes</p>
          <ul>
            <li>✅ Acceso a +70,000 libros</li>
            <li>✅ Biblioteca personal</li>
            <li>✅ Lectura online</li>
            <li>❌ Sin anotaciones</li>
            <li>❌ Con anuncios</li>
            <li>❌ Sin modo offline</li>
          </ul>
        </div>
        <div class="plan premium">
          <div class="badge">Más popular</div>
          <h2>Premium</h2>
          <p class="price">$5 / mes</p>
          <ul>
            <li>✅ Todo lo del plan gratis</li>
            <li>✅ Anotaciones y subrayados</li>
            <li>✅ Sin anuncios</li>
            <li>✅ Descarga para leer offline</li>
            <li>✅ Soporte prioritario</li>
          </ul>
          <button (click)="subscribe()" class="btn-primary" [disabled]="loading">
            {{ loading ? 'Redirigiendo...' : 'Suscribirme ahora' }}
          </button>
        </div>
      </div>
      <div *ngIf="successMessage" class="success-banner">
        🎉 ¡Bienvenido a Premium! Tu cuenta ha sido actualizada.
      </div>
    </div>
  `,
})
export class SubscriptionComponent {
  loading = false;
  successMessage = false;

  constructor(private booksService: BooksService) {
    if (window.location.pathname.includes('success')) {
      this.successMessage = true;
    }
  }

  subscribe() {
    this.loading = true;
    this.booksService.createCheckout().subscribe({
      next: (res) => window.location.href = res.checkout_url,
      error: () => { this.loading = false; },
    });
  }
}
