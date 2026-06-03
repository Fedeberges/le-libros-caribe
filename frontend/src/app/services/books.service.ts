import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({ providedIn: 'root' })
export class BooksService {
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  getBooks(params: { q?: string; language?: string; subject?: string; page?: number; per_page?: number } = {}) {
    let httpParams = new HttpParams();
    if (params.q) httpParams = httpParams.set('q', params.q);
    if (params.language) httpParams = httpParams.set('language', params.language);
    if (params.subject) httpParams = httpParams.set('subject', params.subject);
    if (params.page) httpParams = httpParams.set('page', params.page.toString());
    if (params.per_page) httpParams = httpParams.set('per_page', params.per_page.toString());
    return this.http.get<any>(`${this.apiUrl}/books/`, { params: httpParams });
  }

  getBook(id: number) {
    return this.http.get<any>(`${this.apiUrl}/books/${id}`);
  }

  addToLibrary(bookId: number) {
    return this.http.post(`${this.apiUrl}/books/${bookId}/library`, {});
  }

  getMyLibrary() {
    return this.http.get<any[]>(`${this.apiUrl}/books/my/library`);
  }

  createCheckout() {
    return this.http.post<{ checkout_url: string }>(`${this.apiUrl}/subscriptions/checkout`, {});
  }
}
