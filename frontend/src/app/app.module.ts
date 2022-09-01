import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { CancionesModule } from './canciones/canciones.module';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    CancionesModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
