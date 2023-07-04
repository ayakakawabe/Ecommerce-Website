export interface ItemType{
    id:number,
    name:string,
    price:number,
    imgUrl:string,
    description:string
}

export interface NewsType{
    date:string,
    title:string,
    detail:string
}

export interface CategoryType{
    title:string,
    titleJP:string,
    imgUrl:string
}

export interface ItemTypeLong{
    id:number,
    name:string,
    price:number,
    imgUrl:string[],
    description:string
}

export interface ItemTypeAll{
    id:number,
    name:string,
    price:number,
    category:string,
    imgUrl:string[],
    description:string
}