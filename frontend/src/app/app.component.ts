import {Component, inject} from '@angular/core';
import {RouterOutlet} from '@angular/router';
import {HttpClient} from '@angular/common/http';
import {AsyncPipe, JsonPipe} from '@angular/common';
import {Observable} from 'rxjs';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, AsyncPipe, JsonPipe],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  httpClient = inject(HttpClient);
  cars: Observable<any>;
  bookings: Observable<any>;

  constructor() {
    this.cars = this.httpClient.get('/api/cars');
    this.bookings = this.httpClient.get('/api/bookings');
  }
}
