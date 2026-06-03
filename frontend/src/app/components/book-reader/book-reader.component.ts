import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BooksService } from '../../services/books.service';

@Component({
  selector: 'app-book-reader',
  templateUrl: './book-reader.component.html',
})
export class BookReaderComponent implements OnInit {
  book: any = null;
  loading = true;

  constructor(private route: ActivatedRoute, private booksService: BooksService) {}

  ngOnInit() {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.booksService.getBook(id).subscribe({
      next: (book) => { this.book = book; this.loading = false; },
      error: () => { this.loading = false; },
    });
  }
}
