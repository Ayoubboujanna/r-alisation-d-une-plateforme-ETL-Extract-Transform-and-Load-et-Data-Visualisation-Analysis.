import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {HttpClientModule} from '@angular/common/http';
import {ApolloModule, Apollo } from 'apollo-angular';
import {HttpLinkModule, HttpLink} from 'apollo-angular-link-http'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { InMemoryCache } from 'apollo-cache-inmemory';
import { ListComponent } from './list/list.component';

@NgModule({
  declarations: [
    AppComponent,
    ListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ApolloModule,
    HttpLinkModule
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { 
  constructor(
    apollo:Apollo,
    httpLink:HttpLink
  ){
    apollo.create({ 
      cache: new InMemoryCache() as any,
      link : httpLink.create({ uri: 'http://127.0.0.1:8000'}) as any
     
    })
  }

}
