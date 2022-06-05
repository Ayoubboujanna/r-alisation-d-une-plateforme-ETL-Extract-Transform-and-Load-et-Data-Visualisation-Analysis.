export type Film = {
    rang:number;
    movieName:string;
    year:number;
    rating:number;
    gross:number;
    director:string;
    stars:string;
    votes:number;
}

export type Query ={
    allFilms: Film[];
}
