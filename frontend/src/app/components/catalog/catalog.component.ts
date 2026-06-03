import { Component, OnInit } from '@angular/core';
import { BooksService } from '../../services/books.service';

@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html',
})
export class CatalogComponent implements OnInit {
  books: any[] = [];
  total = 0;
  page = 1;
  perPage = 20;
  search = '';
  language = '';
  loading = false;

  constructor(private booksService: BooksService) {}

  ngOnInit() { this.loadBooks(); }

  loadBooks() {
    this.loading = true;
    this.booksService.getBooks({ q: this.search, language: this.language, page: this.page, per_page: this.perPage })
      .subscribe((res: any) => {
        this.books = res.books;
        this.total = res.total;
        this.loading = false;
      });
  }

  onSearch() { this.page = 1; this.loadBooks(); }
  nextPage() { this.page++; this.loadBooks(); }
  prevPage() { if (this.page > 1) { this.page--; this.loadBooks(); } }

  addToLibrary(bookId: number) {
    this.booksService.addToLibrary(bookId).subscribe();
  }
}
