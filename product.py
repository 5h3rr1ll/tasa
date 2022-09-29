#!/usr/bin/env python3

class Product():
    
    def  __init__(
        self, 
        name: str, 
        image: str, 
        stars: str, 
        ratings: str, 
        price: str, 
        url: str
        ) -> None:
        self.name = name
        self.image = image
        self.stars = stars
        self.ratings = ratings
        self.price = price
        self.url = url
        
    def __str__(self) -> str:
        return f"""
        Name: {self.name} 
        Image: {self.image}
        Stars: {self.stars}
        Ratings: {self.ratings}
        price: {self.price}
        URL: {self.url}
        """
    
    def __name__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.__str__()