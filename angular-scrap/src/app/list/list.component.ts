import { Component, OnInit } from '@angular/core';
import { Apollo } from 'apollo-angular';
import { Observable } from 'rxjs';
import { map } from 'rxjs';

import gql from 'graphql-tag';

import { Film , Query} from '../types'

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {
  films: Observable<Film[]> | undefined;
  constructor(private apollo:Apollo) { }

  ngOnInit(): void {
    this.films= this.apollo.watchQuery<Query>({
      query:gql`
       query allFilms{
         
          rang
          movieName
          year
          rating
          gross
          director
          stars
          votes
        
       }
       `
    })
      .valueChanges
      .pipe(
        map(result=>result.data.allFilms)
      );
  }

}
